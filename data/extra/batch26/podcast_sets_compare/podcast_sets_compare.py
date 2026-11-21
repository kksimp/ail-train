ana = {"Tech Weekly", "Cooking Hour", "History Now", "Space Talk", "Daily Brief"}
ben = {"Daily Brief", "Space Talk", "True Crime Files", "Garden Chat"}
s = lambda x: ", ".join(sorted(x))
b = lambda v: "true" if v else "false"
print(f"both follow: {s(ana & ben)}")
print(f"suggest to Ben: {s(ana - ben)}")
print(f"suggest to Ana: {s(ben - ana)}")
print(f"{len(ana & ben)} of {len(ana | ben)} shows overlap")
fam = {"Daily Brief", "Space Talk"}
print(f"family plan fits Ana: {b(fam <= ana)}, Ben: {b(fam <= ben)}")
kids = {"Garden Chat", "Space Talk"}
print(f"kids plan fits Ana: {b(kids <= ana)}, Ben: {b(kids <= ben)}")
