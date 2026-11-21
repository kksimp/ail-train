def submerged(obj, liquid):
    if obj >= liquid:
        return None
    return obj / liquid
things = [("ice", 917.0), ("oak", 750.0), ("pine", 500.0), ("cork", 240.0), ("aluminium", 2700.0), ("candle wax", 900.0)]
for lname, rho in [("fresh water", 1000.0), ("sea water", 1025.0)]:
    print(f"{lname}:")
    for name, dens in things:
        share = submerged(dens, rho)
        if share is not None:
            above = (1.0 - share) * 100.0
            print(f"  {name:<10} floats, {share * 100.0:.1f}% under, {above:.1f}% above")
        else:
            print(f"  {name:<10} sinks")
raft = 8.0 * 0.2 * 0.2 * 3.0
load = raft * (1000.0 - 500.0)
print(f"a raft of 8 pine logs (0.2 x 0.2 x 3 m) carries up to {load:.1f} kg")
