tr = ["Intro", "Blue Hour", "Static", "Night Bus"]; at = 0; pl = False; vol = 5
for b in ["play", "next", "up", "up", "up", "back", "back", "pause", "down", "down", "eject", "next"]:
    if b == "play": pl = True
    elif b == "pause": pl = False
    elif b == "next": at = (at + 1) % 4
    elif b == "back": at = (at + 3) % 4
    elif b == "up": vol = min(vol + 2, 10)
    elif b == "down": vol = max(vol - 3, 0)
    print(f"{b:<5} -> {'playing' if pl else 'paused'} '{tr[at]}' vol {vol}")
