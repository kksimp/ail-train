def split_words(cs):
    words = []
    cur = []
    started = False
    i = 0
    while i < len(cs):
        c = cs[i]
        if c == ' ':
            if started:
                words.append("".join(cur))
                cur = []
                started = False
            i += 1
        elif c == "'":
            started = True
            i += 1
            while i < len(cs) and cs[i] != "'":
                cur.append(cs[i])
                i += 1
            if i >= len(cs):
                return None, "unclosed single quote"
            i += 1
        elif c == '"':
            started = True
            i += 1
            while i < len(cs) and cs[i] != '"':
                if cs[i] == '\\' and i + 1 < len(cs):
                    i += 1
                cur.append(cs[i])
                i += 1
            if i >= len(cs):
                return None, "unclosed double quote"
            i += 1
        elif c == '\\' and i + 1 < len(cs):
            started = True
            cur.append(cs[i + 1])
            i += 2
        else:
            started = True
            cur.append(c)
            i += 1
    if started:
        words.append("".join(cur))
    return words, None

lines = ["cp notes.txt 'my notes.txt'", "echo \"say \\\"hi\\\"\" now", "grep -r hello\\ world src", "printf '' x", "rm 'unfinished", "a\"\"b 'c'd"]
for line in lines:
    ws, err = split_words(line)
    if ws is not None:
        shown = " ".join(f"[{w}]" for w in ws)
        print(f"{line:<29} -> {len(ws)} words: {shown}")
    else:
        print(f"{line:<29} -> error: {err}")
