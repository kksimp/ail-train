checks = [("user", "at least 3 letters", lambda s: len(s) >= 3), ("user", "at most 12 letters", lambda s: len(s) <= 12), ("email", "has an @", lambda s: "@" in s), ("pin", "digits only", lambda s: s != "" and s.isdigit()), ("pin", "exactly 4 long", lambda s: len(s) == 4)]
forms = [{"user": "kim", "email": "kim@site.io", "pin": "4821"}, {"user": "al", "email": "al.site.io", "pin": "12a4"}, {"user": "maximilian_the_great", "email": "max@site.io", "pin": "99999"}]
for i, f in enumerate(forms):
    failed = [f"{fl} {lb}" for fl, lb, t in checks if not t(f.get(fl, ""))]
    print(f"form {i + 1}: ok" if not failed else f"form {i + 1}: {'; '.join(failed)}")
