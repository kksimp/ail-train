def filled(x, y, z, level):
    a, b, c = x, y, z
    for i in range(level):
        ones = len([d for d in [a % 3, b % 3, c % 3] if d == 1])
        if ones >= 2:
            return False
        a //= 3
        b //= 3
        c //= 3
    return True
print("level  cubes   volume  surface")
for n in range(5):
    f = float(n)
    a, b, c = 20.0 / 27.0, 20.0 / 9.0, 8.0 / 9.0
    cubes = 20 ** n
    surf = 2.0 * b ** f + 4.0 * c ** f
    print(f"{n:>5} {cubes:>6} {a ** f:>8.4f} {surf:>8.4f}")
side = 9
count = faces = 0
dirs = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
for x in range(side):
    for y in range(side):
        for z in range(side):
            if filled(x, y, z, 2):
                count += 1
                for d in dirs:
                    nx, ny, nz = x + d[0], y + d[1], z + d[2]
                    outside = nx < 0 or ny < 0 or nz < 0 or nx >= side or ny >= side or nz >= side
                    if outside or not filled(nx, ny, nz, 2):
                        faces += 1
print(f"voxel check, level 2: {count} cubes, {faces} faces of area 1/81 = {faces // 81} + {faces % 81}/81")
