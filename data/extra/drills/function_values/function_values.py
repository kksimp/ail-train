double = lambda x: x * 2
adder = lambda n: lambda x: x + n
print(double(double(5)))
add3 = adder(3)
print(add3(4))
print(add3(add3(0)))
print(adder(1)(double(10)))
v = 1
for f in [double, adder(10), lambda x: x - 1]:
    v = f(v)
print(v)
rules = [("even", lambda n: n % 2 == 0), ("positive", lambda n: n > 0), ("small", lambda n: n < 50)]
for n in [4, 7, -2, 80]:
    bad = [name for name, t in rules if not t(n)]
    print(f"{n}: " + ("ok" if not bad else "fails " + "+".join(bad)))
print(3)
