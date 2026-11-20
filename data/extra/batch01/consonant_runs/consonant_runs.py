def run(w):
    best, cur = "", ""
    for c in w:
        if c.isalpha() and c.lower() not in "aeiou":
            cur += c
            if len(cur) > len(best):
                best = cur
        else:
            cur = ""
    return best
words = ["strengths", "rhythm", "banana", "twelfths", "Schwartz", "aeiou", "crypts"]
for w in sorted(words, key=lambda w: (-len(run(w)), w)):
    r = run(w)
    print(f"{w:<10}{len(r)} {r if r else '(none)'}")
print(f"consonants in all: {sum(1 for w in words for c in w if c.lower() not in 'aeiou')}")
