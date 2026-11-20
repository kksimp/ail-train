print(" ".join(str(i * i) for i in range(9) if i % 2 == 0))
prices = {"tea": 350, "jam": 420, "oats": 180}
print(",".join(k for k, v in prices.items() if v < 400))
print({v: k for k, v in prices.items()}[420])
print(prices["oats"] * 2)
lengths = {w: len(w) for w in ["a", "bcd", "ef"]}
print(" ".join(f"{w}{lengths[w]}" for w in sorted(lengths)))
print("".join(sorted({n[:1] for n in ["ann", "bob", "alice", "cy"]})))
print(" ".join(f"{r}{c}" for r in (1, 2) for c in "abc"))
print(",".join(str(i) for i, w in enumerate(["x", "skip", "y"]) if w != "skip"))
print(sum(prices.values()))
print(len({n % 3 for n in range(10)}))
