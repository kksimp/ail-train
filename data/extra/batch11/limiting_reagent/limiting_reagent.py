reactions = [
    ("2 H2 + O2 -> 2 H2O", [("H2", 10.0, 2.016, 2.0), ("O2", 64.0, 32.0, 1.0)], "H2O", 18.015, 2.0),
    ("N2 + 3 H2 -> 2 NH3", [("N2", 28.0, 28.014, 1.0), ("H2", 4.0, 2.016, 3.0)], "NH3", 17.031, 2.0),
    ("4 Fe + 3 O2 -> 2 Fe2O3", [("Fe", 100.0, 55.845, 4.0), ("O2", 50.0, 32.0, 3.0)], "Fe2O3", 159.69, 2.0),
]
for title, inputs, product, pm, pc in reactions:
    best = inputs[0]
    for r in inputs:
        if r[1] / r[2] / r[3] < best[1] / best[2] / best[3]:
            best = r
    extent = best[1] / best[2] / best[3]
    made = extent * pc * pm
    print(f"{title}: {best[0]} runs out, makes {made:.2f} g {product}")
    for r in inputs:
        left = r[1] - extent * r[3] * r[2]
        if left > 0.0001:
            print(f"  {r[0]} left over: {left:.2f} g")
