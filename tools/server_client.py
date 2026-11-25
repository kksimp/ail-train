"""Generation through a local llama.cpp server (OpenAI-compatible /v1/chat/completions), for eval_quick.py and
eval_loop.py with --backend server. The server holds the model (a GGUF of the merged weights) on the GPU with several
parallel slots; callers run many requests at once from threads and the server batches them.

Sampling follows the transformers path: temperature and top_p from the command line, and the base model's own
generation_config.json for top_k and the repetition penalty (applied over the whole context, as transformers does);
min_p off. Each sample has its own seed (the caller's seed + sample index).
"""

import json
import os
import time
import urllib.error
import urllib.request


def sampling_defaults(model_dir):
    """top_k and repetition penalty the transformers path takes from the model's generation_config.json."""
    out = {"top_k": 0, "repeat_penalty": 1.0}
    p = os.path.join(model_dir or "", "generation_config.json")
    if os.path.isfile(p):
        g = json.load(open(p, encoding="utf-8"))
        if g.get("top_k") is not None:
            out["top_k"] = int(g["top_k"])
        if g.get("repetition_penalty") is not None:
            out["repeat_penalty"] = float(g["repetition_penalty"])
    return out


class ServerGen:
    def __init__(self, url, temp, max_tokens, model_dir="", timeout=900):
        self.url = url.rstrip("/") + "/v1/chat/completions"
        self.temp, self.max_tokens, self.timeout = temp, max_tokens, timeout
        self.extra = sampling_defaults(model_dir)
        self.wait_ready(url)

    @staticmethod
    def wait_ready(url, limit=600):
        t = time.time()
        while time.time() - t < limit:
            try:
                with urllib.request.urlopen(url.rstrip("/") + "/health", timeout=5) as r:
                    if r.status == 200:
                        return
            except (urllib.error.URLError, OSError):
                pass
            time.sleep(2)
        raise SystemExit("llama-server at {} is not ready".format(url))

    def one(self, msgs, seed):
        body = {"messages": msgs, "temperature": self.temp, "top_p": 1.0, "min_p": 0.0, "max_tokens": self.max_tokens,
                "seed": seed, "top_k": self.extra["top_k"], "repeat_penalty": self.extra["repeat_penalty"],
                "repeat_last_n": 8192, "stream": False}  # the server takes no -1; 8192 covers any slot's context
        req = urllib.request.Request(self.url, data=json.dumps(body).encode("utf-8"),
                                     headers={"Content-Type": "application/json"})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as r:
                    res = json.load(r)
                ch = res["choices"][0]
                u = res.get("usage", {})
                return ch["message"]["content"] or "", u.get("prompt_tokens", 0), u.get("completion_tokens", 0)
            except (urllib.error.URLError, OSError, KeyError, ValueError):
                if attempt == 2:
                    raise
                time.sleep(5)

    def gen(self, msgs, seed, n):
        """n samples: (texts, prompt tokens, generated tokens per sample, seconds). The n requests run at once."""
        import concurrent.futures
        t = time.time()
        with concurrent.futures.ThreadPoolExecutor(n) as ex:
            res = list(ex.map(lambda k: self.one(msgs, seed + k), range(n)))
        return [r[0] for r in res], (res[0][1] if res else 0), [r[2] for r in res], time.time() - t
