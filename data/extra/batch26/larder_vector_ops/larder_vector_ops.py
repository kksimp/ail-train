def s(l): return f"{l[0]} g flour, {l[1]} eggs, {l[2]} ml milk"
def add(a, b): return tuple(x + y for x, y in zip(a, b))
def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def report(label, left):
    out = []
    if left[0] < 0: out.append(f"flour {-left[0]} g")
    if left[1] < 0: out.append(f"eggs {-left[1]}")
    if left[2] < 0: out.append(f"milk {-left[2]} ml")
    if not out:
        print(f"{label}: nothing to buy, left {s(left)}")
    else:
        print(f"{label}: buy {', '.join(out)}")
have = (500, 5, 800); p = (200, 2, 300); c = (250, 4, 100)
print(f"pancakes need {s(p)}")
print(f"cake needs {s(c)}")
both = add(p, c)
print(f"together {s(both)}")
report("both", sub(have, both))
report("double pancakes", sub(have, add(p, p)))
report("cake twice", sub(sub(have, c), c))
