changes = [int(s) for s in "+9,-4,+6,-13,+5".split(",")]
print(f"changes: {changes}")
print(f"part 1: after one pass the dial reads {sum(changes)}")
seen = {0}; at = 0; steps = 0; found = False
while not found:
    for c in changes:
        at += c; steps += 1
        if at in seen:
            found = True; break
        seen.add(at)
print(f"part 2: {at} is reached twice, after {steps} changes ({len(seen)} settings seen)")
