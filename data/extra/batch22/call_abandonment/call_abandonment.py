calls = [(0, 60, 180), (10, 30, 240), (25, 45, 120), (40, 90, 200), (55, 20, 150), (70, 120, 90), (95, 40, 160), (130, 25, 100), (150, 200, 140), (175, 15, 110), (240, 60, 130), (300, 30, 90)]
agents = [0, 0]
answered = 0
quick = 0
gave_up = 0
for i, (arrive, patience, talk) in enumerate(calls):
    a = 0 if agents[0] <= agents[1] else 1
    start = max(arrive, agents[a])
    wait = start - arrive
    if wait > patience:
        gave_up += 1
        print(f"call {i + 1:>2} at {arrive:>3}s: would wait {wait}s, hangs up after {patience}s")
        continue
    agents[a] = start + talk
    answered += 1
    if wait <= 20:
        quick += 1
    print(f"call {i + 1:>2} at {arrive:>3}s: agent {a + 1} answers after {wait}s")
n = len(calls)
print(f"answered {answered}, abandoned {gave_up} ({gave_up * 100 // n}%), within 20 s {quick * 100 // n}% of calls")
