def decode(raw):
    out = []
    i = 0
    while i < len(raw):
        c = raw[i]
        if c != '\\':
            out.append(ord(c))
            i += 1
            continue
        if i + 1 >= len(raw):
            return None, f"lone backslash at {i}"
        e = raw[i + 1]
        if e == 'n':
            out.append(10)
            i += 2
        elif e == 't':
            out.append(9)
            i += 2
        elif e == '\\' or e == '"':
            out.append(ord(e))
            i += 2
        elif e == 'x':
            if i + 4 > len(raw):
                return None, f"short \\x code at {i}"
            hx = raw[i + 2:i + 4]
            try:
                v = int(hx, 16)
            except ValueError:
                return None, f"bad hex '{hx}' at {i}"
            out.append(v)
            i += 4
        elif e == 'u' and i + 2 < len(raw) and raw[i + 2] == '{':
            close = raw[i:].find("}")
            if close < 0:
                return None, f"unclosed \\u at {i}"
            hx = raw[i + 3:i + close]
            try:
                v = int(hx, 16)
            except ValueError:
                return None, f"bad hex '{hx}' at {i}"
            out.append(v)
            i += close + 1
        else:
            return None, f"unknown escape \\{e} at {i}"
    return out, None

for raw in [r"Hello\tWorld\n", "say \\\"hi\\\"", r"\x41\x42C", r"caf\u{e9} \u{1F600}", r"path\\to", r"bad \q here", r"cut \x4"]:
    codes, err = decode(raw)
    if codes is not None:
        shown = " ".join(str(n) if n < 128 else f"U+{n:x}" for n in codes)
        print(f"{raw:<22} {len(codes):>2} chars: {shown}")
    else:
        print(f"{raw:<22} error: {err}")
