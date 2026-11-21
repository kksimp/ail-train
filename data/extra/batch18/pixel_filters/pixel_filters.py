row = [12, 60, 128, 200, 245, 90]
cl = lambda x: min(max(x, 0), 255)
br = lambda n: (lambda p: cl(p + n))
inv = lambda p: 255 - p
th = lambda c: (lambda p: 255 if p >= c else 0)
print(f"original   {row}")
print(f"brighter   {[br(40)(p) for p in row]}")
print(f"inverted   {[inv(p) for p in row]}")
pipe = lambda p: th(100)(inv(br(40)(p)))
print(f"pipeline   {[pipe(p) for p in row]}")
print(f"dark+flip  {[inv(br(-50)(p)) for p in row]}")
print(f"{sum(1 for p in row if pipe(p) == 255)} of {len(row)} pixels end up white")
