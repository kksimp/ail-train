drivers = [(0, 3, 50), (2, 3, 30), (5, 4, 60), (7, 3, 40), (9, 12, 20), (12, 3, 45), (15, 18, 25), (20, 4, 30), (33, 3, 30), (40, 19, 15)]
free_at = [0] * 20
walked = 0
for i, (arrive, dest, stay) in enumerate(drivers):
    k = 0
    while free_at[(dest + k) % 20] > arrive: k += 1
    spot = (dest + k) % 20
    free_at[spot] = arrive + stay
    walked += k
    print(f"driver {i + 1:>2} (minute {arrive:>2}) for space {dest:>2}: parks at {spot:>2}, walks back {k}")
print(f"mean walk {walked / len(drivers):.1f} spaces")
