taken = set(); sf = 0; pf = 0
reqs = [("A3", 4500, "4111-2222"), ("A3", 4500, "4111-3333"), ("E1", 3000, "4111-4444"), ("B7", 18000, "4111-5555"), ("C2", 6000, "5500-0000"), ("D8", 4500, "4111-6666")]
for seat, cents, card in reqs:
    row = seat[0]
    try:
        num = int(seat[1:])
    except ValueError:
        num = 0
    err = None; kind = None
    if row < "A" or row > "D" or num < 1 or num > 8:
        err = f"no seat {seat}"; kind = "s"
    elif seat in taken:
        err = f"seat {seat} is taken"; kind = "s"
    elif card.endswith("0000"):
        err = "card declined"; kind = "p"
    elif cents > 15000:
        err = "over the 150 limit"; kind = "p"
    if err:
        if kind == "s": sf += 1
        else: pf += 1
        print(f"{seat}: {err}")
        continue
    taken.add(seat)
    print(f"{seat}: booked ({len(taken)} sold)")
print(f"seat problems {sf}, payment problems {pf}")
