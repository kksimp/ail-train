text = "# settings\nHOST=localhost\nPORT = 5432\n\nNAME=\"my app\"\nGREETING='hi there'\nDB_HOST=$HOST\nbroken line\nMISSING=$NOPE\n=novalue"
def uq(v):
    if len(v) >= 2 and ((v[0] == v[-1] == '"') or (v[0] == v[-1] == "'")): return v[1:-1]
    return v
env = {}
for i, raw in enumerate(text.split("\n")):
    l = raw.strip()
    if not l or l.startswith("#"): continue
    e = l.find("=")
    if e <= 0: print(f'line {i + 1}: cannot read "{l}"'); continue
    k = l[:e].strip(); v = uq(l[e + 1:].strip())
    if v.startswith("$"): v = env.get(v[1:], "")
    env[k] = v
for k in env: print(f"{k}=[{env[k]}]")
