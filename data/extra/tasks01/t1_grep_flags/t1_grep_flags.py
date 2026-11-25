import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()

head = lines[0] if lines else ""
sp = head.find(" ")
if sp < 0 or sp + 1 >= len(head):
    print("bad pattern")
    sys.exit(0)
flags = head[:sp]
pattern = head[sp + 1:]
if flags != "-" and (flags == "" or any(c not in "ivnc" for c in flags)):
    print("bad flags")
    sys.exit(0)

nocase = "i" in flags and flags != "-"
invert = "v" in flags
numbered = "n" in flags
count_only = "c" in flags

count = 0
for i, line in enumerate(lines[1:], 1):
    if nocase:
        hit = pattern.lower() in line.lower()
    else:
        hit = pattern in line
    if hit == invert:
        continue
    count += 1
    if count_only:
        continue
    print(f"{i}:{line}" if numbered else line)
if count_only:
    print(count)
