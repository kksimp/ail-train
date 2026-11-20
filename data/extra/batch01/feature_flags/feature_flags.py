NAMES = ["dark_mode", "beta_search", "new_checkout", "offline", "telemetry"]
flags = 0
def active(f):
    return [NAMES[i] for i in range(len(NAMES)) if f & (1 << i)]
for cmd in ["on dark_mode", "on offline", "on telemetry", "off offline", "toggle beta_search", "on warp_drive", "toggle dark_mode"]:
    op, name = cmd.split(" ")
    if name not in NAMES:
        print(f"unknown flag {name}")
        continue
    b = 1 << NAMES.index(name)
    if op == "on": flags |= b
    elif op == "off": flags &= ~b
    elif op == "toggle": flags ^= b
    print(f"{cmd:<20} {flags:05b} [{' '.join(active(flags))}]")
print(f"count: {len(active(flags))}, value {flags}")
