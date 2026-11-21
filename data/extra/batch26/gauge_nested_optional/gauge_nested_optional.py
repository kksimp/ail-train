gauges = [("north", [5, None, 2]), ("south", [4, None]), ("west", [6, None, None, 7]), ("east", [])]
def describe(name, xs):
    if xs:
        if xs[-1] is None:
            return f"{name}: last report missing"
        return f"{name}: {xs[-1]} mm"
    return f"{name}: never reported"
for name, xs in gauges:
    got = sum(1 for x in xs if x is not None)
    tot = sum(x for x in xs if x is not None)
    print(f"{describe(name, xs)} ({got} of {len(xs)} reports, {tot} mm in all)")
print(f"missed reports: {sum(1 for _, xs in gauges for x in xs if x is None)}")
