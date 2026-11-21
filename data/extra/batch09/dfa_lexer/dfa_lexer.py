def class_of(c):
    if c.isalpha() or c == '_':
        return 0
    if c.isdigit():
        return 1
    if c == '.':
        return 2
    if c in "+-*/<>=!":
        return 3
    return 4

T = [[1, 2, -1, 5, -1], [1, 1, -1, -1, -1], [-1, 2, 3, -1, -1], [-1, 4, -1, -1, -1], [-1, 4, -1, -1, -1], [-1, -1, -1, 6, -1], [-1, -1, -1, -1, -1]]

def kind(state):
    return {1: "identifier", 2: "integer", 4: "decimal", 5: "operator", 6: "operator"}.get(state, "rejected")

for word in ["count", "x1", "_tmp", "42", "3.14", "3.", ".5", "1a", "+", "<=", "<=>", "a-b"]:
    state = 0
    path = ["0"]
    for c in word:
        state = T[state][class_of(c)]
        path.append(f"{state}")
        if state < 0:
            break
    trail = ">".join(path)
    print(f"{word:<6} {trail:<14} {kind(state)}")
