import sys

lines = sys.stdin.read().splitlines()

def to_int(s):
    t = s[1:] if s.startswith("-") else s
    if t.isascii() and t.isdigit():
        return int(s)
    return None

n = to_int(lines[0].strip()) if lines else None
if n is None or n < 1 or n > 1000:
    print("bad header")
    sys.exit(0)
parent = list(range(n))
size = [1] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def elem(s):
    v = to_int(s)
    if v is None or v < 0 or v >= n:
        return None
    return v

sets = n
for line in lines[1:]:
    w = line.split()
    if not w:
        continue
    c = w[0]
    if c in ("union", "find") and len(w) == 3 and elem(w[1]) is not None and elem(w[2]) is not None:
        a, b = find(elem(w[1])), find(elem(w[2]))
        if c == "union":
            if a == b:
                print("same")
            else:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
                sets -= 1
                print("merged")
        else:
            print("yes" if a == b else "no")
    elif c == "size" and len(w) == 2 and elem(w[1]) is not None:
        print(size[find(elem(w[1]))])
    elif c == "count" and len(w) == 1:
        print(sets)
    elif c == "largest" and len(w) == 1:
        print(max(size[i] for i in range(n) if find(i) == i))
    else:
        print("error")
