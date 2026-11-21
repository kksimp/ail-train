text = "Dr. Hale met Mr. Ruiz on St. Ann's road. They talked! Was it about bees, flowers etc. or the weather? Nobody knows. trailing words"
ab = ["dr", "mr", "mrs", "st", "e.g", "etc"]
out = []; st = 0
for i, c in enumerate(text):
    if c in ".!?":
        if not (i + 1 == len(text) or text[i + 1] == " "): continue
        pc = text[st:i + 1].strip(); lw = pc.split(" ")[-1].lower()
        if c == "." and lw[:-1] in ab: continue
        out.append(pc); st = i + 1
r = text[st:].strip()
if r: out.append(r)
for s in out: print(f"[{len(s.split(' '))}] {s}")
