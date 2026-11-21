heap = [("grass clippings", 30.0, 40.0, 2.4), ("kitchen scraps", 20.0, 35.0, 2.0), ("coffee grounds", 6.0, 40.0, 2.0), ("dry leaves", 10.0, 48.0, 0.8)]

def ratio(heap):
    c = 0.0
    n = 0.0
    for m in heap:
        c += m[1] * m[2]
        n += m[1] * m[3]
    return c / n

for m in heap:
    print(f"{m[0]:<16} {m[1]:>5.1f} kg  C:N {m[2] / m[3]:>5.1f}")
print(f"mix C:N {ratio(heap):.1f}")
buckets = 0
while ratio(heap) < 25.0:
    heap.append(("straw", 4.0, 46.0, 0.6))
    buckets += 1
    print(f"add straw bucket {buckets}: C:N {ratio(heap):.1f}")
total = 0.0
for m in heap:
    total += m[1]
print(f"{buckets} buckets of straw, {total:.1f} kg in the heap")
