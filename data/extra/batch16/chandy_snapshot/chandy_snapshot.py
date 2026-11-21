names = ["P", "Q"]
bal = [100, 50]
chans = [[], []]
rec = [-1, -1]
recording = [False, False]
in_flight = [[], []]

def record(p):
    rec[p] = bal[p]
    chans[p].append(-1)
    recording[1 - p] = True

events = [["send", "0", "10"], ["send", "1", "5"], ["snap", "0", "0"], ["recv", "0", "0"], ["recv", "1", "0"], ["send", "1", "20"], ["recv", "0", "0"], ["recv", "1", "0"], ["recv", "1", "0"]]
for ev in events:
    x = int(ev[1])
    if ev[0] == "send":
        amt = int(ev[2])
        bal[x] -= amt
        chans[x].append(amt)
        print(f"{names[x]} sends {amt}")
    elif ev[0] == "snap":
        record(x)
        print(f"{names[x]} starts the snapshot, records {bal[x]}")
    else:
        msg = chans[x][0]
        chans[x] = chans[x][1:]
        q = 1 - x
        if msg < 0:
            if rec[q] < 0:
                record(q)
                print(f"{names[q]} gets its first marker, records {bal[q]}")
            else:
                print(f"{names[q]} gets the marker back, stops recording")
            recording[x] = False
        else:
            bal[q] += msg
            if recording[x]:
                in_flight[x].append(msg)
            print(f"{names[q]} receives {msg}")
flight = sum(in_flight[0]) + sum(in_flight[1])
print(f"snapshot: P={rec[0]} Q={rec[1]} in flight P>Q {in_flight[0]} Q>P {in_flight[1]}")
print(f"snapshot total {rec[0] + rec[1] + flight}, real total {bal[0] + bal[1]}")
