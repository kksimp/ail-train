COMMON = ["password", "letmein", "qwerty"]
def check(pw):
    if len(pw) < 8:
        return (f"too short: {len(pw)} characters", f"add {8 - len(pw)} more")
    if " " in pw:
        return ("contains a space", "remove spaces")
    if pw.lower() in COMMON:
        return (f"too common: {pw.lower()}", "pick something less common")
    if not any(c.isdigit() for c in pw):
        return ("no digit", "add a number")
    if not any(c.isupper() for c in pw):
        return ("no capital letter", "add a capital")
    return None
for pw in ["abc", "Password", "longenough", "longenough7", "Long enough7", "Longenough7"]:
    e = check(pw)
    if e:
        print(f"{pw}: {e[0]}; {e[1]}")
    else:
        print(f"{pw}: ok")
