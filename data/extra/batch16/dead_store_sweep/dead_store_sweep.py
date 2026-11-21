class Stmt:
    def __init__(s, dst, args):
        s.dst, s.args = dst, args

def render(s):
    return f"{s.dst} = {' + '.join(s.args)}"

def sweep(code, results):
    live = {r: True for r in results}
    keep = [False] * len(code)
    i = len(code) - 1
    while i >= 0:
        s = code[i]
        if live.get(s.dst, False):
            keep[i] = True
            live[s.dst] = False
            for a in s.args:
                live[a] = True
        i -= 1
    return keep

code = [Stmt("a", ["x", "y"]), Stmt("b", ["a", "a"]), Stmt("t", ["x", "x"]), Stmt("a", ["b", "z"]), Stmt("u", ["t", "y"]), Stmt("c", ["a", "b"]), Stmt("t", ["c", "y"])]
keep = sweep(code, ["c"])
kept = 0
for i in range(len(code)):
    mark = "keep" if keep[i] else "drop"
    print(f"{mark}  {render(code[i])}")
    if keep[i]:
        kept += 1
print(f"{kept} of {len(code)} statements kept")
