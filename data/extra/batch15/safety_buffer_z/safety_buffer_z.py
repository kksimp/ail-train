import math
def buffer(z, sd, lead, mean, sdl): return math.sqrt(lead * sd * sd + mean * mean * sdl * sdl) * z
mean = 40.0; sd = 12.0; lead = 9.0
print(f"daily demand {mean:.0f} (sd {sd:.0f}), lead time {lead:.0f} days")
for name, z in [("90%", 1.2816), ("95%", 1.6449), ("98%", 2.0537), ("99%", 2.3263)]:
    fixed = buffer(z, sd, lead, mean, 0.0)
    shaky = buffer(z, sd, lead, mean, 2.0)
    rop = mean * lead + fixed
    print(f"service {name}: buffer {fixed:>5.1f} units (reorder at {rop:.0f}), with lead time sd 2 days {shaky:>6.1f}")
c95 = buffer(1.6449, sd, lead, mean, 0.0)
c99 = buffer(2.3263, sd, lead, mean, 0.0)
print(f"going from 95% to 99% adds {(c99 / c95 - 1.0) * 100.0:.0f}% more buffer")
