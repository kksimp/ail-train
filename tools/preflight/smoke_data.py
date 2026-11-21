"""M1 preflight: token statistics and the smoke-run data for one candidate base.

Usage: python smoke_data.py MODEL_DIR CARD AIL_ROOT REPO_ROOT OUT_DIR [SEQ]

MODEL_DIR is a local model folder (its tokenizer and chat template are used), CARD the core language card, AIL_ROOT
an ail checkout (corpus/), REPO_ROOT this repository (data/extra/). Writes OUT_DIR/data/{train,valid}.jsonl (the
longest `port` examples whose full chat length fits SEQ, so the smoke run measures the worst case at that length)
and OUT_DIR/tokens.json. Deterministic for the same inputs.
"""

import json
import os
import sys

from transformers import AutoTokenizer


def programs(ail_root, repo_root):
    """(group, name, ail, py) for every corpus and data/extra program that has a Python twin, sorted by path."""
    out = []
    roots = [os.path.join(ail_root, "corpus")]
    extra = os.path.join(repo_root, "data", "extra")
    roots += sorted(os.path.join(extra, d) for d in os.listdir(extra) if os.path.isdir(os.path.join(extra, d)))
    for root in roots:
        for name in sorted(os.listdir(root)):
            base = os.path.join(root, name, name)
            if os.path.isfile(base + ".ail") and os.path.isfile(base + ".py"):
                with open(base + ".ail", encoding="utf-8") as f:
                    ail = f.read()
                with open(base + ".py", encoding="utf-8") as f:
                    py = f.read()
                out.append((os.path.basename(root), name, ail, py))
    return out


def task_text(ail):
    """The `##` header comment of a program: the task it states."""
    lines = []
    for line in ail.splitlines():
        if line.startswith("##"):
            lines.append(line[2:].strip())
        elif lines:
            break
    return " ".join(lines) or "Write this program in AIL."


def chat(card, user, assistant):
    return [
        {"role": "system", "content": card},
        {"role": "user", "content": user},
        {"role": "assistant", "content": assistant},
    ]


def pct(xs, p):
    if not xs:
        return 0
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(p / 100.0 * len(xs)))]


def main():
    model_dir, card_path, ail_root, repo_root, out_dir = sys.argv[1:6]
    seq = int(sys.argv[6]) if len(sys.argv) > 6 else 4096
    tok = AutoTokenizer.from_pretrained(model_dir)
    with open(card_path, encoding="utf-8") as f:
        card = f.read()

    def length(msgs):
        ids = tok.apply_chat_template(msgs, tokenize=True)
        if not isinstance(ids, list):  # newer transformers return a dict-like encoding
            ids = ids["input_ids"]
        return len(ids)

    progs = programs(ail_root, repo_root)
    corpus = [p for p in progs if p[0] == "corpus"][:20]
    stats = {
        "programs": len(progs),
        "card_tokens": len(tok.encode(card)),
        "card_chars": len(card),
        "corpus20_ail_tokens": sum(len(tok.encode(p[2])) for p in corpus),
        "corpus20_ail_chars": sum(len(p[2]) for p in corpus),
        "corpus20_py_tokens": sum(len(tok.encode(p[3])) for p in corpus),
    }
    stats["corpus20_ail_tokens_per_program"] = round(stats["corpus20_ail_tokens"] / max(1, len(corpus)), 1)
    stats["ail_chars_per_token"] = round(stats["corpus20_ail_chars"] / max(1, stats["corpus20_ail_tokens"]), 2)

    write_len, port_len, ports = [], [], []
    for group, name, ail, py in progs:
        w = length(chat(card, task_text(ail), ail))
        msgs = chat(card, "Port this Python program to AIL.\n\n" + py, ail)
        p = length(msgs)
        write_len.append(w)
        port_len.append(p)
        ports.append((p, group + "/" + name, msgs))
    for fam, xs in (("write", write_len), ("port", port_len)):
        stats[fam] = {
            "count": len(xs),
            "p50": pct(xs, 50),
            "p90": pct(xs, 90),
            "p99": pct(xs, 99),
            "max": max(xs) if xs else 0,
            "over_2048": sum(1 for x in xs if x > 2048),
            "over_3072": sum(1 for x in xs if x > 3072),
            "over_4096": sum(1 for x in xs if x > 4096),
            "over_6144": sum(1 for x in xs if x > 6144),
        }

    fits = sorted((x for x in ports if x[0] <= seq), key=lambda x: (-x[0], x[1]))[:60]
    os.makedirs(os.path.join(out_dir, "data"), exist_ok=True)
    for split, rows in (("train", fits[:50]), ("valid", fits[50:60])):
        with open(os.path.join(out_dir, "data", split + ".jsonl"), "w", encoding="utf-8") as f:
            for _, _, msgs in rows:
                f.write(json.dumps({"messages": msgs}, ensure_ascii=False) + "\n")
    stats["smoke_examples"] = len(fits)
    stats["smoke_tokens_min"] = fits[-1][0] if fits else 0
    stats["smoke_tokens_max"] = fits[0][0] if fits else 0
    stats["smoke_tokens_total_train"] = sum(x[0] for x in fits[:50])
    with open(os.path.join(out_dir, "tokens.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, sort_keys=True)
    print(json.dumps(stats, sort_keys=True))


if __name__ == "__main__":
    main()
