def expand(spec):
    out = []
    i = 0
    while i < len(spec):
        if i + 2 < len(spec) and spec[i + 1] == '-':
            for code in range(ord(spec[i]), ord(spec[i + 2]) + 1):
                out.append(chr(code))
            i += 3
        else:
            out.append(spec[i])
            i += 1
    return out

def translate(text, frm, to):
    src = expand(frm)
    dst = expand(to)
    out = []
    for c in text:
        if c in src:
            at = src.index(c)
            out.append(dst[min(at, len(dst) - 1)])
        else:
            out.append(c)
    return "".join(out)

def delete(text, st):
    gone = expand(st)
    return "".join(c for c in text if c not in gone)

def squeeze(text, st):
    keep = expand(st)
    out = []
    for c in text:
        last = out[-1] if out else '\n'
        if not (c in keep and c == last):
            out.append(c)
    return "".join(out)

print(translate("hello, world", "a-z", "A-Z"))
print(translate("Why did the chicken cross the road?", "a-zA-Z", "n-za-mN-ZA-M"))
print(translate("2026-11-21 10:45", "-: ", "/._"))
print(translate("secret plans", "a-z", "*"))
print(delete("call 555-0199 or 555-0123 today", "0-9-"))
print(squeeze("too    many     spaces   here", " "))
print(squeeze(translate("a--b__c  d", "-_ ", "..."), "."))
