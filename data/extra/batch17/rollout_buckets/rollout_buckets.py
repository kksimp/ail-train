def bucket(user, feature):
    h = 7
    for c in f"{feature}:{user}":
        h = (h * 31 + ord(c)) % 4294967296
    return h % 100

users = ["ana", "ben", "cy", "dev", "eli", "fay", "gus", "hal", "ivy", "jon", "kai", "liv"]
for u in users:
    print(f"{u:<4} bucket {bucket(u, 'new-checkout'):>2}")
before = []
for pct in [20, 25, 50, 100]:
    on = [u for u in users if bucket(u, "new-checkout") < pct]
    kept = "true" if all(u in on for u in before) else "false"
    shown = " ".join(on)
    print(f"{pct:>3}% -> {len(on):>2} users, earlier users kept: {kept}: {shown}")
    for u in on:
        if u not in before:
            before.append(u)
other = " ".join(u for u in users if bucket(u, "dark-mode") < 25)
print(f"dark-mode at 25%: {other}")
