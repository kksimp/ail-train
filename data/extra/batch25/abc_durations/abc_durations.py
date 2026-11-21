def bar_lengths(music):
    cs = music
    bars = []
    cur = 0
    i = 0
    while i < len(cs):
        c = cs[i]
        if c == '|':
            bars.append(cur)
            cur = 0
            i += 1
        elif c in "ABCDEFGabcdefgz":
            i += 1
            while i < len(cs) and cs[i] in ",'":
                i += 1
            num = 0
            while i < len(cs) and cs[i].isdigit():
                num = num * 10 + int(cs[i])
                i += 1
            if num == 0:
                num = 1
            den = 1
            if i < len(cs) and cs[i] == '/':
                i += 1
                den = 0
                while i < len(cs) and cs[i].isdigit():
                    den = den * 10 + int(cs[i])
                    i += 1
                if den == 0:
                    den = 2
            cur += 16 * num // den
        else:
            i += 1
    return bars

tunes = [("waltz", 6, "A2 B2 c2 | d3 c B2 | A4 z2 | G2 A B c2 | d6 |"), ("jig", 6, "d2c B2A | G3 A3 | B/c/d e3 | d2B A2G G |"), ("march", 8, "C,2 E,G, C2 E2 | ^F2 G2 _B2 A2 | G8 |"), ("reel", 8, "A/B/c dB AFDF | A2 FA d3/2e/f2 | g2 fe d4 |")]
for name, units, music in tunes:
    bars = bar_lengths(music)
    want = units * 16
    shown = " ".join(f"{b // 16}{'' if b % 16 == 0 else '+'}" for b in bars)
    bad = [i + 1 for i, b in enumerate(bars) if b != want]
    verdict = "all bars full" if not bad else "wrong bars [" + ", ".join(str(x) for x in bad) + "]"
    print(f"{name:<6} want {units} units: {shown} -> {verdict}")
