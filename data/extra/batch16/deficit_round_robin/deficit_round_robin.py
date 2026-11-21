names = ["A", "B", "C"]
queues = [[500, 500, 500], [200, 200, 200, 200, 200], [1000, 100]]
quantum = 300
head = [0, 0, 0]
deficit = [0, 0, 0]
sent = [0, 0, 0]
rnd = 0
while any(head[f] < len(queues[f]) for f in range(3)):
    rnd += 1
    log = []
    for f in range(3):
        if head[f] >= len(queues[f]):
            continue
        deficit[f] += quantum
        while head[f] < len(queues[f]) and queues[f][head[f]] <= deficit[f]:
            size = queues[f][head[f]]
            deficit[f] -= size
            sent[f] += size
            head[f] += 1
            log.append(f"{names[f]}{size}")
        if head[f] >= len(queues[f]):
            deficit[f] = 0
    shown = "-" if not log else " ".join(log)
    print(f"round {rnd}: {shown:<20} credit {deficit}")
for f in range(3):
    print(f"flow {names[f]} sent {sent[f]} bytes")
