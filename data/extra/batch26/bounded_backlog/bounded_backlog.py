class Backlog:
    def __init__(self, cap):
        self.cap = cap
        self.items = []
        self.refused = 0
    def offer(self, x):
        if len(self.items) >= self.cap:
            self.refused += 1
            return False
        self.items.append(x)
        return True
    def take(self):
        if not self.items:
            return None
        f = self.items[0]
        self.items = self.items[1:]
        return f

desk = Backlog(3)
for t in ["printer jam", "vpn down", "new laptop", "password reset", "broken chair"]:
    ok = desk.offer(t)
    print(f"{t}: {'queued' if ok else 'refused'}")
f = desk.take()
if f is not None:
    print(f"working on {f}")
again = desk.offer("broken chair")
print(f"retry broken chair: {'true' if again else 'false'}, waiting {len(desk.items)}, refused {desk.refused}")
hub = Backlog(2)
for code in [401, 402, 517, 610]:
    if not hub.offer(code):
        print(f"alarm {code} dropped")
print(f"alarms kept {hub.items}, dropped {hub.refused}")
