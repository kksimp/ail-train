ppl = [("Olu", "0161 496 0012", "olu@mail.test", None), ("Mei", None, "mei@mail.test", "4 Elm Row"), ("Raf", None, None, "9 Quay St"), ("Tia", None, None, None)]
for n, p, e, a in ppl:
    r = f"call {p}" if p else (f"email {e}" if e else (f"write to {a}" if a else "no way to reach"))
    print(f"{n}: {r}")
print(f"{sum(1 for x in ppl if x[1] is None)} of {len(ppl)} have no phone")
print("emails: [" + ", ".join(f'"{x[2] or "-"}"' for x in ppl) + "]")
