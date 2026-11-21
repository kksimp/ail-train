def scan(s):
    depth = score = junk = 0; in_junk = skip = False
    for c in s:
        if skip: skip = False
        elif c == '!': skip = True
        elif in_junk:
            if c == '>': in_junk = False
            else: junk += 1
        elif c == '<': in_junk = True
        elif c == '(':
            depth += 1; score += depth
        elif c == ')': depth -= 1
    return [score, junk]

streams = ["()", "((()))", "(<a>,<b>)", "((<!>),<x>),(<q!!>))", "(<(()>,((!))<zz>))", "(((<ab!c>),()),(<>))"]
total = [0, 0]
for s in streams:
    r = scan(s)
    print(f"{s:<24} score {r[0]:>2}, garbage {r[1]}")
    total[0] += r[0]; total[1] += r[1]
print(f"part 1: total score {total[0]}")
print(f"part 2: total garbage {total[1]}")
