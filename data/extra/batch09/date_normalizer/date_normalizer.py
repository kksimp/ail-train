def month_of(name):
    names = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    key = name.lower()[:min(3, len(name))]
    return (names.index(key) if key in names else -1) + 1

def days_in(y, m):
    leap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
    lengths = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return lengths[m - 1]

def to_i(s):
    try:
        return int(s)
    except ValueError:
        return 0

def normalise(text):
    t = text.replace(",", "")
    y = m = d = 0
    if "-" in t:
        p = t.split("-")
        y, m, d = to_i(p[0]), to_i(p[1]), to_i(p[2])
    elif "/" in t:
        p = t.split("/")
        d, m, y = to_i(p[0]), to_i(p[1]), to_i(p[2])
    elif " " in t:
        p = t.split(" ")
        if len(p) != 3:
            return None, "unknown layout"
        if p[0][0].isdigit():
            d = to_i(p[0])
            m = month_of(p[1])
        else:
            m = month_of(p[0])
            d = to_i(p[1])
        y = to_i(p[2])
    else:
        return None, "unknown layout"
    if m < 1 or m > 12:
        return None, f"no month {m}"
    if d < 1 or d > days_in(y, m):
        return None, f"day {d} is not in {y}-{m:02}"
    return f"{y}-{m:02}-{d:02}", None

for t in ["2024-03-05", "05/03/2024", "5 Mar 2024", "March 5, 2024", "20240305", "29 Feb 2023", "29/02/2024", "2024-13-01", "next tuesday"]:
    iso, err = normalise(t)
    if iso is not None:
        print(f"{t:<14} -> {iso}")
    else:
        print(f"{t:<14} -> rejected: {err}")
