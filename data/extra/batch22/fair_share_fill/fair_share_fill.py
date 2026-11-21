def fair(demand, supply):
    n = len(demand)
    got = [0] * n
    done = [False] * n
    left = supply
    active = n
    while active > 0:
        share = left // active
        settled = 0
        for i in range(n):
            if not done[i] and demand[i] <= share:
                got[i] = demand[i]
                left -= demand[i]
                done[i] = True
                settled += 1
        if settled == 0:
            extra = left % active
            for i in range(n):
                if not done[i]:
                    got[i] = share
                    if extra > 0:
                        got[i] += 1
                        extra -= 1
            left = 0
            active = 0
        else:
            active -= settled
    return got

stores = ["north", "south", "east", "west", "centre"]
demand = [10, 40, 25, 60, 30]
shares = fair(demand, 100)
total = sum(demand)
for i in range(len(stores)):
    prop = 100 * demand[i] // total
    print(f"{stores[i]:<6} asks {demand[i]:>2}: fair share {shares[i]:>2}, proportional {prop:>2}")
print(f"asked {total}, shared {sum(shares)}")
