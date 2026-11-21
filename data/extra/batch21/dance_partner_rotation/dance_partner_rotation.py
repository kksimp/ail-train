leads = ["Al", "Bo", "Cy", "Dev", "Eli", "Fox"]
follows = ["Gia", "Hen", "Isa", "Jo", "Kay", "Liv", "Mo"]
pairs = set()
sat = []
for d in range(7):
    line = []
    for p in range(len(leads)):
        f = follows[(p + d) % len(follows)]
        pairs.add(f"{leads[p]}-{f}")
        line.append(f"{leads[p]}-{f}")
    out = follows[(6 + d) % len(follows)]
    sat.append(out)
    if d < 3:
        print(f"dance {d + 1}: {' '.join(line)}; sitting out {out}")
print("...")
print(f"after 7 dances: {len(pairs)} of {len(leads) * len(follows)} pairings danced")
print(f"sit-outs in order: {', '.join(sat)}")
