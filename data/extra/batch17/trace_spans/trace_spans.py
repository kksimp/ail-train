class Span:
    def __init__(self, id, parent, name, start, end):
        self.id, self.parent, self.name, self.start, self.end = id, parent, name, start, end

def show(spans, id, depth):
    s = spans[id]
    kids = [k for k in spans if k.parent == id]
    child_time = sum(k.end - k.start for k in kids)
    dur = s.end - s.start
    label = " " * (depth * 2) + s.name
    print(f"{label:<18} {s.start:>3}-{s.end:<3} {dur:>3} ms, self {dur - child_time:>3} ms")
    for k in kids:
        show(spans, k.id, depth + 1)

spans = [Span(0, -1, "GET /order", 0, 180), Span(1, 0, "auth", 5, 25), Span(2, 0, "load order", 30, 110), Span(3, 2, "db query", 35, 90), Span(4, 2, "cache set", 92, 105), Span(5, 0, "render", 112, 170), Span(6, 5, "template", 115, 160)]
show(spans, 0, 0)
path = []
cur = 0
while True:
    path.append(spans[cur].name)
    kids = [k for k in spans if k.parent == cur]
    if len(kids) == 0:
        break
    cur = sorted(kids, key=lambda k: -k.end)[0].id
print(f"critical path: {' > '.join(path)}")
