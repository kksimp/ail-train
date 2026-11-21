queue = [("report", 5), ("photos", 9), ("letter", 2), ("manual", 12)]
sheet = 0; fin = []; can = []
for name, pages in queue:
    p = 0; jam = False
    while p < pages:
        sheet += 1
        if sheet % 7 == 0:
            print(f"jam on sheet {sheet}, {name} page {p + 1}: job cancelled")
            can.append(name); jam = True; break
        p += 1
    if jam: continue
    fin.append(name)
    print(f"{name}: all {pages} pages printed")
print(f"finished: {', '.join(fin)}; cancelled: {', '.join(can)}; {sheet} sheets fed")
