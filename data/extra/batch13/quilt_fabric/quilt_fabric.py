patches = [("navy", 16, 90), ("cream", 10, 120), ("rust", 24, 20), ("sage", 7, 350)]

def inches(q):
    whole = q // 4
    return [f"{whole}", f"{whole} 1/4", f"{whole} 1/2", f"{whole} 3/4"][q % 4]

width_q = 42 * 4
total_eighths = 0
for fabric, finished_q, count in patches:
    cut = finished_q + 2
    per_strip = width_q // cut
    strips = (count + per_strip - 1) // per_strip
    length_q = strips * cut
    eighths = (length_q + 17) // 18
    total_eighths += eighths
    print(f"{fabric:<6} cut {inches(cut):>6} in, {per_strip:>2} per strip, {strips:>2} strips, {inches(length_q):>8} in = {eighths}/8 yd")
print(f"buy {total_eighths // 8} yd and {total_eighths % 8}/8 in all")
