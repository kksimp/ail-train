def title_case(t):
    return " ".join(w[:1].upper() + w[1:].lower() for w in t.split())

def boxed(t):
    ls = t.split("\n")
    w = max(len(l) for l in ls)
    edge = "+" + "-" * (w + 2) + "+"
    return "\n".join([edge] + [f"| {l.ljust(w)} |" for l in ls] + [edge])

print(title_case("the QUICK  brown fOX"))
print(boxed("hello\nto\neveryone"))
print("url -> http://x/?a=1&b=2")
print("flag -> []")
print("a+b+c")
print("20/11/2026")
print(";".join(f"{i},{i * i}" for i in range(1, 4)))
print("ababab")
print('{"id": 7}')
print(2)
print(3)
print(4)
