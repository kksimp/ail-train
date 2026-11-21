def burn(errors, requests):
    return float(errors * 200) / float(requests)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
requests = [12000, 15000, 11000, 18000, 16000, 9000, 14000]
errors = [20, 45, 30, 250, 72, 12, 40]
total = sum(requests)
allowed = total * 5 // 1000
print(f"{total} requests allow {allowed} errors")
used = 0
hot = []
for i in range(len(days)):
    used += errors[i]
    rate = burn(errors[i], requests[i])
    pct = float(used * 100) / float(allowed)
    print(f"{days[i]} {requests[i]:>6} req {errors[i]:>4} err  burn {rate:>4.2f}  used {pct:>5.1f}%")
    if rate > 2.0:
        hot.append(days[i])
print(f"remaining budget: {allowed - used} errors")
print(f"days burning over 2x: {', '.join(hot)}")
