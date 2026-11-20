fs = [0, 1]
M = 2**63 - 1
while fs[-1] + fs[-2] <= M:
    fs.append(fs[-1] + fs[-2])
print(", ".join(map(str, fs[:10])))
sm = [x for x in fs if x < 1000]
print(f"below 1000: {len(sm)} numbers, sum {sum(sm)}")
print(f"even sum below 4 million: {sum(x for x in fs if x < 4000000 and x % 2 == 0)}")
print(f"{len(fs)} numbers fit in an int; the last is {fs[-1]}")
for i, x in enumerate(fs):
    if len(str(x)) >= 10:
        print(f"first with 10 digits: F({i}) = {x}"); break
