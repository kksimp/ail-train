def needs_quotes(s):
    return "," in s or '"' in s or "\n" in s or s.startswith(" ") or s.endswith(" ")

def csv_field(s):
    if needs_quotes(s):
        inner = s.replace('"', '""')
        return '"' + inner + '"'
    return s

rows = [["sku", "title", "price", "note"], ["A-1", "Desk lamp", "24.50", ""], ["B-7", "Chair, oak", "89.00", "ships flat"], ["C-3", '12" ruler', "3.20", " fragile "], ["D-9", "Poster", "9.99", "two\nlines"]]
quoted = 0
for row in rows:
    cells = []
    for f in row:
        if needs_quotes(f):
            quoted += 1
        cells.append(csv_field(f))
    print(",".join(cells))
print(f"{quoted} fields needed quotes")
