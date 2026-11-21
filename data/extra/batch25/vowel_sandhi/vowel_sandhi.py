def short(c):
    return {'ā': 'a', 'ī': 'i', 'ū': 'u'}.get(c, c)

def long(c):
    if c == 'a':
        return "ā"
    if c == 'i':
        return "ī"
    return "ū"

def join(first, second):
    x = short(first[-1])
    y = short(second[0])
    head = first[:-1]
    tail = second[1:]
    if x not in "aiu" or y not in "aiueo":
        return f"{first} {second}"
    if x == y:
        return head + long(x) + tail
    if x == 'a':
        mid = {"i": "e", "u": "o", "e": "ai"}.get(y, "au")
        return head + mid + tail
    glide = "y" if x == 'i' else "v"
    return head + glide + second

pairs = [("na", "asti"), ("deva", "indra"), ("sūrya", "udaya"), ("iti", "api"), ("su", "āgatam"), ("guru", "upadeśa"), ("rāma", "eva"), ("nadī", "iva"), ("tava", "odana"), ("vana", "gacchati")]
fused = 0
for first, second in pairs:
    j = join(first, second)
    if " " not in j:
        fused += 1
    print(f"{first} + {second} = {j}")
print(f"{fused} of {len(pairs)} pairs fused")
