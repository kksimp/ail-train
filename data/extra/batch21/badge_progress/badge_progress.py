badges = {"Camper": {"tent", "cook", "knots", "night"}, "Navigator": {"map", "compass", "route", "night"}, "First Aid": {"bandage", "recovery", "cpr"}, "Naturalist": {"birds", "trees", "pond", "map"}}
scouts = [("Ivy", {"tent", "cook", "knots", "night", "map", "compass"}), ("Jo", {"bandage", "cpr", "birds", "trees", "pond", "map"}), ("Kit", {"route", "compass"})]
for name, done in scouts:
    earned = []
    best = ""
    best_missing = 99
    for badge, req in badges.items():
        if req <= done:
            earned.append(badge)
        else:
            lacking = len(req - done)
            if lacking < best_missing:
                best_missing = lacking
                best = badge
    print(f"{name}: earned {', '.join(earned) if earned else 'none'}")
    print(f"  closest: {best}, needs {', '.join(sorted(badges[best] - done))}")
