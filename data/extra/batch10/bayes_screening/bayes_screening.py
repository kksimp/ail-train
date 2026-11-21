def posterior(prior, sens, spec):
    hit = sens * prior
    false_alarm = (1.0 - spec) * (1.0 - prior)
    return hit / (hit + false_alarm)

sens, spec = 0.9, 0.95
print("sensitivity 90%, specificity 95%")
for prev in [0.001, 0.01, 0.05, 0.2, 0.5]:
    p = posterior(prev, sens, spec)
    again = posterior(p, sens, spec)
    pct = prev * 100.0
    print(f"prevalence {pct:>5.1f}%: one positive {p * 100.0:>5.1f}%, two positives {again * 100.0:>5.1f}%")
people = 100000
sick = people // 100
true_pos = sick * 90 // 100
false_pos = (people - sick) * 5 // 100
print(f"of {people} people with 1% sick: {true_pos} true and {false_pos} false positives")
