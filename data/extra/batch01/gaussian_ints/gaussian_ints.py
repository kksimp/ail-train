def show(z): return f"{int(z.real)}{'-' if z.imag < 0 else '+'}{abs(int(z.imag))}i"
a, b = complex(3, 2), complex(1, -4)
n = lambda z: int(z.real) ** 2 + int(z.imag) ** 2
print(f"a = {show(a)}, b = {show(b)}")
print(f"a + b = {show(a + b)}")
print(f"a - b = {show(a - b)}")
print(f"a * b = {show(a * b)}")
print(f"-a = {show(-a)}")
print(f"N(a) * N(b) = {n(a) * n(b)} = N(a*b) = {n(a * b)}")
p, ps = complex(1, 0), []
for _ in range(5):
    ps.append(show(p)); p = p * 1j
print("powers of i: " + ", ".join(ps))
