import json
MISSING = -999
data = {}
undo = []

def set_(k, v):
    if len(undo) > 0:
        if k not in undo[-1]:
            undo[-1][k] = data.get(k, MISSING)
    data[k] = v

def rollback():
    if not undo:
        return "NO TRANSACTION"
    level = undo.pop()
    for k, old in level.items():
        if old == MISSING:
            del data[k]
        else:
            data[k] = old
    return f"rolled back {len(level)} keys"

script = ["SET a 10", "BEGIN", "SET a 20", "SET b 5", "BEGIN", "SET a 30", "GET a", "ROLLBACK", "GET a", "GET b", "ROLLBACK", "GET a", "GET b", "ROLLBACK", "BEGIN", "SET c 1", "COMMIT", "GET c"]
for line in script:
    p = line.split(" ")
    if p[0] == "SET":
        set_(p[1], int(p[2]))
    elif p[0] == "GET":
        v = data.get(p[1])
        shown = "NULL" if v is None else f"{v}"
        print(f"{line} -> {shown}")
    elif p[0] == "BEGIN":
        undo.append({})
    elif p[0] == "ROLLBACK":
        print(f"{line} -> {rollback()}")
    else:
        undo = []
print(f"open levels: {len(undo)}, keys: {json.dumps(sorted(data.keys()))}")
