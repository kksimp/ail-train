import sys

def syl(tok):
    letters = [c for c in tok.lower() if "a" <= c <= "z"]
    if not letters:
        return 0
    count = 0
    prev = False
    for c in letters:
        v = c in "aeiouy"
        if v and not prev:
            count += 1
        prev = v
    return max(count, 1)

def main():
    text = sys.stdin.read().replace("!", ".").replace("?", ".")
    W = S = Y = 0
    for piece in text.split("."):
        n = 0
        for tok in piece.split():
            s = syl(tok)
            if s > 0:
                n += 1
                Y += s
        W += n
        if n > 0:
            S += 1
    if W == 0:
        print("no words")
        return
    a = W * 100 // S
    b = Y * 100 // W
    milli = 206835 - a * 1015 // 100 - b * 846
    score = 0 if milli < 0 else milli // 1000
    if score >= 90:
        level = "very easy"
    elif score >= 60:
        level = "standard"
    elif score >= 30:
        level = "difficult"
    else:
        level = "very difficult"
    print(f"words={W}")
    print(f"sentences={S}")
    print(f"syllables={Y}")
    print(f"score={score}")
    print(f"level={level}")

main()
