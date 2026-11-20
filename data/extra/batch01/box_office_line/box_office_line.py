from collections import deque
line = deque()
events = ["join Ana", "join Ben", "book Cleo", "serve", "join Dev", "join Eve", "leave", "book Fin", "serve", "serve", "serve", "serve"]
served = []
for ev in events:
    parts = ev.split(" ")
    k = parts[0]
    if k == "join":
        line.append((parts[1], False))
    elif k == "book":
        line.appendleft((parts[1], True))
    elif k == "leave":
        if line:
            print(f"{line.pop()[0]} gave up")
        else:
            continue
    elif k == "serve":
        if not line:
            print("nobody to serve")
            continue
        c = line.popleft()
        print(f"served {c[0]}{' (booked)' if c[1] else ''}")
        served.append(c[0])
    print("  line: [" + " ".join(c[0] for c in line) + "]")
print("served in order: " + ", ".join(served))
