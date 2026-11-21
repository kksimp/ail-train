def field(p, f):
    return {"name": p[0], "age": str(p[1]), "city": p[2], "role": p[3]}.get(f, "")

def test(p, cond):
    t = cond.strip().split(" ")
    have = field(p, t[0])
    want = t[2]
    op = t[1]
    if op == "=" or op == "!=":
        return (have == want) == (op == "=")
    a = int(have)
    b = int(want)
    return {"<": a < b, ">": a > b, "<=": a <= b, ">=": a >= b}.get(op, False)

def matches(p, query):
    return any(all(test(p, c) for c in part.split(" and ")) for part in query.split(" or "))

staff = [("Ann", 34, "Oslo", "dev"), ("Bo", 23, "Bergen", "dev"), ("Cy", 45, "Oslo", "ops"), ("Di", 29, "Tromso", "design"), ("Ed", 52, "Bergen", "ops")]
queries = ["city = Oslo", "age > 30 and role = ops", "role = design or age < 25", "city != Oslo and age >= 29", "age > 40 and city = Oslo or name = Bo"]
for q in queries:
    names = ", ".join(p[0] for p in staff if matches(p, q))
    shown = "nobody" if names == "" else names
    print(f"{q:<38} -> {shown}")
