log = ["E12", "E07", "E12", "E31", "E07", "E12", "E44", "E31", "E12", "E07", "E02", "E31", "E31"]
meaning = {"E12": "paper jam", "E07": "card reader timeout", "E31": "network lost"}
counts = {}
for c in log: counts[c] = counts.get(c, 0) + 1
print(f"{len(log)} faults, {len(counts)} distinct codes")
top = sorted(counts, key=lambda k: -counts[k])[:3]
for i, c in enumerate(top):
    n = counts[c]
    print(f"{i + 1}. {c} x{n} ({n * 100 // len(log)}%): {meaning.get(c, 'unknown fault')}")
print(f"seen once: {', '.join(sorted(k for k in counts if counts[k] == 1))}")
