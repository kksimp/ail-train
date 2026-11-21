p = 2147483647
g = 7
alice = 1234567
bob = 7654321
A = pow(g, alice, p)
B = pow(g, bob, p)
print(f"public: p = {p}, g = {g}")
print(f"Alice sends {A}, Bob sends {B}")
k1 = pow(B, alice, p)
k2 = pow(A, bob, p)
print(f"Alice's key {k1}, Bob's key {k2}, equal: {'true' if k1 == k2 else 'false'}")
sp, sg = 23, 5
sa = pow(sg, 6, sp)
sb = pow(sg, 15, sp)
print(f"toy exchange mod 23: A = {sa}, B = {sb}")
found = -1
for x in range(1, sp):
    if found < 0 and pow(sg, x, sp) == sa:
        found = x
print(f"eavesdropper tries exponents: 5^{found} = {sa}, so the key is {pow(sb, found, sp)}")
print(f"real key {pow(sb, 6, sp)}: a 23-element search is no protection")
