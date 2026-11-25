import sys

def check(line):
    parts = line.split(" ")
    if len(parts) < 2:
        return "malformed"
    puz = parts[0]
    if puz.count("+") != 1 or puz.count("=") != 1:
        return "malformed"
    left, c = puz.split("=")
    if "+" not in left:
        return "malformed"
    a, b = left.split("+")
    words = [a, b, c]
    for w in words:
        if w == "" or not all("A" <= ch <= "Z" for ch in w):
            return "malformed"
    asg = {}
    dups = None
    for item in parts[1:]:
        if len(item) != 3 or item[1] != "=" or not ("A" <= item[0] <= "Z") or item[2] not in "0123456789":
            return "malformed"
        if item[0] in asg and dups is None:
            dups = item[0]
        asg[item[0]] = int(item[2])
    if dups is not None:
        return "conflict " + dups
    for w in words:
        for ch in w:
            if ch not in asg:
                return "missing " + ch
    seen = {}
    for letter, d in asg.items():
        seen.setdefault(d, []).append(letter)
    shared = sorted(d for d, ls in seen.items() if len(ls) > 1)
    if shared:
        return "duplicate digit %d" % shared[0]
    for w in words:
        if len(w) > 1 and asg[w[0]] == 0:
            return "leading zero " + w
    nums = [int("".join(str(asg[ch]) for ch in w)) for w in words]
    if nums[0] + nums[1] == nums[2]:
        return "ok"
    return "wrong %d + %d != %d" % tuple(nums)

for raw in sys.stdin.read().split("\n"):
    line = raw.strip()
    if line == "":
        continue
    print(check(line))
