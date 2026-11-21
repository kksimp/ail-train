def estimates(sex, cm):
    inches = cm / 2.54 - 60.0
    if sex == "Man":
        return [50.0 + 2.3 * inches, 52.0 + 1.9 * inches, 56.2 + 1.41 * inches]
    return [45.5 + 2.3 * inches, 49.0 + 1.7 * inches, 53.1 + 1.36 * inches]
for sex, cm in [("Man", 165.0), ("Man", 180.0), ("Man", 193.0), ("Woman", 155.0), ("Woman", 170.0)]:
    e = estimates(sex, cm)
    spread = max(e) - min(e)
    print(f"Sex.{sex} {cm} cm: Devine {e[0]:.1f}, Robinson {e[1]:.1f}, Miller {e[2]:.1f} kg (spread {spread:.1f})")
