machines = [("press", 480, 47, 9, 2400, 2316), ("lathe", 480, 88, 30, 700, 672), ("mill", 450, 30, 20, 1150, 1081)]
labels = ["availability", "performance", "quality"]
for name, planned, down, cycle, made, good in machines:
    run = float(planned - down)
    a = run / float(planned)
    p = float(cycle * made) / (run * 60.0)
    q = float(good) / float(made)
    f = [a, p, q]
    oee = a * p * q * 100.0
    weak = 0
    for i in range(1, 3):
        if f[i] < f[weak]:
            weak = i
    print(f"{name:<5} A {a * 100.0:.1f}%, P {p * 100.0:.1f}%, Q {q * 100.0:.1f}%: OEE {oee:.1f}%, weakest {labels[weak]}")
