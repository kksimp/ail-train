def split(syms, freq, lo, hi, prefix, codes):
    if hi - lo == 1:
        codes[syms[lo]] = "0" if prefix == "" else prefix
        return
    total = 0
    for i in range(lo, hi):
        total += freq[syms[i]]
    acc = 0
    best = lo + 1
    best_gap = total + 1
    for k in range(lo + 1, hi):
        acc += freq[syms[k - 1]]
        gap = abs(2 * acc - total)
        if gap < best_gap:
            best_gap = gap
            best = k
    split(syms, freq, lo, best, prefix + "0", codes)
    split(syms, freq, best, hi, prefix + "1", codes)

def show(c):
    return "_" if c == " " else c

text = "she sells sea shells by the sea"
freq = {}
for c in text:
    freq[c] = freq.get(c, 0) + 1
syms = sorted(freq, key=lambda c: (-freq[c], ord(c)))
codes = {}
split(syms, freq, 0, len(syms), "", codes)
bits = 0
for c in syms:
    code = codes[c]
    bits += freq[c] * len(code)
    print(f"{show(c)} x{freq[c]:<2} {code}")
n = len(text)
avg = bits / n
print(f"{bits} bits for {n} letters ({avg:.3f} per letter) against {n * 4} with fixed 4-bit codes")
