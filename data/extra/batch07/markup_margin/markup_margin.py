for n, c, p in [("lamp", 2400, 3990), ("chair", 5500, 8900), ("rug", 12000, 15900), ("vase", 800, 2500)]:
    mk = (p - c) * 1000 // c; mg = (p - c) * 1000 // p; t = (c * 100 + 59) // 60
    print(f"{n}: markup {mk // 10}.{mk % 10}%, margin {mg // 10}.{mg % 10}%, 40% margin needs {t // 100}.{t % 100:02}")
