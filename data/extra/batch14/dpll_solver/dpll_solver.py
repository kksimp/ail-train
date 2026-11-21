def simplify(clauses, lit):
    return [[x for x in c if x != -lit] for c in clauses if lit not in c]
def dpll(clauses, assign, steps):
    steps[0] += 1
    if not clauses:
        return True
    if any(len(c) == 0 for c in clauses):
        return False
    for c in clauses:
        if len(c) == 1:
            lit = c[0]
            assign[abs(lit)] = lit > 0
            return dpll(simplify(clauses, lit), assign, steps)
    v = abs(clauses[0][0])
    for lit in [v, -v]:
        trial = dict(assign)
        if dpll(simplify(clauses, lit), trial, steps):
            trial[v] = lit > 0
            assign.clear()
            assign.update(trial)
            return True
    return False
def solve(name, clauses, n):
    assign = {}
    steps = [0]
    if dpll(clauses, assign, steps):
        shown = " ".join(f"x{v}={'true' if assign.get(v, True) else 'false'}" for v in range(1, n + 1))
        print(f"{name}: satisfiable after {steps[0]} calls: {shown}")
    else:
        print(f"{name}: unsatisfiable after {steps[0]} calls")
solve("small", [[1, 2], [-1, 3], [-2, -3], [2, 3]], 3)
solve("chain", [[1], [-1, 2], [-2, 3], [-3, 4], [-4, -5], [5, 6]], 6)
solve("3 pigeons, 2 holes", [[1, 2], [3, 4], [5, 6], [-1, -3], [-1, -5], [-3, -5], [-2, -4], [-2, -6], [-4, -6]], 6)
solve("contradiction", [[1, 2], [1, -2], [-1, 2], [-1, -2]], 2)
