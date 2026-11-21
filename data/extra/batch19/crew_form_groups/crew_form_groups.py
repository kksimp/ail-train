crews = ["abc ab ac", "xyz", "pq qr rp", "mno nmo omn", "a b c d", "kl lk klm"]
anyone = everyone = 0
for crew in crews:
    forms = [set(f) for f in crew.split(" ")]
    a = set().union(*forms); e = set(forms[0]).intersection(*forms)
    print(f"crew [{crew}]: anyone {len(a)}, everyone {len(e)}")
    anyone += len(a); everyone += len(e)
print(f"part 1: {anyone}")
print(f"part 2: {everyone}")
