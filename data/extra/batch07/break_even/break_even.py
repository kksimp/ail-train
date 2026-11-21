for n, f, p, u, fc in [("mug", 450000, 1200, 450, 900), ("tote bag", 300000, 1500, 700, 300), ("poster", 120000, 800, 150, 250), ("hoodie", 800000, 4000, 2200, 380)]:
    m = p - u; un = (f + m - 1) // m; pr = fc * m - f; a = abs(pr)
    print(f"{n}: break even at {un} units; at {fc}: {'-' if pr < 0 else ''}{a // 100}.{a % 100:02}")
