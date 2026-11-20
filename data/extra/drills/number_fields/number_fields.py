import re

def parse_field(raw, base=10):
    t = raw.strip()
    if base == 10 and re.fullmatch(r"-?[0-9]+", t):
        return int(t)
    return None

def sum_fields(line):
    return sum(parse_field(f) or 0 for f in line.split(","))

def bad_fields(line):
    return [f.strip() for f in line.split(",") if parse_field(f) is None]

for line in ["1, 2,3", " 10 ,x, -4", "+7,7", ",,", "0x1f, 31"]:
    bad = bad_fields(line)
    note = "clean" if not bad else "bad: [" + "|".join(bad) + "]"
    print(f"{sum_fields(line)} {note}")
print(int("ff", 16))
print(int("101", 2))
print(-1)
print(-1)
print(-7)
print(f"{2.5 * 2.0:.1f}")
print("got 43")
