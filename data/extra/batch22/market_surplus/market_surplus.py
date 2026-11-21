def trades(values, costs, floor):
    n = 0
    while n < len(values) and n < len(costs) and values[n] >= costs[n] and values[n] >= floor:
        n += 1
    return n

values = sorted([40, 90, 60, 75, 30, 80, 50])[::-1]
costs = sorted([55, 20, 85, 45, 65, 30, 70])
n = trades(values, costs, 0)
low = max(costs[n - 1], values[n])
high = min(values[n - 1], costs[n])
price = (low + high) // 2
cs = 0
ps = 0
for i in range(n):
    cs += values[i] - price
    ps += price - costs[i]
    print(f"trade {i + 1}: buyer worth {values[i]}, seller cost {costs[i]}")
print(f"{n} trades, price range {low}-{high}, at {price}: consumer surplus {cs}, producer surplus {ps}, total {cs + ps}")
m = trades(values, costs, 70)
fcs = sum(values[i] - 70 for i in range(m))
fps = sum(70 - costs[i] for i in range(m))
print(f"floor 70: {m} trades, consumer {fcs}, producer {fps}, total {fcs + fps}, lost {cs + ps - fcs - fps}")
