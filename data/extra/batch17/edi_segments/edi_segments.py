def cents(s):
    parts = s.split(".")
    whole = int(parts[0])
    frac = parts[1].ljust(2, '0')[:2] if len(parts) > 1 else "00"
    return whole * 100 + int(frac)

msg = "ST*850*0001~BEG*00*SA*PO-4471**20250301~PO1*1*10*EA*2.5**VP*W-100~PO1*2*3*EA*12.00**VP*W-200~PO1*3*1*BX*49.99**VP*W-310~CTT*3~SE*7*0001~"
segs = [s for s in msg.split("~") if s != ""]
lines = 0
total = 0
declared_lines = 0
declared_segs = 0
for s in segs:
    e = s.split("*")
    if e[0] == "BEG":
        print(f"order {e[3]} dated {e[5]}")
    elif e[0] == "PO1":
        qty = int(e[2])
        each = cents(e[4])
        lines += 1
        total += qty * each
        print(f"  line {e[1]}: {qty} {e[3]} of {e[7]} at {each // 100}.{each % 100:02} = {qty * each // 100}.{qty * each % 100:02}")
    elif e[0] == "CTT":
        declared_lines = int(e[1])
    elif e[0] == "SE":
        declared_segs = int(e[1])
print(f"total {total // 100}.{total % 100:02}")
lines_ok = "ok" if lines == declared_lines else "MISMATCH"
segs_ok = "ok" if len(segs) == declared_segs else "MISMATCH"
print(f"line count {lines}/{declared_lines} {lines_ok}, segment count {len(segs)}/{declared_segs} {segs_ok}")
