def show(s):
    return ",".join(sorted(s)) if s else "-"

def repeats(xs):
    seen, out = set(), []
    for x in xs:
        if x in seen:
            out.append(x)
        seen.add(x)
    return out

def b(v):
    return "true" if v else "false"

ann, bob, need = {"ail", "sql", "css"}, {"sql", "go"}, {"ail", "sql"}
print(show(ann | bob))
print(show(ann & bob))
print(show(ann - bob))
print(show(bob - ann))
print(b(need <= ann))
print(b(need <= bob))
print(show(need - bob))
print(show(set()))
print(" ".join(repeats(["a", "b", "a", "c", "b", "a"])))
print(b("css" in ann and "css" not in bob))
print(b(len(ann) + len(bob) - len(ann & bob) == len(ann | bob)))
print("".join(sorted(set("mississippi"))))
