def layer(seed, spacing, width):
    state = seed
    def below(n):
        nonlocal state
        state = (state * 1103515245 + 12345) % 2147483648
        return (state // 65536) % n
    knots = [below(100) for k in range(width // spacing + 2)]
    out = []
    for x in range(width):
        k = x // spacing; f = x % spacing
        out.append((knots[k] * (spacing - f) + knots[k + 1] * f) // spacing)
    return out
width = 49
coarse = layer(17, 8, width)
fine = layer(71, 2, width)
mixed = [(2 * coarse[x] + fine[x]) // 3 for x in range(width)]
for level in range(6):
    cut = 90 - level * 16
    print("".join('#' if v >= cut else '.' for v in mixed))
print(f"heights from {min(mixed)} to {max(mixed)}")
