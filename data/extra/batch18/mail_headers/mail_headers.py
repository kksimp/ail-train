raw = ["From: Lena Ortiz <lena@example.org>", "To: team@example.org", "Subject: Re: Re: RE: Offsite: agenda", "Date: Tue, 17 Nov 2026 09:12:44 +0000", "X-Labels: travel, planning,", "  budget", "Received from mx1"]
keys = []; vals = {}; bad = 0
for l in raw:
    if l.startswith(" "):
        if keys: vals[keys[-1]] = vals[keys[-1]] + " " + l.strip()
        continue
    p = l.split(": ", 1)
    if len(p) < 2: bad += 1; continue
    k = p[0].lower(); keys.append(k); vals[k] = p[1]
for k in keys: print(f"{k:<9} {vals[k]}")
s = vals.get("subject", "")
while s.startswith("Re: ") or s.startswith("RE: "): s = s[4:]
print(f"thread topic: {s}")
print(f"{len(keys)} headers, {bad} unreadable")
