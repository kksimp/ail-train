pay = 4200
lines = [("rent", 1500, "Need"), ("groceries", 450, "Need"), ("transport", 180, "Need"), ("utilities", 160, "Need"), ("insurance", 120, "Need"), ("dining out", 320, "Want"), ("streaming", 40, "Want"), ("clothes", 150, "Want"), ("hobbies", 210, "Want"), ("pension top-up", 300, "Save"), ("emergency fund", 200, "Save")]
targets = {"Need": 50, "Want": 30, "Save": 20}
spent = sum(l[1] for l in lines)
for k in ["Need", "Want", "Save"]:
    total = sum(l[1] for l in lines if l[2] == k)
    if k == "Save":
        total += pay - spent
    share = total * 1000 // pay
    goal = targets[k] * pay // 100
    if k == "Save" and total < goal:
        flag = "under target"
    elif k != "Save" and total > goal:
        flag = "over target"
    else:
        flag = "ok"
    print(f"{k:<4} {total:>5} = {share // 10}.{share % 10}% (target {targets[k]}%, {goal}): {flag}")
print(f"left unspent: {pay - spent}")
