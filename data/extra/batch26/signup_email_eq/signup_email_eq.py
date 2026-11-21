raw = ["Ana@Mail.com", "bo@site.org", "ana@mail.com", " BO@site.org", "cy@site.org", "Cy@Site.org", "dee@mail.com"]
kept = []; dropped = 0
norm = lambda s: s.strip().lower()
for r in raw:
    if any(norm(k) == norm(r) for k in kept):
        print(f"duplicate: '{r}'")
        dropped += 1
        continue
    kept.append(r)
print(f"mailing list: {', '.join(kept)}")
print(f"{len(kept)} kept, {dropped} duplicates")
print(f"Zed@x.io vs zed@x.org same: {'true' if norm('Zed@x.io') == norm('zed@x.org') else 'false'}")
