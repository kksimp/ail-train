"""M1 preflight: one table from a preflight run folder. Usage: python summarize.py RUN_DIR
Writes RUN_DIR/SUMMARY.md and prints it. The run folder names the candidates, so it never goes into git (D6)."""

import json
import os
import re
import statistics
import sys

REPORT = re.compile(
    r"Iter (\d+): Train loss ([\d.na]+).*?It/sec ([\d.]+), Tokens/sec ([\d.]+).*?Peak mem ([\d.]+) GB"
)


def read_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


# mlx-lm 0.32 prints a table instead: "iter train_loss tok/s tokens" rows.
# Rows look like "     2    0.554 ▼       60      1.4k" (the arrow is optional; tokens may carry a k suffix).
TABLE = re.compile(r"^\s*(\d+)\s+([\d.]+)\s+(?:[^\s\d.]+\s+)?([\d.]+)\s+([\d.]+k?)\s*$", re.M)


def lora_numbers(log, peak):
    log = re.sub(r"\x1b\[[0-9;]*m", "", log)  # mlx-lm 0.32 colours the table
    rows = [m.groups() for m in REPORT.finditer(log)]
    if not rows:
        t = [m.groups() for m in TABLE.finditer(log)]
        rows = [(it, loss, "0", tps, peak or "0") for it, loss, tps, _ in t]
    if not rows:
        return {}
    later = rows[1:] or rows
    tps = statistics.median(float(r[3]) for r in later)
    its = statistics.median(float(r[2]) for r in later)
    return {
        "steps": int(rows[-1][0]),
        "loss_first": rows[0][1],
        "loss_last": rows[-1][1],
        "train_tok_s": round(tps, 1),
        "s_per_step": round(1 / its, 1) if its else None,
        "peak_gb": peak or max(float(r[4]) for r in rows),
        "hours_per_1M_tokens": round(1e6 / tps / 3600, 2) if tps else None,
    }


def main():
    run = sys.argv[1]
    cands = sorted(d for d in os.listdir(run) if os.path.isdir(os.path.join(run, d)) and d[:1].isdigit())
    lines = ["# M1 preflight summary", "", read(os.path.join(run, "system.txt")).strip(), ""]
    head = (
        "| # | candidate | status | disk GB | card tok | AIL tok/prog (20) | AIL chars/tok | port p90 / max tok"
        " | port > 4096 | train peak GB | train tok/s | s/step | h per 1M tok | swap delta MB | gen tok/s | prefill tok/s"
        " | gen peak GB |"
    )
    lines += [head, "|" + "---|" * 17]
    answers = []
    for c in cands:
        d = os.path.join(run, c)
        name = read(os.path.join(d, "model.txt")).strip()
        status = read(os.path.join(d, "status.txt")).strip() or "not run"
        t = read_json(os.path.join(d, "tokens.json"))
        g = read_json(os.path.join(d, "gen.json"))
        peak = read(os.path.join(d, "peak_gb.txt")).strip()
        l = lora_numbers(read(os.path.join(d, "lora.log")), peak)
        if not l and peak:
            l = {"peak_gb": peak}
        swap = read(os.path.join(d, "swap_delta_mb.txt")).strip()
        free = [int(x) for x in read(os.path.join(d, "free_pct.txt")).split() if x.isdigit()]
        if free:
            swap += " (min free {}%)".format(min(free))
        disk = read(os.path.join(d, "disk_gb.txt")).strip()
        port = t.get("port", {})
        lines.append(
            "| {} | {} | {} | {} | {} | {} | {} | {} / {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
                c, name, status, disk, t.get("card_tokens", ""), t.get("corpus20_ail_tokens_per_program", ""),
                t.get("ail_chars_per_token", ""), port.get("p90", ""), port.get("max", ""), port.get("over_4096", ""),
                l.get("peak_gb", ""), l.get("train_tok_s", ""), l.get("s_per_step", ""),
                l.get("hours_per_1M_tokens", ""), swap, g.get("generation_tps", ""), g.get("prompt_tps", ""),
                g.get("peak_memory_gb", ""),
            )
        )
        if g.get("answer"):
            answers.append("### {} ({}), untrained answer\n\n```\n{}\n```\n".format(c, name, g["answer"].strip()))
        if l.get("steps"):
            answers.append("{} loss {} -> {} over {} steps".format(c, l["loss_first"], l["loss_last"], l["steps"]))
    lines += ["", "Train numbers: batch 1, LoRA rank 16 (layers as in the header), gradient checkpointing, prompt masked, the 50",
              "longest port examples that fit the sequence cap. Hours per 1M tokens is trained tokens at the median rate.",
              ""] + answers
    text = "\n".join(lines) + "\n"
    with open(os.path.join(run, "SUMMARY.md"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
