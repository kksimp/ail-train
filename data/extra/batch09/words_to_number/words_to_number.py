def small_values():
    names = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split(" ")
    m = {n: i for i, n in enumerate(names)}
    tens = "twenty thirty forty fifty sixty seventy eighty ninety".split(" ")
    for i, n in enumerate(tens):
        m[n] = (i + 2) * 10
    return m

def parse(text):
    values = small_values()
    total = 0
    group = 0
    words = [w for w in text.replace("-", " ").split(" ") if w != "" and w != "and"]
    if not words:
        return None, "empty"
    for w in words:
        if w in values:
            group += values[w]
        elif w == "hundred":
            group *= 100
        elif w == "thousand":
            total += group * 1000
            group = 0
        elif w == "million":
            total += group * 1000000
            group = 0
        else:
            return None, f"unknown word '{w}'"
    return total + group, None

for t in ["forty-two", "two hundred and forty-five", "one thousand nine hundred eighty-four", "seven million three hundred thousand and seven", "twelve thousand", "ninety-nine thousand nine hundred ninety-nine", "three dozen", "zero"]:
    n, err = parse(t)
    if n is not None:
        print(f"{n:>9}  {t}")
    else:
        print(f"    error  {t}: {err}")
