t = "AIL says hi!\tTabs & newlines\n."; b = [ord(c) for c in t]; o = 0
while o < len(b):
    h = []; s = ""
    for i in range(o, o + 8):
        if i < len(b): h.append(f"{b[i]:02x}"); s += chr(b[i]) if 32 <= b[i] < 127 else "."
        else: h.append("  ")
    print(f"{o:04x}: {' '.join(h)}  {s}"); o += 8
