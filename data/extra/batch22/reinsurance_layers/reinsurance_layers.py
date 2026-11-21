def layer(claim, attach, size):
    return min(max(claim - attach, 0), size)

claims = [40, 130, 260, 450, 900, 75, 320]
kept = first = second = 0
for c in claims:
    l1 = layer(c, 100, 200)
    l2 = layer(c, 300, 500)
    own = c - l1 - l2
    kept += own
    first += l1
    second += l2
    print(f"claim {c:>3}: insurer {own:>3}, layer 1 {l1:>3}, layer 2 {l2:>3}")
total = kept + first + second
print(f"totals: insurer {kept}, layer 1 {first}, layer 2 {second} of {total}")
print(f"{sum(1 for c in claims if c > 300)} claims reached the second layer")
