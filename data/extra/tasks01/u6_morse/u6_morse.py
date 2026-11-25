import sys

CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
CODES = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
         "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
         "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
ENC = dict(zip(CHARS, CODES))
DEC = dict(zip(CODES, CHARS))


def main():
    for line in sys.stdin.read().split("\n"):
        if line == "":
            continue
        parts = line.split(" ", 1)
        arg = parts[1] if len(parts) > 1 else ""
        if parts[0] == "enc":
            words = [w for w in arg.split(" ") if w != ""]
            try:
                print(" / ".join(" ".join(ENC[c.upper()] for c in w) for w in words))
            except KeyError:
                print("error")
        elif parts[0] == "dec":
            out = []
            ok = True
            for tok in [t for t in arg.split(" ") if t != ""]:
                if tok == "/":
                    out.append(" ")
                elif tok in DEC:
                    out.append(DEC[tok])
                else:
                    ok = False
                    break
            print("".join(out) if ok else "error")
        else:
            print("bad command")


main()
