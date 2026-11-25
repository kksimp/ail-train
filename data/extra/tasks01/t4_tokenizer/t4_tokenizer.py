import sys

KW = {"if", "else", "while", "return"}
for ln, line in enumerate(sys.stdin.read().split("\n"), 1):
    i, n = 0, len(line)
    while i < n:
        c = line[i]
        if c in " \t":
            i += 1
            continue
        j = i
        if c.isalpha() and c.isascii() or c == "_":
            while j < n and (line[j].isascii() and line[j].isalnum() or line[j] == "_"):
                j += 1
            t = line[i:j]
            kind = "KEYWORD" if t in KW else "IDENT"
        elif c.isascii() and c.isdigit():
            while j < n and line[j].isascii() and line[j].isdigit():
                j += 1
            kind = "INT"
            if j + 1 < n and line[j] == "." and line[j + 1].isascii() and line[j + 1].isdigit():
                j += 1
                while j < n and line[j].isascii() and line[j].isdigit():
                    j += 1
                kind = "FLOAT"
        elif c == '"':
            j = line.find('"', i + 1)
            if j < 0:
                print(f"{ln}:{i+1} ERROR {line[i:]}")
                break
            j += 1
            kind = "STRING"
        elif line[i:i+2] in ("==", "!=", "<=", ">=", "->"):
            j = i + 2
            kind = "OP"
        elif c in "+-*/%<>=!":
            j = i + 1
            kind = "OP"
        elif c in "(){},;:":
            j = i + 1
            kind = "PUNCT"
        else:
            j = i + 1
            kind = "ERROR"
        print(f"{ln}:{i+1} {kind} {line[i:j]}")
        i = j
