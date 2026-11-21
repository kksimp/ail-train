class Lcg:
    def __init__(self, state):
        self.state = state

    def next(self, n):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state >> 8) % n

class Slot:
    def __init__(self, item, count, err):
        self.item = item
        self.count = count
        self.err = err

def offer(slots, item, k):
    for s in slots:
        if s.item == item:
            s.count += 1
            return
    if len(slots) < k:
        slots.append(Slot(item, 1, 0))
        return
    low = 0
    for i in range(1, len(slots)):
        if slots[i].count < slots[low].count:
            low = i
    floor = slots[low].count
    slots[low] = Slot(item, floor + 1, floor)

pages = ["home", "news", "shop", "help", "blog", "jobs", "about", "faq", "terms", "press"]
weights = [30, 18, 12, 8, 6, 5, 4, 3, 2, 2]
cumulative = []
run = 0
for w in weights:
    run += w
    cumulative.append(run)
rng = Lcg(31)
slots = []
exact = {}
for _ in range(5000):
    r = rng.next(run)
    i = 0
    while cumulative[i] <= r:
        i += 1
    offer(slots, pages[i], 5)
    exact[pages[i]] = exact.get(pages[i], 0) + 1
ranked = sorted(slots, key=lambda s: -s.count)
for s in ranked:
    lowest = s.count - s.err
    print(f"{s.item:<6} counted {s.count:>4} (true count between {lowest} and {s.count}; actual {exact[s.item]})")
print(f"5 counters followed a stream of 5000 views over {len(pages)} pages")
