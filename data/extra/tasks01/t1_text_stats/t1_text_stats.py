import sys

data = sys.stdin.read()
lines = data.split("\n")
if lines and lines[-1] == "":
    lines.pop()

words = 0
chars = 0
blank = 0
longest = 0
longest_at = 0
for i, line in enumerate(lines, 1):
    n = len(line.split())
    words += n
    chars += len(line)
    if n == 0:
        blank += 1
    if len(line) > longest:
        longest = len(line)
        longest_at = i

print(f"lines: {len(lines)}")
print(f"words: {words}")
print(f"chars: {chars}")
print(f"blank: {blank}")
print(f"longest: {longest} (line {longest_at})")
