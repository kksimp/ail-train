snaps = [("web-1", 92, 120, 3), ("web-2", 40, 80, 0), ("db-1", 88, 12, 75), ("cache", 15, 9, 0)]
quiet = 0
for h, cpu, disk, err in snaps:
    out = []
    if cpu > 85: out.append(f"cpu {cpu}% over 85%")
    if disk < 20: out.append(f"only {disk} GB free")
    if not out:
        quiet += 1; continue
    print(f"{h}: {'; '.join(out)}")
print(f"{quiet} of {len(snaps)} hosts quiet")
