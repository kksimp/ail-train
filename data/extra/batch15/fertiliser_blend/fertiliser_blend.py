import math
def bags(kg): return int(math.ceil(kg / 50.0))
need_n = 140.0; need_p = 60.0; need_k = 90.0; hectares = 12.0
dap = ("DAP 18-46-0", 0.18, 0.46, 0.0, 31.5)
urea = ("urea 46-0-0", 0.46, 0.0, 0.0, 24.0)
potash = ("potash 0-0-60", 0.0, 0.0, 0.6, 22.0)
dap_kg = need_p / dap[2]
urea_kg = (need_n - dap_kg * dap[1]) / urea[1]
potash_kg = need_k / potash[3]
cost = 0.0
for prod, per_ha in [(dap, dap_kg), (urea, urea_kg), (potash, potash_kg)]:
    field = per_ha * hectares
    b = bags(field)
    cost += float(b) * prod[4]
    print(f"{prod[0]:<14} {per_ha:>6.1f} kg/ha, {field:>7.1f} kg on the field = {b} bags")
applied = dap_kg * dap[1] + urea_kg * urea[1]
print(f"nitrogen applied {applied:.1f} kg/ha (need {need_n:.0f})")
print(f"cost {cost:.2f}, {cost / hectares:.2f} per hectare")
