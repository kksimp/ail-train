for s in ["the quick brown fox", "  hello   world  ", "Is this the end?", "One.", ""]:
    ro = " ".join(reversed(s.split()))
    re_ = " ".join(w[::-1] for w in s.split())
    t = s.strip()
    if t and t[-1] in ".!?":
        ke = " ".join(reversed(t[:-1].split())) + t[-1]
    else:
        ke = " ".join(reversed(t.split()))
    print(f"[{ro}] [{re_}] [{ke}]")
