def premiums(q, years, rate, cover):
    v = 1.0 / (1.0 + rate)
    alive = 1.0; disc = 1.0; single = 0.0; annuity = 0.0
    for k in range(years):
        annuity += disc * alive
        single += disc * v * alive * q[k] * cover
        alive = alive * (1.0 - q[k])
        disc = disc * v
    return [single, single / annuity]
q = [0.00102, 0.00110, 0.0012, 0.00131, 0.00144, 0.00158, 0.00174, 0.00192, 0.00213, 0.00236]
cover = 250000.0
for years in [5, 10]:
    for rate in [0.02, 0.04]:
        p = premiums(q, years, rate, cover)
        print(f"{years:>2}-year term from age 40 at {rate * 100.0:.0f}%: single {p[0]:>8.2f}, yearly {p[1]:>7.2f}")
deaths = 0.0
for x in q: deaths = deaths + x
print(f"rough 10-year death chance {deaths * 100.0:.2f}%")
