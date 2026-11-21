import json
ranks = {"Small": 1, "Medium": 2, "Large": 3}
lockers = [["A1", "Small", 0], ["A2", "Small", 0], ["B1", "Medium", 0], ["B2", "Medium", 0], ["C1", "Large", 0]]
seed = 4242
codes = {}
events = [("drop", "book", "Small"), ("drop", "shoes", "Medium"), ("drop", "lamp", "Large"), ("drop", "mug", "Small"), ("drop", "phone", "Small"), ("drop", "rug", "Large"), ("pick", "shoes", "Small"), ("drop", "rug", "Large"), ("drop", "kettle", "Medium")]
for kind, item, size in events:
    if kind == "drop":
        pick = -1
        for i in range(len(lockers)):
            if lockers[i][2] == 0 and ranks[lockers[i][1]] >= ranks[size]:
                if pick < 0 or ranks[lockers[i][1]] < ranks[lockers[pick][1]]:
                    pick = i
        if pick < 0:
            print(f"{item} (Size.{size}): no locker free")
            continue
        seed = (seed * 7919 + 13) % 9973
        code = 1000 + seed % 9000
        lockers[pick][2] = code
        codes[item] = code
        print(f"{item} (Size.{size}) -> {lockers[pick][0]}, code {code}")
    else:
        code = codes.get(item, -1)
        for l in lockers:
            if l[2] == code:
                l[2] = 0
                print(f"{item} picked up from {l[0]}")
busy = [l[0] for l in lockers if l[2] != 0]
print(f"busy: {json.dumps(busy)}")
