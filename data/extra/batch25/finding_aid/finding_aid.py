levels = ["fonds", "series", "file", "item"]
units = [("MS7", "Harrow Mill papers", 0), ("MS7/2", "Correspondence", 0), ("MS7/1", "Accounts", 0), ("MS7/1/1", "Wage books 1880-1899", 14), ("MS7/1/2", "Ledgers of sales", 9), ("MS7/2/1", "Letters from agents", 120), ("MS7/2/10", "Letters to the bank", 33), ("MS7/2/2", "Union letters", 41), ("MS7/3", "Photographs", 0), ("MS7/3/1", "Mill floor 1902", 1), ("MS7/1/1/4", "Wage book 1884", 1)]

def key(code):
    return [int(p) for p in code.split("/")[1:]]

for code, title, items in sorted(units, key=lambda u: key(u[0])):
    depth = code.count("/")
    prefix = code + "/"
    total = sum(v[2] for v in units if v[0] == code or v[0].startswith(prefix))
    indent = "  " * depth
    print(f"{indent}{code} [{levels[depth]}] {title} ({total} items)")
print(f"{len(units)} units described")
