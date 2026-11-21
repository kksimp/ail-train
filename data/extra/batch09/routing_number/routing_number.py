def weighted(digits):
    weights = [3, 7, 1, 3, 7, 1, 3, 7, 1]
    return sum(d * weights[i] for i, d in enumerate(digits))

def digits_of(s):
    return [int(c) for c in s]

for num in ["011000015", "123456780", "123456789", "091000019", "026009593"]:
    total = weighted(digits_of(num))
    verdict = "valid" if total % 10 == 0 else "invalid"
    print(f"{num}: weighted sum {total:>3} -> {verdict}")
for prefix in ["12345678", "07200080", "11100002"]:
    ds = digits_of(prefix) + [0]
    partial = weighted(ds)
    check = (10 - partial % 10) % 10
    print(f"{prefix} needs check digit {check}")
