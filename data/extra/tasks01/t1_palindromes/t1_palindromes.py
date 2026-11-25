import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()


def is_palindrome(line):
    cs = [c for c in line.lower() if ("a" <= c <= "z") or ("0" <= c <= "9")]
    return bool(cs) and cs == cs[::-1]


found = 0
for i, line in enumerate(lines, 1):
    if is_palindrome(line):
        print(f"{i}: {line}")
        found += 1
print(f"palindromes: {found}")
print(f"total lines: {len(lines)}")
