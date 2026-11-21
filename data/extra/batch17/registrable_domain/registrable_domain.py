def site_of(host, suffixes):
    labels = host.lower().split(".")
    for i in range(len(labels)):
        tail = ".".join(labels[i:])
        if tail in suffixes:
            if i == 0:
                return ""
            return ".".join(labels[i - 1:])
    return ""

suffixes = ["com", "org", "uk", "co.uk", "io", "github.io", "au", "com.au", "jp", "co.jp"]
hosts = ["www.example.com", "a.b.example.co.uk", "ana.github.io", "github.io", "shop.example.com.au", "localhost", "News.BBC.co.uk", "mail.yahoo.co.jp"]
for h in hosts:
    s = site_of(h, suffixes)
    shown = "(no registrable domain)" if s == "" else s
    print(f"{h:<20} {shown}")
pairs = [("ana.github.io", "ben.github.io"), ("www.example.com", "api.example.com"), ("example.co.uk", "other.co.uk")]
for a, b in pairs:
    same = site_of(a, suffixes) == site_of(b, suffixes)
    word = "same site" if same else "cross site"
    print(f"{a} vs {b}: {word}")
