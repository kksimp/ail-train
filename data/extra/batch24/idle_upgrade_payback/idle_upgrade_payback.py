def race(best_payback, show):
    ups = [["cart", 15, 1], ["mill", 100, 8], ["mine", 1100, 50]]
    gold = 0; income = 1; bought = 0; second = 0
    while gold < 20000:
        second += 1
        gold += income
        while True:
            pick = 0
            for i in range(1, 3):
                if best_payback:
                    if ups[i][1] * ups[pick][2] < ups[pick][1] * ups[i][2]: pick = i
                elif ups[i][1] < ups[pick][1]: pick = i
            if ups[pick][1] > gold: break
            gold -= ups[pick][1]
            income += ups[pick][2]
            bought += 1
            if show and bought <= 5:
                print(f"  second {second:>3}: buy {ups[pick][0]} for {ups[pick][1]}, income now {income}")
            ups[pick][1] = ups[pick][1] * 115 // 100
    return [second, bought, income]
print("saving for best payback:")
a = race(True, True)
b = race(False, False)
print(f"best payback reaches 20000 gold in {a[0]} s ({a[1]} upgrades, income {a[2]}/s)")
print(f"cheapest first reaches it in {b[0]} s ({b[1]} upgrades, income {b[2]}/s)")
