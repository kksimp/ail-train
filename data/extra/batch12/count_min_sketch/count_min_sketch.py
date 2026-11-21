def base_hash(s):
    h = 0
    for c in s:
        h = (h * 31 + ord(c)) % 1000003
    return h

def slot(s, row):
    seeds = [[17, 5], [29, 11], [43, 3], [61, 7]]
    return ((base_hash(s) * seeds[row][0] + seeds[row][1]) % 1009) % 16

pages = ["/home", "/shop", "/cart", "/help", "/blog", "/about", "/jobs", "/news", "/faq", "/login"]
grid = [[0] * 16 for _ in range(4)]
truth = {}
seed = 11
for i in range(300):
    seed = (seed * 1103515245 + 12345) % 2147483648
    roll = (seed >> 8) % 100
    if roll < 40:
        page = pages[0]
    elif roll < 60:
        page = pages[1]
    elif roll < 70:
        page = pages[2]
    else:
        page = pages[3 + roll % 7]
    truth[page] = truth.get(page, 0) + 1
    for r in range(4):
        grid[r][slot(page, r)] += 1
for p in pages:
    est = min(grid[r][slot(p, r)] for r in range(4))
    real = truth.get(p, 0)
    print(f"{p:<7} true {real:>3}, estimate {est:>3}, over by {est - real}")
print(f"64 counters for {len(pages)} pages")
