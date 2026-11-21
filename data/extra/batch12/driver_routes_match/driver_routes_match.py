def try_route(r, can, seen, owner):
    for d in can[r]:
        if not seen[d]:
            seen[d] = True
            cur = owner[d]
            if cur < 0 or try_route(cur, can, seen, owner):
                owner[d] = r
                return True
    return False

routes = ["North loop", "Harbour", "Airport", "Old town", "Ring road"]
drivers = ["Ana", "Bo", "Cy", "Dev", "Eli", "Fay"]
can = [[0, 1], [0], [1, 2, 3], [2], [3, 4]]
owner = [-1] * 6
matched = 0
for r in range(len(routes)):
    seen = [False] * 6
    if try_route(r, can, seen, owner):
        matched += 1
        print(f"{routes[r]:<11} matched, drivers now {owner}")
    else:
        print(f"{routes[r]:<11} has no free driver")
for d in range(len(drivers)):
    if owner[d] >= 0:
        print(f"{drivers[d]} drives {routes[owner[d]]}")
    else:
        print(f"{drivers[d]} is spare")
print(f"{matched} of {len(routes)} routes covered")
