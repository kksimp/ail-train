def run_season(et, rain, raw, log):
    deficit = 0; applied = 0
    for day in range(len(et)):
        deficit += et[day] - rain[day]
        if deficit < 0: deficit = 0
        if deficit >= raw:
            log.append(f"day {day + 1:>2}: deficit {deficit} mm, irrigate {deficit} mm")
            applied += deficit
            deficit = 0
    return applied
et = [4, 5, 5, 6, 6, 7, 3, 2, 5, 6, 7, 7, 8, 6, 4, 5, 6, 7, 7, 6]
rain = [0, 0, 12, 0, 0, 0, 9, 15, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 22, 0]
taw = 44; raw = taw // 2
log = []
applied = run_season(et, rain, raw, log)
for line in log: print(line)
print(f"{len(et)} days: crop used {sum(et)} mm, rain {sum(rain)} mm, irrigation {applied} mm in {len(log)} waterings")
