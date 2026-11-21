L = "abcdefghijklmnopqrstuvwxyz"
C = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
t = dict(zip(L, C)); b = {v: k for k, v in t.items()}
enc = lambda s: " / ".join(" ".join(t.get(c, "?") for c in w) for w in s.lower().split(" "))
dec = lambda m: " ".join("".join(b.get(x, "?") for x in w.split(" ")) for w in m.split(" / "))
for msg in ["SOS", "hello world", "ail is here"]:
    m = enc(msg); print(f"{msg} -> {m}"); print(f"  back: {dec(m)}")
