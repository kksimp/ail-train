state = 7
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def clashes(parts):
    for i in range(1, len(parts)):
        if parts[i-1][-1] in "aeiou" and parts[i][0] in "aeiou": return True
    return False
starts = ["ash", "bra", "cor", "dun", "el", "fe", "gar", "lo"]
middles = ["a", "ber", "in", "ow", "ra", "th"]
ends = ["by", "den", "ford", "ham", "ock", "ton", "wick"]
names = []; thrown = 0
while len(names) < 10:
    parts = [starts[below(len(starts))]]
    if below(2) == 1: parts.append(middles[below(len(middles))])
    parts.append(ends[below(len(ends))])
    if clashes(parts):
        thrown += 1; continue
    word = "".join(parts)
    names.append(word[0].upper() + word[1:])
print(", ".join(names[:5]))
print(", ".join(names[5:]))
print(f"{thrown} draws thrown away for meeting vowels")
