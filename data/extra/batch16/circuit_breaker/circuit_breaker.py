def label(s):
    if s[0] == "closed":
        return "closed"
    if s[0] == "open":
        return f"open, retry at {s[1]}"
    return "half-open"

class Breaker:
    def __init__(self):
        self.state = ("closed",)
        self.fails = 0
    def call(self, t, ok):
        if self.state[0] == "open":
            if t < self.state[1]:
                return "rejected without calling"
            self.state = ("half",)
        if self.state[0] == "half":
            if ok:
                self.state = ("closed",)
                self.fails = 0
                return "trial succeeded"
            self.state = ("open", t + 30)
            return "trial failed"
        if ok:
            self.fails = 0
            return "ok"
        self.fails += 1
        if self.fails >= 3:
            self.state = ("open", t + 30)
            return "failed, tripping"
        return f"failed ({self.fails} in a row)"

calls = [(0, True), (5, False), (8, False), (9, False), (12, True), (20, True), (42, False), (45, True), (80, True), (85, False), (86, False), (87, False), (130, True), (131, True)]
b = Breaker()
for t, ok in calls:
    what = b.call(t, ok)
    print(f"t={t:>3}: {what:<25} now {label(b.state)}")
