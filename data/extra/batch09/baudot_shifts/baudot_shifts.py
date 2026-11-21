TABLES = {"L": "~E~A SIU~DRJNFCKTZLWHYPQOBG~MXV~", "F": "~3~- '87~$4~,!:(5+)2#6019?&~./=~"}

def encode(text):
    mode = "L"
    out = [31]
    for c in text:
        if c == ' ':
            out.append(4)
            continue
        at = TABLES[mode].find(c)
        if at < 0:
            mode = "F" if mode == "L" else "L"
            out.append(27 if mode == "F" else 31)
            at = TABLES[mode].find(c)
        out.append(at)
    return out

def decode(codes):
    mode = "L"
    out = []
    for c in codes:
        if c == 27:
            mode = "F"
        elif c == 31:
            mode = "L"
        else:
            out.append(TABLES[mode][c])
    return "".join(out)

for msg in ["CALL 999 NOW", "ROOM 12B AT 3", "HELLO WORLD", "PI=3.14"]:
    codes = encode(msg)
    shifts = sum(1 for c in codes if c == 27 or c == 31)
    print(f"{msg:<14} {len(codes):>2} codes ({shifts} shifts), back '{decode(codes)}'")
first = " ".join(f"{c:05b}" for c in encode("A1"))
print(f"A1 on tape: {first}")
