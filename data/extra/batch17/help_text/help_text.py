class Opt:
    def __init__(self, short, long, arg, help, default):
        self.short, self.long, self.arg, self.help, self.default = short, long, arg, help, default

def left_col(o):
    s = "    " if o.short == "" else f"-{o.short}, "
    a = "" if o.arg == "" else f" {o.arg}"
    return f"  {s}--{o.long}{a}"

def fit(text, width):
    lines = []
    cur = []
    used = 0
    for w in text.split():
        if used > 0 and used + 1 + len(w) > width:
            lines.append(" ".join(cur))
            cur = []
            used = 0
        used += len(w) if used == 0 else len(w) + 1
        cur.append(w)
    if len(cur) > 0:
        lines.append(" ".join(cur))
    return lines

opts = [Opt("o", "output", "FILE", "write the report to FILE instead of standard output", ""), Opt("n", "lines", "N", "show only the first N matching lines", "20"), Opt("", "color", "WHEN", "colour the output: always, never or auto, where auto colours only when writing to a terminal", "auto"), Opt("v", "verbose", "", "explain each step", ""), Opt("h", "help", "", "show this help and exit", "")]
print("usage: logscan [OPTIONS] PATTERN [FILE...]")
print("options:")
col = max(len(left_col(o)) for o in opts)
for o in opts:
    text = o.help
    if o.default != "":
        text = f"{o.help} (default: {o.default})"
    parts = fit(text, 34)
    print(f"{left_col(o).ljust(col + 2, ' ')}{parts[0]}")
    for p in parts[1:]:
        print(" " * (col + 2) + p)
