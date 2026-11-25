import re
import sys

# unit -> (category, factor in thousandths of the base unit)
UNITS = {
    "mm": (0, 1), "cm": (0, 10), "m": (0, 1000), "km": (0, 1000000),
    "mg": (1, 1), "g": (1, 1000), "kg": (1, 1000000),
    "ms": (2, 1), "s": (2, 1000), "min": (2, 60000), "h": (2, 3600000),
}
BASE = ["m", "g", "s"]
NAMES = ["length", "mass", "time"]


def fmt(thousandths):
    whole, frac = divmod(thousandths, 1000)
    if frac == 0:
        return str(whole)
    return "%d.%s" % (whole, ("%03d" % frac).rstrip("0"))


totals = [None, None, None]
for raw in sys.stdin.read().split("\n"):
    text = raw.strip()
    if text == "":
        continue
    m = re.fullmatch(r"([0-9]{1,12})\s*([A-Za-z]+)", text)
    if not m or m.group(2) not in UNITS:
        print("%s = invalid" % text)
        continue
    cat, factor = UNITS[m.group(2)]
    small = int(m.group(1)) * factor
    totals[cat] = (totals[cat] or 0) + small
    print("%s = %s %s" % (text, fmt(small), BASE[cat]))
for i in range(3):
    if totals[i] is not None:
        print("total %s: %s %s" % (NAMES[i], fmt(totals[i]), BASE[i]))
