import sys

def to_int(s):
    try:
        if s.lstrip("-").isdigit() and s.count("-") <= 1 and (s[0] != "-" or len(s) > 1) and s.isascii():
            return int(s)
    except ValueError:
        pass
    return None

heap = []

def push(x):
    heap.append(x)
    i = len(heap) - 1
    while i > 0:
        p = (i - 1) // 2
        if heap[p] <= heap[i]:
            break
        heap[p], heap[i] = heap[i], heap[p]
        i = p

def pop():
    if not heap:
        return None
    top = heap[0]
    last = heap.pop()
    if heap:
        heap[0] = last
        n = len(heap)
        i = 0
        while True:
            l = 2 * i + 1
            r = l + 1
            m = i
            if l < n and heap[l] < heap[m]:
                m = l
            if r < n and heap[r] < heap[m]:
                m = r
            if m == i:
                break
            heap[m], heap[i] = heap[i], heap[m]
            i = m
    return top

for line in sys.stdin.read().splitlines():
    w = line.split()
    if not w:
        continue
    c = w[0]
    if c == "push" and len(w) == 2 and to_int(w[1]) is not None:
        push(to_int(w[1]))
        print("ok")
    elif c == "pop" and len(w) == 1:
        v = pop()
        print("empty" if v is None else v)
    elif c == "peek" and len(w) == 1:
        print(heap[0] if heap else "empty")
    elif c == "size" and len(w) == 1:
        print(len(heap))
    elif c == "drain" and len(w) == 1:
        out = []
        while heap:
            out.append(str(pop()))
        print(" ".join(out) if out else "empty")
    else:
        print("error")
