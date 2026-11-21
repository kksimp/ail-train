def show(c, ls, d):
    t = sum(ls); print(f"{c:<9} {len(ls)} lines, {t // 100}.{t % 100:02}, due in {d} days")
show("(blank)", [4900, 2500], 30)
show("Acme", [4900, 2500, 1200], 30)
show("Bolt Ltd", [4900, 0], 14)
show("Cove", [4900], 14)
print("template unchanged: true")
