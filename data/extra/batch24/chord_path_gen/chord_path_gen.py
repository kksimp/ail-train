state = 1960
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
nxt = {"I": ["IV", "V", "vi", "ii", "iii"], "ii": ["V", "vii"], "iii": ["vi", "IV"], "IV": ["V", "I", "ii"], "V": ["I", "vi"], "vi": ["ii", "IV"], "vii": ["I", "iii"]}
redraws = 0
for phrase in range(1, 5):
    chords = ["I"]
    while len(chords) < 6:
        here = chords[-1]
        options = nxt.get(here, ["I"])
        pick = options[below(len(options))]
        fits = "V" in nxt.get(pick, ["I"])
        if len(chords) == 5 and not fits:
            redraws += 1
            continue
        chords.append(pick)
    chords.append("V"); chords.append("I")
    print(f"phrase {phrase}: {' - '.join(chords)}")
print(f"{redraws} sixth chords re-drawn so the cadence V - I could follow")
