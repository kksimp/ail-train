def ones():
    return ["", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"]

def tens():
    return ["", "", "zwanzig", "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"]

def unit_word(n):
    return "ein" if n == 1 else ones()[n]

def below_100(n):
    if n < 20:
        return ones()[n]
    t = tens()[n // 10]
    if n % 10 == 0:
        return t
    return f"{unit_word(n % 10)}und{t}"

def below_1000(n):
    if n < 100:
        return below_100(n)
    head = f"{unit_word(n // 100)}hundert"
    if n % 100 == 0:
        return head
    return f"{head}{below_100(n % 100)}"

def german(n):
    if n < 1000:
        return below_1000(n)
    th = n // 1000
    head = "eintausend" if th == 1 else f"{below_1000(th)}tausend"
    if n % 1000 == 0:
        return head
    return f"{head}{below_1000(n % 1000)}"

for n in [1, 11, 16, 17, 21, 30, 67, 101, 199, 1000, 2025, 31001, 999999]:
    print(f"{n:>6} {german(n)}")
