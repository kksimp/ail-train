import re
def parse(t):
    ps = t.split(".")
    if len(ps) != 4:
        return None, f"needs 4 parts, has {len(ps)}"
    v = 0
    for p in ps:
        if len(p) > 1 and p.startswith("0"):
            return None, f"leading zero in '{p}'"
        if not re.fullmatch(r"-?\d+", p):
            return None, f"'{p}' is not a number"
        n = int(p)
        if n < 0 or n > 255:
            return None, f"{n} is out of range"
        v = v * 256 + n
    return v, None
def private(v):
    a, b = v >> 24, (v >> 16) & 255
    return a == 10 or (a == 172 and 16 <= b <= 31) or (a == 192 and b == 168)
for ip in ["192.168.1.20", "8.8.8.8", "10.0.0.256", "172.20.3.4", "172.32.0.1", "1.2.3", "01.2.3.4", "a.b.c.d", "255.255.255.255"]:
    v, e = parse(ip)
    if v is not None:
        print(f"{ip:<16} {v:>10} {'private' if private(v) else 'public'}")
    else:
        print(f"{ip:<16} invalid: {e}")
