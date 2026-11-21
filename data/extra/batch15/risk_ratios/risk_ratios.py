import math
def rr(t):
    r1 = float(t[1]) / float(t[1] + t[2])
    r0 = float(t[3]) / float(t[3] + t[4])
    return r1 / r0
def orr(t): return float(t[1] * t[4]) / float(t[2] * t[3])
def interval(t):
    se = math.sqrt(1.0 / float(t[1]) + 1.0 / float(t[2]) + 1.0 / float(t[3]) + 1.0 / float(t[4]))
    l = math.log(orr(t))
    return [math.exp(l - 1.96 * se), math.exp(l + 1.96 * se)]
for t in [("smoking / bronchitis", 84, 316, 41, 559), ("night shifts / ulcer", 22, 178, 19, 181), ("helmet / head injury", 17, 983, 52, 948)]:
    ci = interval(t)
    sig = "significant" if ci[0] > 1.0 or ci[1] < 1.0 else "not significant"
    print(f"{t[0]}: RR {rr(t):.2f}, OR {orr(t):.2f} (95% CI {ci[0]:.2f} to {ci[1]:.2f}), {sig}")
