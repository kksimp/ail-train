from itertools import takewhile, dropwhile

def page(xs, number, size):
    return xs[(number - 1) * size:][:size]

def header(lines):
    return list(takewhile(lambda l: l != "", lines))

def body(lines):
    return list(dropwhile(lambda l: l != "", lines))[1:]

entries = ["boot", "mount", "net up", "login ann", "login bob", "sync", "halt"]
print(", ".join(page(entries, 1, 3)))
print(", ".join(page(entries, 3, 3)))
print(len(page(entries, 4, 3)))
message = ["From: ann", "To: bob", "", "hello", "", "bye"]
print(" / ".join(header(message)))
print(" / ".join(body(message)))
print(next((e for e in entries if e.startswith("login")), "none"))
print(next((e for e in entries if e.startswith("panic")), "none"))
nums = [2, 4, 6, 7, 8, 10]
print(" ".join(map(str, takewhile(lambda n: n % 2 == 0, nums))))
print(" ".join(map(str, dropwhile(lambda n: n % 2 == 0, nums))))
