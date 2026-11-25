import sys


def valid_name(s):
    return s != "" and all(("a" <= c <= "z") or ("0" <= c <= "9") for c in s)


def check(line):
    stack = []
    count = 0
    i = 0
    n = len(line)
    while i < n:
        if line[i] != "<":
            i += 1
            continue
        j = i + 1
        while j < n and line[j] != ">":
            j += 1
        if j >= n:
            return "unterminated tag"
        tag = line[i + 1:j]
        count += 1
        i = j + 1
        if tag.startswith("/"):
            name = tag[1:]
            if not valid_name(name):
                return f"bad tag {count}"
            if not stack:
                return f"unexpected close {name} at tag {count}"
            top = stack.pop()
            if top != name:
                return f"mismatch at tag {count}: expected {top} got {name}"
        elif tag.endswith("/"):
            if not valid_name(tag[:-1]):
                return f"bad tag {count}"
        else:
            if not valid_name(tag):
                return f"bad tag {count}"
            stack.append(tag)
    if stack:
        return f"unclosed {stack[-1]}"
    return "OK"


def main():
    for n, line in enumerate(sys.stdin.read().splitlines()):
        if line.strip() == "":
            continue
        print(f"{n + 1}: {check(line)}")


main()
