def tokenize(cs):
    out = []
    i = 0
    while i < len(cs):
        c = cs[i]
        j = i + 1
        if c == ' ':
            i = j
            continue
        if c == '"':
            while j < len(cs) and cs[j] != '"':
                j += 2 if cs[j] == '\\' else 1
            if j >= len(cs):
                return None, f"unterminated string at {i}"
            j += 1
        elif c.isalnum() or c == '-':
            while j < len(cs) and (cs[j].isalnum() or cs[j] == '.'):
                j += 1
            w = cs[i:j]
            if c.isalpha() and w not in ("true", "false", "null"):
                return None, f"unknown word '{w}' at {i}"
        elif c not in "{}[]:,":
            return None, f"unexpected '{c}' at {i}"
        out.append(cs[i:j])
        i = j
    return out, None

def kind(t):
    first = t[0]
    if first == '"':
        return "string"
    if first.isdigit() or first == '-':
        return "number"
    if first.isalpha():
        return "word"
    return "punct"

docs = ["{\"name\": \"Ada\", \"age\": 36, \"langs\": [\"en\", \"fr\"], \"admin\": false}", "[1, -2.5, {\"a\": [null, true]}]", "{\"quote\": \"say \\\"hi\\\"\"}", "{\"bad\": tru}", "[\"open]", "{\"x\": #1}"]
for d in docs:
    toks, err = tokenize(d)
    if toks is not None:
        depth = 0
        deepest = 0
        counts = {}
        for t in toks:
            counts[kind(t)] = counts.get(kind(t), 0) + 1
            if t == "{" or t == "[":
                depth += 1
                deepest = max(deepest, depth)
            elif t == "}" or t == "]":
                depth -= 1
        shown = ", ".join(f"{n} {k}" for k, n in counts.items())
        print(f"{len(toks)} tokens ({shown}), depth {deepest}")
    else:
        print(f"error: {err}")
