def es(s): return "".join({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}.get(c, c) for c in s)
def un(s): return s.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&#39;", "'").replace("&amp;", "&")
for t in ["Fish & Chips", "<b>bold</b>", 'say "hi"', "it's 5 > 3 & 2 < 4", "plain text", "&amp; already"]:
    e = es(t); print(f"{e} | round trip {'true' if un(e) == t else 'false'}")
