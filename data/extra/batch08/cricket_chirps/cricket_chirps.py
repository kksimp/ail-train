for c in [10, 18, 25, 32, 40, 47]:
    n = c * 4; f = 50.0 + (n - 40) / 4.0; print(f"{c:>2} chirps in 15 s: {n:>3}/min, {f:.1f} F, {(f - 32.0) * 5.0 / 9.0:.1f} C")
for t in [60, 68, 77]: print(f"at {t} F expect {(t - 50) * 4 + 40} chirps a minute")
