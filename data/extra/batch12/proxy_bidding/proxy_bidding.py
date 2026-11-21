def money(cents):
    return f"{cents // 100}.{cents % 100:02}"

class Auction:
    def __init__(self, price, step):
        self.leader = ""; self.top = 0; self.price = price; self.step = step
    def bid(self, who, mx):
        if self.leader == "":
            self.leader = who
            self.top = mx
            return f"opens, {who} leads"
        if who == self.leader:
            self.top = max(self.top, mx)
            return f"{who} raises their own maximum"
        if mx > self.top:
            self.price = min(mx, self.top + self.step)
            self.leader = who
            self.top = mx
            return f"{who} takes the lead"
        self.price = min(self.top, mx + self.step)
        return f"{self.leader} keeps the lead"

a = Auction(1000, 100)
bids = [("kim", 2500), ("lou", 1800), ("max", 3000), ("kim", 3000), ("nia", 4250), ("lou", 4000), ("max", 4300)]
for who, mx in bids:
    note = a.bid(who, mx)
    print(f"{who} bids up to {money(mx):>6}: {note}, price {money(a.price)}")
print(f"sold to {a.leader} for {money(a.price)}")
