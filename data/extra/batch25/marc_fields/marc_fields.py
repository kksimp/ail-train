def subfields(line):
    out = {}
    parts = line.split("$")
    for p in parts[1:]:
        if len(p) > 1:
            out[p[0]] = p[1:].strip()
    return out

def clean(s):
    t = s.strip()
    while t.endswith(" /") or t.endswith(" :") or t.endswith(",") or t.endswith("."):
        t = t[:len(t) - 1].strip()
    return t

def cite(record):
    fields = {}
    for line in record:
        fields[line[:3]] = line
    if "245" not in fields:
        return None
    t = subfields(fields["245"])
    title = clean(t.get('a', ""))
    sub = clean(t.get('b', ""))
    if sub != "":
        title = f"{title}: {sub}"
    author = clean(subfields(fields.get("100", "")).get('a', "Anonymous"))
    date = clean(subfields(fields.get("264", "")).get('c', "n.d."))
    return f"{author}. {title} ({date})"

records = [["100 1  $aTolkien, J. R. R.,", "245 14 $aThe hobbit :$bor there and back again /$cJ.R.R. Tolkien.", "264  1 $aLondon :$bAllen & Unwin,$c1937."], ["100 1  $aShelley, Mary,", "245 10 $aFrankenstein /$cMary Shelley.", "264  1 $aLondon :$bLackington,$c1818."], ["245 00 $aBeowulf :$ba new verse translation.", "264  1 $aNew York :$bNorton,$c2000."], ["100 1  $aAusten, Jane.", "264  1 $c1813."]]
for r in records:
    c = cite(r)
    if c is not None:
        print(c)
    else:
        print("rejected: no 245 title field")
