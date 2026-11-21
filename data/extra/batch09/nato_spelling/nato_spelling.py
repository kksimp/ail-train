WORDS = "Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey Xray Yankee Zulu".split(" ")
DIGITS = "Zero One Two Three Four Five Six Seven Eight Niner".split(" ")

def spell(code):
    out = []
    for c in code.upper():
        if c.isupper():
            out.append(WORDS[ord(c) - 65])
        elif c.isdigit():
            out.append(DIGITS[int(c)])
        elif c == '-':
            out.append("(dash)")
    return " ".join(out)

def unspell(spoken):
    out = []
    for w in spoken.split(" "):
        if w in WORDS:
            out.append(chr(WORDS.index(w) + 65))
        elif w in DIGITS:
            out.append(chr(DIGITS.index(w) + 48))
        else:
            out.append('-')
    return "".join(out)

for code in ["QX7-K9", "ZB42", "hj-1905"]:
    print(f"{code:<8} {spell(code)}")
heard = "Tango Echo Sierra Tango (dash) Niner One"
print(f"heard: {heard}")
print(f"code:  {unspell(heard)}")
