def expand(rank):
    out = []
    for c in rank:
        if c.isdigit():
            out.append("." * int(c))
        else:
            out.append(c)
    return "".join(out)

fen = "r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 4 4"
fields = fen.split(" ")
ranks = fields[0].split("/")
white = 0
black = 0
for i, r in enumerate(ranks):
    row = expand(r)
    print(f"{8 - i} {row}")
    for c in row:
        if c.isupper():
            white += 1
        elif c != '.':
            black += 1
print("  abcdefgh")
side = "white" if fields[1] == "w" else "black"
names = {'K': "white short", 'Q': "white long", 'k': "black short", 'q': "black long"}
rights = [names.get(c, "none") for c in fields[2]]
castles = ", ".join(rights)
print(f"{side} to move, move {fields[5]}; pieces {white} white, {black} black")
print(f"castling: {castles}")
