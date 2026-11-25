import sys

lines = sys.stdin.read().splitlines()
if not lines:
    print("breaches: 0 of 0")
    sys.exit(0)
now = int(lines[0].strip())
LIM = {"P1": 60, "P2": 240}
total = hits = 0
for line in lines[1:]:
    line = line.strip()
    if not line:
        continue
    tid, pri, opened, res = line.split(",")
    total += 1
    end = now if res == "-" else int(res)
    over = end - int(opened) - LIM.get(pri, 1440)
    if over > 0:
        hits += 1
        print(f"{tid} over by {over}")
print(f"breaches: {hits} of {total}")
