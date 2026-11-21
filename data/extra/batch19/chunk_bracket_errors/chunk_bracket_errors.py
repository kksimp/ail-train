CL = {'(': ')', '[': ']', '<': '>'}
def check(line):
    st = []
    for c in line:
        if c in "([<":
            st.append(c)
        else:
            top = st.pop() if st else ' '
            if CL.get(top, '>') != c:
                return [{')': 2, ']': 7}.get(c, 19), 0]
    fix = 0
    while st:
        o = st.pop()
        fix = fix * 4 + {'(': 1, '[': 2}.get(o, 3)
    return [0, fix]

lines = ["([<>]<(", "[(<>)]]", "<<[]>(", "(([[<>]]))", "([)]", "[<(<>)", "<(>", "(([<"]
errors = 0; fixes = []
for l in lines:
    r = check(l)
    if r[0] > 0:
        print(f"{l:<12} corrupted, score {r[0]}"); errors += r[0]
    elif r[1] > 0:
        print(f"{l:<12} incomplete, completion score {r[1]}"); fixes.append(r[1])
    else:
        print(f"{l:<12} complete")
print(f"part 1: error score {errors}")
s = sorted(fixes)
print(f"part 2: median completion score {s[len(s) // 2]}")
