import math

def erf(x):
    sign = -1.0 if x < 0.0 else 1.0
    ax = abs(x)
    t = 1.0 / (1.0 + 0.3275911 * ax)
    poly = ((((1.061405429 * t - 1.453152027) * t + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t
    return sign * (1.0 - poly * math.exp(-ax * ax))

def cdf(z):
    return 0.5 * (1.0 + erf(z / math.sqrt(2.0)))

for k in [1.0, 2.0, 3.0]:
    inside = cdf(k) - cdf(-k)
    print(f"within {k:.0f} sd: {inside * 100.0:.2f}%")
for z in [-1.645, 0.0, 1.282, 1.96, 2.576]:
    print(f"P(Z < {z:>6.3f}) = {cdf(z):.4f}")
mean = 170.0
sd = 7.5
lo = 160.0
hi = 185.0
share = cdf((hi - mean) / sd) - cdf((lo - mean) / sd)
print(f"heights mean {mean:.0f} cm, sd {sd:.1f}: between {lo:.0f} and {hi:.0f} cm {share * 100.0:.1f}%")
