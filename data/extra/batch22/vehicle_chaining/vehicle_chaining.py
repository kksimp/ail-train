places = ["Airport", "Bay", "City"]
empty = [[0, 20, 30], [20, 0, 15], [30, 15, 0]]
trips = [("T1", 360, 430, 0, 1), ("T2", 390, 440, 1, 2), ("T3", 450, 520, 1, 0), ("T4", 460, 510, 2, 0), ("T5", 480, 540, 0, 2), ("T6", 540, 610, 0, 1), ("T7", 550, 590, 2, 1), ("T8", 630, 680, 1, 2)]

def clock(m):
    return f"{m // 60:02d}:{m % 60:02d}"

free_at = []
place = []
chains = []
for tid, start, finish, origin, dest in trips:
    bus = -1
    for b in range(len(free_at)):
        if bus == -1 and free_at[b] + empty[place[b]][origin] <= start:
            bus = b
    if bus == -1:
        bus = len(free_at)
        free_at.append(0)
        place.append(origin)
        chains.append([])
    free_at[bus] = finish
    place[bus] = dest
    chains[bus].append(tid)
    print(f"{tid} {clock(start)} {places[origin]} -> {places[dest]}: bus {bus + 1}")
for b in range(len(chains)):
    print(f"bus {b + 1}: {' '.join(chains[b])}")
