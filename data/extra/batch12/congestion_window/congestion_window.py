events = {8: "DupAcks", 12: "Timeout"}

def step(cwnd, ssthresh, ev):
    if ev == "DupAcks":
        return [max(cwnd // 2, 2), max(cwnd // 2, 2)]
    if ev == "Timeout":
        return [1, max(cwnd // 2, 2)]
    if cwnd < ssthresh:
        return [min(cwnd * 2, ssthresh), ssthresh]
    return [cwnd + 1, ssthresh]

cwnd = 1
ssthresh = 16
for rtt in range(1, 16):
    ev = events.get(rtt, "NoLoss")
    bar = "#" * cwnd
    note = "" if ev == "NoLoss" else f" Loss.{ev}"
    print(f"{rtt:>2} {cwnd:>2} {bar}{note}")
    r = step(cwnd, ssthresh, ev)
    cwnd = r[0]
    ssthresh = r[1]
