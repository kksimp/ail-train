def to_int(s):
    t = s[1:] if s.startswith("-") else s
    return t != "" and t.isdigit()

def to_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_date(s):
    if len(s) != 10:
        return False
    for i, c in enumerate(s):
        if i == 4 or i == 7:
            if c != '-':
                return False
        elif not c.isdigit():
            return False
    return True

def is_flag(s):
    return s.lower() in ["true", "false", "yes", "no"]

def guess(values):
    vals = [v for v in values if v != ""]
    if all(to_int(v) for v in vals):
        return "int"
    if all(to_float(v) for v in vals):
        return "float"
    if all(is_flag(v) for v in vals):
        return "bool"
    if all(is_date(v) for v in vals):
        return "date"
    return "text"

text = "id,price,active,joined,city,score\n1,12.5,yes,2024-01-05,Oslo,7\n2,8,no,2024-02-11,,-3\n3,,Yes,2023-12-30,Lima,10\n4,3.25,no,2024-13-01x,Pune,\n5,7.75,true,,Kyiv,4"
lines = text.split("\n")
header = lines[0].split(",")
rows = [l.split(",") for l in lines[1:]]
for j, name in enumerate(header):
    col = [r[j] for r in rows]
    blanks = len([v for v in col if v == ""])
    print(f"{name:<7} {guess(col):<6} {blanks} missing")
