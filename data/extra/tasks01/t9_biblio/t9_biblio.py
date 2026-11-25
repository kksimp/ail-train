import sys


def author(a):
    if "," not in a:
        return None
    last, given = a.split(",", 1)
    last = last.strip()
    names = given.split()
    if last == "" or not names:
        return None
    return last + ", " + " ".join(n[0].upper() + "." for n in names)


good = []
bad = []
for k, line in enumerate(sys.stdin.read().split("\n"), 1):
    if line.strip() == "":
        continue
    f = [p.strip() for p in line.split("|")]
    if len(f) != 4:
        bad.append(k)
        continue
    raw_authors, title, year, venue = f
    authors = [author(a) for a in raw_authors.split(";")]
    if None in authors or title == "" or venue == "":
        bad.append(k)
        continue
    if len(year) != 4 or not all(c in "0123456789" for c in year):
        bad.append(k)
        continue
    if len(authors) == 1:
        al = authors[0]
    elif len(authors) == 2:
        al = authors[0] + " & " + authors[1]
    else:
        al = ", ".join(authors[:-1]) + ", & " + authors[-1]
    good.append("%s (%s). %s. %s." % (al, year, title, venue))
for c in sorted(good):
    print(c)
for k in bad:
    print("error: line %d: bad entry" % k)
