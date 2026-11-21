def bit_parity(n):
    return bin(n).count("1") % 2

def power_sum(xs, k):
    return sum(x ** k for x in xs)

bits = [bit_parity(n) for n in range(32)]
print(f"t(0..31) = {''.join(str(b) for b in bits)}")
doubled = [0]
while len(doubled) < 32:
    doubled += [1 - b for b in doubled]
print(f"by doubling with complement, same: {str(doubled == bits).lower()}")
order = ["A" if b == 0 else "B" for b in bits[:8]]
print(f"picking order: {' '.join(order)}")
group_a = [n for n in range(16) if bit_parity(n) == 0]
group_b = [n for n in range(16) if bit_parity(n) == 1]
print(f"A = {group_a}")
print(f"B = {group_b}")
for k in range(5):
    print(f"sum of k = {k} powers: {power_sum(group_a, k)} vs {power_sum(group_b, k)}")
