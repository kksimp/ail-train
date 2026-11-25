import sys

lines = sys.stdin.read().splitlines()
if lines:
    fleet = set(lines[0].split())
    left = len(fleet)
    shot = set()
    for raw in lines[1:]:
        s = raw.strip()
        if not s:
            continue
        ok = False
        if 2 <= len(s) <= 3 and "A" <= s[0] <= "J" and s[1:].isascii() and s[1:].isdigit():
            if str(int(s[1:])) == s[1:] and 1 <= int(s[1:]) <= 10:
                ok = True
        if not ok:
            print(f"{s}: invalid")
        elif s in shot:
            print(f"{s}: repeat")
        else:
            shot.add(s)
            if s in fleet:
                left -= 1
                print(f"{s}: " + ("hit, fleet sunk" if left == 0 else "hit"))
            else:
                print(f"{s}: miss")
