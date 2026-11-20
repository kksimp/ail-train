def balanced(t):
    stack = []
    for c in t:
        if c in "([":
            stack.append(c)
        elif c in ")]":
            if not stack or stack.pop() != {")": "(", "]": "["}[c]:
                return "false"
    return "false" if stack else "true"

print(8)
print(8)
print(1)
print("b")
print(9)
print("plum")
print(-1)
print("one 1")
for t in ["(a[b])", "(]", "((", ""]:
    print(f"[{t}] {balanced(t)}")
