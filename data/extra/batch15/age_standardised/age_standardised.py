def crude(t): return float(sum(t[1])) / float(sum(t[2])) * 100000.0
def standardised(t, standard):
    expected = 0.0
    for i in range(len(standard)):
        rate = float(t[1][i]) / float(t[2][i])
        expected += rate * float(standard[i])
    return expected / float(sum(standard)) * 100000.0
bands = ["0-39", "40-64", "65-79", "80+"]
standard = [50000, 32000, 13000, 5000]
towns = [("Seaview", [8, 60, 210, 390], [18000, 16000, 12000, 6000]), ("Newfield", [22, 95, 120, 140], [52000, 30000, 8000, 2000])]
print(f"age bands {', '.join(bands)}")
for t in towns:
    c = crude(t); s = standardised(t, standard)
    print(f"{t[0]:<9} crude {c:>6.1f}, standardised {s:>6.1f} per 100,000")
a = standardised(towns[0], standard); b = standardised(towns[1], standard)
print(f"standardised ratio Seaview / Newfield: {a / b:.2f}")
