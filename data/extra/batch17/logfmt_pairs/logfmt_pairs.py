def parse_logfmt(line):
    cs = list(line)
    out = {}
    i = 0
    while i < len(cs):
        while i < len(cs) and cs[i] == ' ':
            i += 1
        key = []
        while i < len(cs) and cs[i] != '=' and cs[i] != ' ':
            key.append(cs[i])
            i += 1
        val = []
        if i < len(cs) and cs[i] == '=':
            i += 1
            if i < len(cs) and cs[i] == '"':
                i += 1
                while i < len(cs) and cs[i] != '"':
                    val.append(cs[i])
                    i += 1
                i += 1
            else:
                while i < len(cs) and cs[i] != ' ':
                    val.append(cs[i])
                    i += 1
        if len(key) > 0:
            out["".join(key)] = "".join(val)
    return out

lines = ['level=info msg="server up" port=8080', 'level=info path=/home dur=35ms status=200', 'level=warn path=/search dur=240ms status=200 cached', 'level=error path=/pay dur=80ms status=502 msg="upstream closed"', 'level=info path=/img dur=12ms status=304', 'level=error msg="disk almost full" free=2%']
levels = {}
for i, line in enumerate(lines):
    m = parse_logfmt(line)
    level = m.get("level", "info")
    levels[level] = levels.get(level, 0) + 1
    dur_text = m.get("dur", "0ms")
    d = dur_text[:-2] if dur_text.endswith("ms") else "0"
    dur = int(d) if d.isdigit() else 0
    if level == "error" or dur > 100:
        what = m["msg"] if "msg" in m else m.get("path", "?")
        flag = " (cached)" if "cached" in m else ""
        print(f"line {i + 1}: {level} {what} {dur}ms{flag}")
for k, v in levels.items():
    print(f"{k:<6} {v}")
