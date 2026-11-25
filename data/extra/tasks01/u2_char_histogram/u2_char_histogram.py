import sys

def main():
    text = sys.stdin.read()
    if text == "":
        print("no input")
        return
    names = ["upper", "lower", "digit", "space", "newline", "punct", "other"]
    cnt = {n: 0 for n in names}
    for ch in text:
        o = ord(ch)
        if "A" <= ch <= "Z":
            cnt["upper"] += 1
        elif "a" <= ch <= "z":
            cnt["lower"] += 1
        elif "0" <= ch <= "9":
            cnt["digit"] += 1
        elif ch == " " or ch == "\t":
            cnt["space"] += 1
        elif ch == "\n":
            cnt["newline"] += 1
        elif 33 <= o <= 126:
            cnt["punct"] += 1
        else:
            cnt["other"] += 1
    m = max(cnt.values())
    for n in names:
        c = cnt[n]
        line = f"{n:<8}{c:>4}"
        if c > 0:
            line += " " + "#" * ((c * 20 + m - 1) // m)
        print(line)
    print(f"total={len(text)}")

main()
