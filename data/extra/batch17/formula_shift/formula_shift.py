def col_num(letters):
    n = 0
    for c in letters:
        n = n * 26 + ord(c) - 64
    return n

def col_name(n):
    out = []
    k = n
    while k > 0:
        r = (k - 1) % 26
        out.insert(0, chr(65 + r))
        k = (k - 1) // 26
    return "".join(out)

def shift(formula, dr, dc):
    cs = list(formula)
    out = []
    i = 0
    while i < len(cs):
        start = i
        abs_col = False
        if cs[i] == '$':
            abs_col = True
            i += 1
        letters = []
        while i < len(cs) and cs[i].isupper():
            letters.append(cs[i])
            i += 1
        abs_row = False
        if i < len(cs) and cs[i] == '$' and len(letters) > 0:
            abs_row = True
            i += 1
        digits = []
        while i < len(cs) and cs[i].isdigit():
            digits.append(cs[i])
            i += 1
        if len(letters) > 0 and len(digits) > 0:
            col = col_num("".join(letters))
            row = int("".join(digits))
            new_col = col if abs_col else col + dc
            new_row = row if abs_row else row + dr
            out.append(("$" if abs_col else "") + col_name(new_col) + ("$" if abs_row else "") + str(new_row))
        elif i == start:
            out.append(cs[i])
            i += 1
        else:
            out.append(formula[start:i])
    return "".join(out)

f = "=SUM(A1:A9)+$B$2*C$3-$D4/Z10"
print(f"C5 : {f}")
for name, dr, dc in [("D5", 0, 1), ("C8", 3, 0), ("AB12", 7, 25)]:
    print(f"{name:<4}: {shift(f, dr, dc)}")
