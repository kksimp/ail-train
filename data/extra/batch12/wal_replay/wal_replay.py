log = [(1, "begin", "", 0, 0), (1, "set", "alice", 100, 70), (2, "begin", "", 0, 0), (1, "set", "bob", 50, 80), (2, "set", "carol", 20, 95), (1, "commit", "", 0, 0), (3, "begin", "", 0, 0), (3, "set", "alice", 70, 60), (2, "set", "bob", 80, 10), (3, "commit", "", 0, 0)]
disk = {"alice": 100, "bob": 80, "carol": 95}

def show(m):
    return "{" + ", ".join(f'"{k}": {v}' for k, v in m.items()) + "}"

print(f"disk after crash: {show(disk)}")
committed = [r[0] for r in log if r[1] == "commit"]
print(f"committed transactions: {committed}")
for tx, op, key, old, new in log:
    if op == "set" and tx in committed:
        disk[key] = new
        print(f"redo T{tx}: {key} = {new}")
i = len(log) - 1
while i >= 0:
    tx, op, key, old, new = log[i]
    if op == "set" and tx not in committed:
        disk[key] = old
        print(f"undo T{tx}: {key} = {old}")
    i -= 1
print(f"disk after recovery: {show(disk)}")
print(f"total money {sum(disk.values())}")
