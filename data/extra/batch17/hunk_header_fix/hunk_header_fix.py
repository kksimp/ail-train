def header_nums(h):
    inner = h.replace("@", "").strip()
    halves = inner.split(" ")
    old = halves[0][1:].split(",")
    new = halves[1][1:].split(",")
    return [int(old[0]), int(old[1]), int(new[0]), int(new[1])]

diff = ["@@ -1,4 +1,4 @@", " [server]", "-port = 80", "+port = 8080", " host = a", " debug = no", "@@ -10,3 +10,5 @@", " [db]", "+pool = 8", "+timeout = 30", " name = shop", "@@ -20,2 +22,2 @@", " [log]", "-level = info", "-file = app.log", "+level = warn"]
i = 0
fixed = 0
while i < len(diff):
    head = diff[i]
    i += 1
    old_n = 0
    new_n = 0
    while i < len(diff) and not diff[i].startswith("@@"):
        l = diff[i]
        if not l.startswith("+"):
            old_n += 1
        if not l.startswith("-"):
            new_n += 1
        i += 1
    n = header_nums(head)
    if n[1] == old_n and n[3] == new_n:
        print(f"{head:<20} ok")
    else:
        fixed += 1
        print(f"{head:<20} body has -{old_n} +{new_n}, now @@ -{n[0]},{old_n} +{n[2]},{new_n} @@")
print(f"{fixed} header(s) rewritten")
