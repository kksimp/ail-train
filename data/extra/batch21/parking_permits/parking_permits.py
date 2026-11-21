def controlled(day, hour):
    return day < 6 and 8 <= hour < 18

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
permits = {"LX19 AAB": "B", "KT20 CCD": "C", "MV21 EEF": "B"}
vouchers = {"YR70 GGH": 2, "SN66 JJK": 1}
seen = [("LX19 AAB", "B", 0, 9), ("KT20 CCD", "B", 0, 10), ("YR70 GGH", "C", 1, 11), ("YR70 GGH", "C", 1, 12), ("YR70 GGH", "C", 1, 13), ("SN66 JJK", "B", 5, 17), ("SN66 JJK", "B", 5, 18), ("WP12 LLM", "C", 6, 14), ("WP12 LLM", "C", 2, 8)]

def check(s):
    plate, zone, day, hour = s
    if not controlled(day, hour):
        return "free hours"
    if permits.get(plate, "") == zone:
        return "permit"
    left = vouchers.get(plate, 0)
    if left > 0:
        vouchers[plate] = left - 1
        return f"voucher ({left - 1} h left)"
    return "PENALTY"

fines = {}
for s in seen:
    r = check(s)
    if r == "PENALTY":
        fines[s[1]] = fines.get(s[1], 0) + 1
    print(f"{days[s[2]]} {s[3]:02d}:00 zone {s[1]} {s[0]}: {r}")
for zone, n in fines.items():
    print(f"zone {zone}: {n} penalty notices")
