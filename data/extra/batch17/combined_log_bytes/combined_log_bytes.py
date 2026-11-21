class Hit:
    def __init__(self, ip, method, path, status, size):
        self.ip, self.method, self.path, self.status, self.size = ip, method, path, status, size

def to_int(s):
    t = s[1:] if s.startswith("-") else s
    return int(s) if t.isdigit() and t != "" else None

def parse(line):
    parts = line.split('"')
    if len(parts) < 3:
        return None, "no quoted request"
    ip = parts[0].split(" ")[0]
    req = parts[1].split(" ")
    if len(req) != 3:
        return None, "bad request field"
    tail = parts[2].strip().split(" ")
    status = to_int(tail[0])
    if status is None:
        return None, "bad status"
    size = to_int(tail[1])
    if size is None:
        size = 0
    return Hit(ip, req[0], req[1], status, size), None

lines = ['10.0.0.5 - - [12/Mar/2025:10:01:02 +0000] "GET /index.html HTTP/1.1" 200 5120', '10.0.0.7 - - [12/Mar/2025:10:01:09 +0000] "GET /logo.png HTTP/1.1" 200 20480', '10.0.0.5 - - [12/Mar/2025:10:02:11 +0000] "GET /about.html HTTP/1.1" 200 3072', '10.0.0.9 - - [12/Mar/2025:10:02:30 +0000] "POST /login HTTP/1.1" 302 -', '10.0.0.5 - - [12/Mar/2025:10:03:00 +0000] "GET /index.html HTTP/1.1" 304 0', '10.0.0.7 - - [12/Mar/2025:10:03:41 +0000] "GET /video.mp4 HTTP/1.1" 206 65536', 'garbage line without quotes', '10.0.0.9 - - [12/Mar/2025:10:04:02 +0000] "BREW" 400 0']
sent = {}
distinct = {}
seen = set()
posts = 0
for line in lines:
    h, err = parse(line)
    if h is not None:
        sent[h.ip] = sent.get(h.ip, 0) + h.size
        key = f"{h.ip} {h.path}"
        if key not in seen:
            seen.add(key)
            distinct[h.ip] = distinct.get(h.ip, 0) + 1
        if h.method == "POST":
            posts += 1
    else:
        print(f"skipped: {err}")
for ip, b in sent.items():
    print(f"{ip:<10} {b:>6} bytes, {distinct[ip]} paths")
order = sorted(sent.keys(), key=lambda k: -sent[k])
print(f"heaviest client: {order[0]}")
print(f"POST requests: {posts}")
