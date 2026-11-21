for n, i, d, p in [("Ade", 5200, 400, 1150), ("Bea", 3900, 650, 1100), ("Col", 7400, 1200, 1900), ("Dia", 2800, 150, 900), ("Eli", 6100, 300, 1450)]:
    r = (d + p) * 1000 // i; v = "approve" if r <= 360 else "refer" if r <= 430 else "decline"
    print(f"{n}: income {i}, outgoings {d + p}, ratio {r // 10}.{r % 10}% -> {v}")
