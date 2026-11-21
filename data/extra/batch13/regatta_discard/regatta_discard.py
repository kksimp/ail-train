boats = ["Petrel", "Skua", "Tern", "Gannet", "Fulmar"]
races = [[1, 3, 2, 5, 4], [2, 1, 4, 3, 0], [3, 2, 1, 4, 5], [1, 4, 0, 2, 3], [4, 1, 2, 3, 5], [2, 3, 1, 5, 4]]
fleet = len(boats)

def if_dnf(place, fleet):
    return fleet + 1 if place == 0 else place

nets = []
firsts = []
for b in range(fleet):
    scores = [if_dnf(r[b], fleet) for r in races]
    worst = max(scores)
    gross = sum(scores)
    nets.append(gross - worst)
    firsts.append(scores.count(1))
    shown = " ".join(str(s) for s in scores)
    print(f"{boats[b]:<7} {shown}  gross {gross:>2} drop {worst} net {gross - worst:>2}")
order = sorted([0, 1, 2, 3, 4], key=lambda b: (nets[b], -firsts[b]))
for place, b in enumerate(order):
    print(f"{place + 1}. {boats[b]} {nets[b]}")
