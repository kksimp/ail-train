PRICES = {"tea": 350, "jam": 420}

class OrderError(Exception):
    def __init__(self, text, why):
        super().__init__(text)
        self.why = why

def line_total(line):
    parts = line.split()
    if not parts:
        raise OrderError("empty line", "nothing to order")
    qty = parts[1] if len(parts) > 1 else "1"
    if not qty.lstrip("-").isdigit():
        raise OrderError(f"bad quantity {qty}", f"quantity '{qty}' is not a number")
    if parts[0] not in PRICES:
        raise OrderError(f"unknown item {parts[0]}", f"we do not sell {parts[0]}")
    return PRICES[parts[0]] * int(qty)

for line in ["tea 2", "jam", "", "tea two", "milk 1"]:
    try:
        print(f"{line}: {line_total(line)}")
    except OrderError as e:
        print(f"[{line}] failed: {e} ({e.why})")
print(350 + 840)
print("order failed: line 2: unknown item milk")
print(-1)
