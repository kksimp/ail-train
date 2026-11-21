def classify(temp, rain):
    warm = max(temp)
    cold = min(temp)
    mean = 0.0
    for t in temp:
        mean = mean + t
    mean = mean / 12.0
    total = sum(rain)
    if warm < 10.0:
        return "ET" if warm > 0.0 else "EF"
    limit = 20.0 * mean + 140.0
    if float(total) < limit:
        return "BW" if float(total) < limit / 2.0 else "BS"
    driest = min(rain)
    if cold >= 18.0:
        if driest >= 60:
            return "Af"
        return "Am" if driest * 25 >= 2500 - total else "Aw"
    group = "C" if cold > -3.0 else "D"
    summer = rain[3:9]
    winter = [rain[0], rain[1], rain[2], rain[9], rain[10], rain[11]]
    dry_summer = min(summer)
    dry_winter = min(winter)
    wet_summer = max(summer)
    wet_winter = max(winter)
    if dry_summer < 40 and dry_summer * 3 < wet_winter:
        season = "s"
    elif dry_winter * 10 < wet_summer:
        season = "w"
    else:
        season = "f"
    warm_months = len([t for t in temp if t >= 10.0])
    heat = "a" if warm >= 22.0 else "b" if warm_months >= 4 else "c"
    return f"{group}{season}{heat}"

stations = [("Equatoria", [27.0, 27.5, 28.0, 28.0, 28.0, 27.5, 27.0, 27.0, 27.0, 27.0, 26.5, 26.5], [240, 160, 180, 180, 170, 160, 160, 170, 170, 190, 250, 280]), ("Dunesville", [14.0, 16.0, 19.0, 23.0, 26.0, 28.0, 29.0, 28.5, 26.5, 23.5, 19.0, 15.0], [5, 4, 3, 1, 1, 0, 0, 0, 0, 1, 3, 5]), ("Olive Bay", [8.0, 9.0, 11.0, 14.0, 18.0, 22.0, 25.0, 25.0, 22.0, 17.0, 12.0, 9.0], [80, 75, 65, 60, 35, 20, 10, 20, 70, 110, 110, 95]), ("Fogmoor", [5.0, 5.5, 7.0, 9.0, 12.0, 15.0, 17.0, 17.0, 14.5, 11.0, 7.5, 5.5], [55, 40, 42, 44, 49, 45, 45, 50, 49, 69, 59, 55]), ("Birchgrad", [-9.0, -8.0, -2.5, 6.0, 13.0, 17.0, 19.0, 17.0, 11.0, 5.0, -1.0, -6.0], [50, 40, 38, 36, 50, 80, 90, 80, 65, 60, 55, 50]), ("Ice Point", [-27.0, -28.0, -24.0, -16.0, -4.0, 4.0, 8.0, 7.0, 2.0, -7.0, -15.0, -23.0], [20, 18, 22, 28, 27, 35, 59, 70, 46, 36, 25, 18]), ("Monsoon Ford", [-4.0, -1.0, 6.0, 14.0, 20.0, 25.0, 26.5, 25.5, 20.5, 13.0, 4.5, -2.0], [3, 5, 9, 26, 29, 70, 180, 160, 50, 20, 9, 3]), ("Savanna Gate", [29.0, 28.5, 29.0, 29.5, 28.0, 26.0, 25.5, 26.5, 28.5, 30.0, 30.5, 30.0], [420, 360, 320, 100, 20, 2, 1, 3, 15, 70, 140, 250])]
for name, temp, rain in stations:
    total = sum(rain)
    warm = max(temp)
    cold = min(temp)
    print(f"{name:<13} {total:>5} mm, {cold:>5.1f} to {warm:>4.1f} C -> {classify(temp, rain)}")
