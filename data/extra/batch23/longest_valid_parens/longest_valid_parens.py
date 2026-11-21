def longest(s):
    stack = [-1]
    best = 0
    start = 0
    i = 0
    for c in s:
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                span = i - stack[-1]
                if span > best:
                    best = span
                    start = stack[-1] + 1
        i += 1
    return [best, start]

for s in ["(()", ")()())", "()(()", "(()())())(", ")(((((()())()()))()(()))(", "))((", "()()()"]:
    r = longest(s)
    stop = r[1] + r[0]
    piece = "-" if r[0] == 0 else s[r[1]:stop]
    print(f"{s:<26} longest {r[0]:>2} at {r[1]:>2}: {piece}")
