def run(i, evs):
    s = ("placed",); refused = 0
    for e in evs:
        t = None
        if s[0] == "placed":
            if e[0] == "pay": t = ("paid", e[1])
            elif e[0] == "cancel": t = ("cancelled", e[1])
        elif s[0] == "paid":
            if e[0] == "ship": t = ("shipped", e[1])
            elif e[0] == "cancel": t = ("cancelled", e[1] + ", refunded")
        elif s[0] == "shipped":
            if e[0] == "deliver": t = ("delivered", e[1])
        if t: s = t
        else: refused += 1
    k = s[0]
    txt = {"placed": lambda: "placed", "paid": lambda: f"paid {s[1]} cents", "shipped": lambda: f"shipped by {s[1]}", "delivered": lambda: f"delivered on day {s[1]}", "cancelled": lambda: f"cancelled ({s[1]})"}[k]()
    print(f"order {i}: {txt}, {refused} refused")
run(1, [("pay", 2599), ("ship", "DHL"), ("deliver", 4)])
run(2, [("ship", "UPS"), ("pay", 1250), ("cancel", "changed mind")])
run(3, [("pay", 800), ("ship", "post"), ("cancel", "late"), ("deliver", 9)])
run(4, [("cancel", "duplicate"), ("pay", 500)])
