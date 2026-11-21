answers = [16, 132, 36, 110, 40, 60, 14, 88, 4, 24]
s = 2026
right = 0
missed = {}
for i, given in enumerate(answers):
    s = (s * 75 + 74) % 65537
    a = s % 11 + 2
    s = (s * 75 + 74) % 65537
    b = s % 12 + 1
    ok = given == a * b
    if ok:
        right += 1
    else:
        missed[a] = missed.get(a, 0) + 1
    mark = "right" if ok else f"wrong, it is {a * b}"
    print(f"{i + 1:>2}. {a} x {b} = {given}: {mark}")
print(f"score {right}/{len(answers)}")
print(f"practise the [{', '.join(str(t) for t in sorted(missed))}] times tables")
