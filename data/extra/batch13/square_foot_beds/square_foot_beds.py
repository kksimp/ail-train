crops = [("tomato", 1, 4, 85), ("lettuce", 4, 3, 80), ("beet", 9, 2, 70), ("carrot", 16, 3, 65), ("pepper", 1, 2, 60), ("onion", 16, 2, 75)]

def plants(c):
    return c[1] * c[2]

def seeds(c):
    return (plants(c) * 100 + c[3] - 1) // c[3]

bed_squares = 16
used = sum(c[2] for c in crops)
print("crop     squares plants seeds")
for c in crops:
    print(f"{c[0]:<8} {c[2]:>7} {plants(c):>6} {seeds(c):>5}")
print(f"{used} squares planted in two 4 x 4 beds ({2 * bed_squares - used} free)")
biggest = sorted(crops, key=lambda c: -plants(c))[0]
print(f"most plants: {biggest[0]} ({plants(biggest)})")
