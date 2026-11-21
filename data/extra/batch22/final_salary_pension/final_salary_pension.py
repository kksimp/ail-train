def best_three(pay):
    return max(sum(pay[i:i + 3]) for i in range(len(pay) - 2)) // 3

def pension(avg, service, age):
    full = service * avg // 60
    return full * (100 - 4 * (65 - age)) // 100

salaries = [41000, 42500, 44000, 47000, 46000, 48500, 50000, 49000, 51500, 50500]
avg = best_three(salaries)
print(f"best three-year average {avg}")
for age in range(60, 66):
    service = age - 33
    print(f"retire at {age}: {service} years, pension {pension(avg, service, age)} a year")
p65 = pension(avg, 32, 65)
given = p65 // 4
print(f"at 65: keep {p65 - given} a year and take {given * 12} as cash")
