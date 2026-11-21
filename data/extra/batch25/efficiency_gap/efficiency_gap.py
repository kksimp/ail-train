districts = [(62000, 38000), (35000, 65000), (36000, 64000), (34000, 66000), (71000, 29000), (38000, 62000), (37000, 63000)]
waste_a = waste_b = seats_a = votes_a = total = 0
for i, (a, b) in enumerate(districts):
    need = (a + b) // 2 + 1
    wa = a - need if a > b else a
    wb = b - need if b > a else b
    if a > b:
        seats_a += 1
    waste_a += wa
    waste_b += wb
    votes_a += a
    total += a + b
    winner = "A" if a > b else "B"
    print(f"district {i + 1}: A {a:>6,} B {b:>6,} won by {winner}, wasted A {wa:>6,} B {wb:>6,}")
gap = (waste_a - waste_b) / total * 100.0
share = votes_a / total * 100.0
favours = "B" if gap > 0.0 else "A"
print(f"party A: {share:.1f}% of votes, {seats_a} of {len(districts)} seats")
print(f"efficiency gap {abs(gap):.1f}% in favour of {favours}")
