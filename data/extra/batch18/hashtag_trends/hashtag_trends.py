posts = ["Morning run by the river #running #Sunrise", "New PB today! #Running #marathon", "Coffee first #sunrise #coffee", "Rain again #running", "Trying oat milk #Coffee #vegan", "Hill reps done #marathon #running", "Lazy sunday # nothing"]
c = {}
for p in posts:
    for w in p.split():
        if w.startswith("#") and len(w) > 1: c[w.lower()] = c.get(w.lower(), 0) + 1
order = list(c)
top = sorted(order, key=lambda k: (-c[k], order.index(k)))[:3]
for i, t in enumerate(top): print(f"{i + 1}. {t} ({c[t]} posts)")
print("used once: [" + ", ".join(f'"{k}"' for k in sorted(k for k in c if c[k] == 1)) + "]")
print(f"{len(c)} distinct tags in {len(posts)} posts")
