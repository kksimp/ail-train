class Name:
    def __init__(self, title, first, middle, last, suffix):
        self.title, self.first, self.middle, self.last, self.suffix = title, first, middle, last, suffix

def parse_name(raw):
    titles = ["Dr.", "Mr.", "Ms.", "Mrs.", "Prof."]
    suffixes = ["Jr.", "Sr.", "II", "III", "PhD"]
    text = raw.strip()
    if "," in text:
        halves = text.split(",")
        text = f"{halves[1].strip()} {halves[0].strip()}"
    words = text.split()
    title = ""
    suffix = ""
    if len(words) > 1 and words[0] in titles:
        title = words[0]
        words = words[1:]
    if len(words) > 1 and words[-1] in suffixes:
        suffix = words[-1]
        words = words[:-1]
    if len(words) == 1:
        return Name(title, words[0], "", "", suffix)
    middle = " ".join(words[1:-1])
    return Name(title, words[0], middle, words[-1], suffix)

def show(v):
    return "-" if v == "" else v

raw_names = ["Dr. Martin Luther King Jr.", "Hopper, Grace Brewster", "Prof. Ada Lovelace", "Cher", "Mr. John Ronald Reuel Tolkien III", "  Turing,  Alan  "]
print(f"{'title':<6} {'first':<7} {'middle':<13} {'last':<9} suffix")
for r in raw_names:
    n = parse_name(r)
    print(f"{show(n.title):<6} {n.first:<7} {show(n.middle):<13} {show(n.last):<9} {show(n.suffix)}")
