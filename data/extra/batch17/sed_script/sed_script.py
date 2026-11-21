class Cmd:
    def __init__(self, lo, hi, pattern, op, old, new, glob):
        self.lo, self.hi, self.pattern, self.op, self.old, self.new, self.glob = lo, hi, pattern, op, old, new, glob

def parse(cmd):
    rest = cmd
    lo = 0
    hi = 0
    pattern = ""
    if rest.startswith("/"):
        close = rest[1:].find("/")
        pattern = rest[1:close + 1]
        rest = rest[close + 2:]
    else:
        digits = 0
        while digits < len(rest) and (rest[digits].isdigit() or rest[digits] == ','):
            digits += 1
        if digits > 0:
            nums = rest[:digits].split(",")
            lo = int(nums[0])
            hi = int(nums[1]) if len(nums) > 1 else lo
            rest = rest[digits:]
    if rest == "d":
        return Cmd(lo, hi, pattern, "d", "", "", False)
    parts = rest.split("/")
    return Cmd(lo, hi, pattern, "s", parts[1], parts[2], parts[3] == "g")

def applies(c, n, line):
    if c.pattern != "":
        return c.pattern in line
    if c.lo > 0:
        return n >= c.lo and n <= c.hi
    return True

script = ["s/colour/color/g", "2d", "/TODO/s/TODO/DONE/", "3,4s/ /_/g", "s/a/A/"]
cmds = [parse(s) for s in script]
text = ["the colour of a colour wheel", "line to drop", "TODO: TODO list for today", "a b c", "banana bread"]
for i, line in enumerate(text):
    cur = line
    deleted = False
    for c in cmds:
        if not applies(c, i + 1, cur):
            continue
        if c.op == "d":
            deleted = True
            break
        if c.glob:
            cur = cur.replace(c.old, c.new)
        else:
            at = cur.find(c.old)
            if at >= 0:
                cur = cur[:at] + c.new + cur[at + len(c.old):]
    if not deleted:
        print(cur)
print(f"({len(script)} commands, {len(text)} input lines)")
