for iban in ["GB82 WEST 1234 5698 7654 32", "GB82 WEST 1234 5698 7654 33", "DE89 3704 0044 0532 0130 00", "NL91ABNA0417164300", "XX12", "FR14 2004 1010 0505 0001 3M02 606", "GB82 WEST 1234 5698 7654 3!"]:
    s = iban.replace(" ", "").upper()
    if not 15 <= len(s) <= 34:
        print(f"{iban}: length {len(s)} is out of range"); continue
    m = s[4:] + s[:4]
    bad = next((c for c in m if not (c.isdigit() or "A" <= c <= "Z")), None)
    if bad:
        print(f"{iban}: bad character '{bad}'"); continue
    n = int("".join(c if c.isdigit() else str(ord(c) - 55) for c in m))
    print(f"{iban}: {'valid' if n % 97 == 1 else 'wrong check digits'}")
