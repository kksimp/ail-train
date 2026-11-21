import math
def rate_ratio(ea, t1_c, t2_c):
    t1 = t1_c + 273.15
    t2 = t2_c + 273.15
    return math.exp(ea / 8.314 * (1.0 / t1 - 1.0 / t2))
ea = 80000.0
for temp in [0.0, 4.0, 8.0, 12.0, 20.0, 30.0]:
    ratio = rate_ratio(ea, 4.0, temp)
    days = 10.0 / ratio
    hours = days * 24.0
    print(f"{temp:>4.1f} C: {ratio:>6.2f} times the fridge rate, lasts {days:>5.2f} days ({hours:.1f} h)")
two = 2.0
doubling_ea = 8.314 * math.log(two) / (1.0 / 293.15 - 1.0 / 303.15)
print(f"a rate that doubles from 20 C to 30 C has Ea = {doubling_ea / 1000.0:.1f} kJ/mol")
