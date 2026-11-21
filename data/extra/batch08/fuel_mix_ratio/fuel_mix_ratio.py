for r in [25, 40, 50]: print(f"{r}:1 -> " + ", ".join(f"{l:.1f} l: {l * 1000.0 / r:.0f} ml" for l in [1.0, 2.0, 5.0, 10.0]))
print(f"5.0 l with 200 ml oil is {5.0 * 1000.0 / 200.0:.0f}:1; add {200.0 * 50.0 / 1000.0 - 5.0:.1f} l petrol to reach {50.0:.0f}:1")
