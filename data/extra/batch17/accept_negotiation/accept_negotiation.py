class Want:
    def __init__(self, kind, q):
        self.kind, self.q = kind, q

def parse_accept(h):
    out = []
    for part in h.split(","):
        bits = part.strip().split(";")
        q = 1000
        for b in bits[1:]:
            b = b.strip()
            if b.startswith("q="):
                f = float(b[2:])
                q = int(round(f * 1000.0))
        out.append(Want(bits[0].strip(), q))
    return out

def weight(wants, offer):
    major = offer.split("/")[0]
    best_spec = -1
    q = 0
    for w in wants:
        spec = 2 if w.kind == offer else 1 if w.kind == major + "/*" else 0 if w.kind == "*/*" else -1
        if spec > best_spec:
            best_spec = spec
            q = w.q
    return 0 if best_spec < 0 else q

def choose(header, offers):
    wants = parse_accept(header)
    best = ""
    best_q = 0
    for o in offers:
        q = weight(wants, o)
        if q > best_q:
            best = o
            best_q = q
    return "406 Not Acceptable" if best == "" else f"{best} (q={best_q})"

offers = ["application/json", "text/html", "text/csv"]
headers = ["text/html;q=0.9, application/json, */*;q=0.1", "text/*;q=0.5, text/csv;q=0.8", "image/png, image/*;q=0.5", "*/*", "application/xml, text/html;q=0", "text/*, text/html;q=0"]
for h in headers:
    print(f"{h:<46} -> {choose(h, offers)}")
