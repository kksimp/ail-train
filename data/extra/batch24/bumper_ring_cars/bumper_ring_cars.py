dist = [0, 250, 500, 750]
speed = [9, 4, 6, 2]
bumps = 0
for tick in range(1, 601):
    for i in range(4): dist[i] += speed[i]
    for i in range(4):
        j = (i + 1) % 4
        ahead = dist[j] + 1000 if j == 0 else dist[j]
        if dist[i] >= ahead:
            speed[i], speed[j] = speed[j], speed[i]
            dist[i] = ahead - 1
            bumps += 1
    if tick % 150 == 0:
        print(f"after {tick // 10} s: speeds {speed}, {bumps} bumps so far")
for i in range(4):
    driven = dist[i] - 250 * i
    print(f"car {i + 1}: {driven // 10} m driven, {driven // 1000} full laps")
