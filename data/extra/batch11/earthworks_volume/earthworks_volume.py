def volumes(areas, spacing):
    out = []
    for i in range(1, len(areas)):
        out.append((areas[i - 1] + areas[i]) / 2.0 * spacing)
    return out
stations = [0, 20, 40, 60, 80, 100]
cut = [0.0, 12.5, 18.0, 6.0, 0.0, 0.0]
fill = [4.0, 0.0, 0.0, 3.5, 14.0, 9.0]
vc = volumes(cut, 20.0)
vf = volumes(fill, 20.0)
for i in range(len(vc)):
    print(f"station {stations[i]:>3} to {stations[i + 1]:>3}: cut {vc[i]:>5.1f} m3, fill {vf[i]:>5.1f} m3")
total_cut = 0.0
for x in vc:
    total_cut = total_cut + x
total_fill = 0.0
for x in vf:
    total_fill = total_fill + x
usable = total_cut * 0.9
print(f"cut {total_cut} m3 gives {usable:.1f} m3 of fill; fill needed {total_fill} m3")
if usable >= total_fill:
    print(f"spare spoil {usable - total_fill:.1f} m3 to haul away")
else:
    print(f"import {total_fill - usable:.1f} m3 of fill")
