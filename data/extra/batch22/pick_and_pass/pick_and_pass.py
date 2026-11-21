def finish_times(lines):
    done = []
    for o in range(len(lines)):
        row = []
        for z in range(3):
            arrived = 0 if z == 0 else row[z - 1]
            freed = 0 if o == 0 else done[o - 1][z]
            row.append(max(arrived, freed) + lines[o][z])
        done.append(row)
    return done

lines = [[3, 1, 4], [2, 5, 1], [4, 2, 2], [1, 3, 5], [2, 2, 3]]
done = finish_times(lines)
for o in range(len(lines)):
    print(f"tote {o + 1}: lines {lines[o]}, leaves zones at {done[o]}")
last = done[-1][2]
for z in range(3):
    busy = sum(l[z] for l in lines)
    print(f"zone {z + 1}: busy {busy} of {last} minutes ({busy * 100 // last}%)")
