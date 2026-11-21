def fi(t, l): return t if len(t) <= l else t[:l - 3] + "..."
C = [("email to kim@home.net", 200, lambda t, b: f"Subject: {t} | {b}"), ("sms to 07700 900123", 40, lambda t, b: f"{t}: {b}"), ("push to phone", 30, lambda t, b: t)]
for t, b in [("Delivery today", "Your parcel arrives between 10:00 and 12:00."), ("Payment due", "Card ending 4242 will be charged on the 3rd.")]:
    for n, l, r in C: print(f"{n}: {fi(r(t, b), l)}")
