files = [("Holiday Photo.JPG", 1800), ("report.docx", 120), ("scan.pdf", 5300), ("README", 3), (".png", 10), ("Floor Plan v2.png", 640)]
st = []
for n, kb in files:
    if kb > 2048: print(f"{n}: {kb} KB is over the 2048 KB limit"); continue
    d = n.rfind(".")
    if d < 0: print(f"{n}: no extension"); continue
    ext = n[d + 1:].lower()
    if ext not in ["png", "jpg", "pdf"]: print(f"{n}: type .{ext} is not allowed"); continue
    stem = n[:d].strip()
    if not stem: print(f"{n}: empty file name"); continue
    s = f"{stem.lower().replace(' ', '-')}.{ext}"; st.append(s); print(f"{n}: stored as {s}")
print(f"{len(st)} of {len(files)} uploads accepted")
