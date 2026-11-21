import math
week = 0.0
for n, r, w in [("espresso", 2.0, 36.0), ("pour over", 16.0, 250.0), ("french press", 15.0, 500.0), ("cold brew", 8.0, 1000.0), ("aeropress", 13.0, 220.0), ("moka pot", 10.0, 200.0)]:
    g = w / r; week += g * 7.0
    print(f"{n:<12} 1:{r:<4.0f} {w:>6.0f} g water -> {g:>5.1f} g coffee ({g / 5.0:.1f} tbsp)")
print(f"a week of one of each: {week:.0f} g, {math.ceil(week / 250.0)} bags of 250 g")
