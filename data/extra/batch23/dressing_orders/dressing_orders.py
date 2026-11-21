def count_orders(n, pre):
    total = 1 << n
    dp = [0] * total
    dp[0] = 1
    for mask in range(total):
        if dp[mask] > 0:
            for v in range(n):
                bit = 1 << v
                if (mask & bit) == 0 and (pre[v] & mask) == pre[v]:
                    dp[mask | bit] += dp[mask]
    return dp[total - 1]

def needs(names, rules):
    pre = [0] * len(names)
    for r in rules:
        a = names.index(r[0])
        b = names.index(r[1])
        pre[b] = pre[b] | (1 << a)
    return pre

names = ["vest", "shirt", "tie", "jacket", "pants", "belt", "socks", "shoes", "watch"]
rules = []
print(f"no rules: {count_orders(len(names), needs(names, rules))} orders")
for r in [["vest", "shirt"], ["shirt", "tie"], ["tie", "jacket"], ["shirt", "belt"], ["pants", "belt"], ["belt", "jacket"], ["pants", "shoes"], ["socks", "shoes"], ["shirt", "watch"]]:
    rules.append(r)
    c = count_orders(len(names), needs(names, rules))
    print(f"+ {r[0]} before {r[1]}: {c} orders")
