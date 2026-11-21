def fn_(L, f): return L - L / 2.0 ** (f / 12.0)
for f in [1, 2, 3, 5, 7, 12, 17, 19, 24]: print(f"fret {f:>2}: {fn_(648.0, f):>6.1f} mm")
print(f"gap nut to fret 1 {fn_(648.0, 1):.1f} mm, fret 11 to 12 {fn_(648.0, 12) - fn_(648.0, 11):.1f} mm")
