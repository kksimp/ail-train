def to_int(s):
    return int(s) if s.isdigit() else None

def parse_range(spec, size):
    dash = spec.find("-")
    if dash < 0:
        return []
    a = spec[:dash].strip()
    b = spec[dash + 1:].strip()
    if a == "":
        n = to_int(b)
        if n is None:
            n = 0
        if n <= 0:
            return []
        return [max(size - n, 0), size - 1]
    start = to_int(a)
    if start is None:
        start = -1
    if start < 0 or start >= size:
        return []
    if b == "":
        end = size - 1
    else:
        v = to_int(b)
        end = min(size - 1 if v is None else v, size - 1)
    if end < start:
        return []
    return [start, end]

def respond(header, size):
    if not header.startswith("bytes="):
        return f"200 whole file ({size} bytes)"
    spec = header[6:]
    parts = []
    total = 0
    for piece in spec.split(","):
        r = parse_range(piece, size)
        if len(r) == 2:
            parts.append(f"{r[0]}-{r[1]}")
            total += r[1] - r[0] + 1
    if len(parts) == 0:
        return f"416 range not satisfiable (size {size})"
    if len(parts) == 1:
        return f"206 bytes {parts[0]}/{size} ({total} bytes)"
    shown = ", ".join(parts)
    return f"206 multipart: {shown} ({total} bytes)"

size = 1000
for h in ["bytes=0-499", "bytes=500-", "bytes=-200", "bytes=0-99,200-299", "bytes=900-1200", "bytes=1500-", "bytes=-5000", "items=0-5", "bytes=300-100,950-"]:
    print(f"{h:<20} {respond(h, size)}")
