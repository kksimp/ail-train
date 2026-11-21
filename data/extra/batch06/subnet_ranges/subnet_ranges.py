def ti(ip):
    n = 0
    for p in ip.split("."): n = n * 256 + int(p)
    return n
def dt(n): return f"{(n >> 24) & 255}.{(n >> 16) & 255}.{(n >> 8) & 255}.{n & 255}"
for c in ["192.168.1.130/26", "10.4.77.9/8", "172.16.5.200/30", "203.0.113.77/24", "198.51.100.14/32"]:
    a, b = c.split("/"); a = ti(a); b = int(b); s = 1 << (32 - b); n = a // s * s; l = n + s - 1
    if b >= 31: print(f"{c}: network {dt(n)}, {s} address(es), no host range"); continue
    print(f"{c}: network {dt(n)}, broadcast {dt(l)}, hosts {dt(n + 1)} - {dt(l - 1)} ({s - 2})")
