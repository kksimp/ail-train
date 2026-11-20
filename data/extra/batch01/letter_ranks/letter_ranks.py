text = "It was a bright cold day in April, and the clocks were striking thirteen.\nWinston Smith, his chin nuzzled into his breast in an effort to escape the vile wind,\nslipped quickly through the glass doors."
c = {}
for ch in text.lower():
    if ch.isalpha():
        c[ch] = c.get(ch, 0) + 1
tot = sum(c.values())
print(f"letters: {tot}, distinct: {len(c)}")
order = list(c)
for ch in sorted(order, key=lambda k: (-c[k], order.index(k)))[:5]:
    n = c[ch]
    print(f"{ch}: {n:>3} {n * 1000 // tot // 10}.{n * 1000 // tot % 10}%")
v = sum(c.get(x, 0) for x in "aeiou")
print(f"vowels {v}, consonants {tot - v}")
print("unused: " + "".join(x for x in "abcdefghijklmnopqrstuvwxyz" if x not in c))
