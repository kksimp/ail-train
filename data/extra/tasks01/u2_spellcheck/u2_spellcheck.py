import sys

def main():
    lines = sys.stdin.read().splitlines()
    sep = -1
    for i, ln in enumerate(lines):
        if ln.strip(" \t") == "---":
            sep = i
            break
    if sep < 0:
        print("bad input")
        return
    dic = set()
    for ln in lines[:sep]:
        w = ln.strip().lower()
        if w:
            dic.add(w)
    bad = 0
    uniq = set()
    for n, ln in enumerate(lines[sep + 1:], 1):
        i = 0
        while i < len(ln):
            ch = ln[i]
            if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
                j = i
                while j < len(ln) and (("a" <= ln[j] <= "z") or ("A" <= ln[j] <= "Z")):
                    j += 1
                w = ln[i:j]
                if w.lower() not in dic:
                    print(f"{n}:{i + 1} {w}")
                    bad += 1
                    uniq.add(w.lower())
                i = j
            else:
                i += 1
    if bad == 0:
        print("all words ok")
    else:
        print(f"misspelled={bad} unique={len(uniq)}")

main()
