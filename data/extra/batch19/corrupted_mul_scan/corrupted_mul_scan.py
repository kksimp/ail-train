def number_at(s, i):
    j = i; n = 0
    while j < len(s) and j - i < 3 and s[j].isdigit():
        n = n * 10 + int(s[j]); j += 1
    return [n, j - i, j]

def scan(text, switches):
    total = 0; enabled = True; i = 0
    while i < len(text):
        rest = text[i:]
        if rest.startswith("on()"):
            enabled = True
        elif rest.startswith("off()"):
            enabled = False
        elif rest.startswith("mul("):
            a = number_at(text, i + 4)
            if a[1] > 0 and a[2] < len(text) and text[a[2]] == ',':
                b = number_at(text, a[2] + 1)
                if b[1] > 0 and b[2] < len(text) and text[b[2]] == ')' and (enabled or not switches):
                    total += a[0] * b[0]
        i += 1
    return total

dump = "xmul(3,4)%&mul[2,2]off()mul(10,20)!mul(7,8)on()?mul(5,5)mul(1234,2)mul( 6,6)when()mul(11,9)off()mul(2,3"
print(f"dump of {len(dump)} characters")
print(f"part 1: all products sum to {scan(dump, False)}")
print(f"part 2: enabled products sum to {scan(dump, True)}")
