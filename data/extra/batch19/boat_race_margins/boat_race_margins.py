def ways(t, record):
    return sum(1 for h in range(t + 1) if h * (t - h) > record)

times = "Time:      8   19   27   41"
records = "Record:    12  70   150  380"
ts = [int(w) for w in times.split(":")[1].split()]
rs = [int(w) for w in records.split(":")[1].split()]
product = 1
for i in range(len(ts)):
    k = ways(ts[i], rs[i])
    print(f"race of {ts[i]} s, record {rs[i]}: {k} ways")
    product *= k
print(f"part 1: product {product}")
bt = int("".join(times.split(":")[1].split()))
br = int("".join(records.split(":")[1].split()))
print(f"part 2: race of {bt} s, record {br}: {ways(bt, br)} ways")
