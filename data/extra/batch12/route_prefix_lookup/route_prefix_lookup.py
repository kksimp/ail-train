def to_num(ip):
    n = 0
    for part in ip.split("."):
        n = n * 256 + int(part)
    return n

def matches(addr, net, bits):
    if bits == 0:
        return True
    return (addr >> (32 - bits)) == (net >> (32 - bits))

table = [("0.0.0.0/0", "isp"), ("10.0.0.0/8", "core"), ("10.20.0.0/16", "branch"), ("10.20.30.0/24", "lab"), ("192.168.1.0/24", "office"), ("192.168.1.128/25", "wifi")]
for dest in ["10.1.2.3", "10.20.5.9", "10.20.30.77", "192.168.1.10", "192.168.1.200", "8.8.8.8"]:
    a = to_num(dest)
    best = -1
    via = ""
    route = ""
    for prefix, port in table:
        parts = prefix.split("/")
        bits = int(parts[1])
        if matches(a, to_num(parts[0]), bits) and bits > best:
            best = bits
            via = port
            route = prefix
    print(f"{dest:<14} -> {via:<6} ({route})")
