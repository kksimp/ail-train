def cost(score):
    if score < 8 or score > 15:
        return None, f"score {score} out of 8..15"
    return (score - 8 if score <= 13 else 5 + (score - 13) * 2), None

def signed(n):
    return f"+{n}" if n >= 0 else f"{n}"

def check(scores):
    spent = 0
    for s in scores:
        c, err = cost(s)
        if err:
            return None, err
        spent += c
    if spent > 27:
        return None, f"costs {spent}, over the budget of 27"
    return spent, None

abilities = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
builds = [("fighter", [15, 13, 14, 8, 12, 10], [2, 0, 1, 0, 0, 0]), ("wizard", [8, 14, 14, 15, 12, 8], [0, 0, 1, 2, 0, 0]), ("greedy", [15, 15, 15, 10, 8, 8], [0, 0, 0, 0, 0, 0]), ("odd", [16, 12, 12, 12, 12, 8], [0, 0, 0, 0, 0, 0])]
for name, scores, bonus in builds:
    spent, err = check(scores)
    if err is None:
        parts = []
        for i in range(6):
            total = scores[i] + bonus[i]
            parts.append(f"{abilities[i]} {total}({signed(total // 2 - 5)})")
        shown = " ".join(parts)
        print(f"{name:<8} {spent:>2} pts: {shown}")
    else:
        print(f"{name:<8} invalid: {err}")
