class Query:
    def __init__(self, words, phrases, excluded, tags):
        self.words, self.phrases, self.excluded, self.tags = words, phrases, excluded, tags

def parse(q):
    words, phrases, excluded, tags = [], [], [], []
    pieces = q.split('"')
    for i, piece in enumerate(pieces):
        if i % 2 == 1:
            phrases.append(piece.lower())
            continue
        for w in piece.split():
            low = w.lower()
            if low.startswith("-"):
                excluded.append(low[1:])
            elif low.startswith("tag:"):
                tags.append(low[4:])
            else:
                words.append(low)
    return Query(words, phrases, excluded, tags)

def matches(q, text, doc_tags):
    low = text.lower()
    ws = low.split()
    return all(w in ws for w in q.words) and all(p in low for p in q.phrases) and all(x not in ws for x in q.excluded) and all(t in doc_tags for t in q.tags)

def show_list(xs):
    return "[" + ", ".join(xs) + "]"

docs = [("Install guide for the command line tool", ["docs", "cli"]), ("Command line flags reference", ["docs", "cli"]), ("Release notes for the line editor", ["news"]), ("Guide to the web dashboard", ["docs", "web"]), ("Old command line tool guide", ["docs", "archive"])]
queries = ['"command line" guide', "guide -old", "line tag:news", '"line tool" tag:docs -archive']
for qs in queries:
    q = parse(qs)
    print(f"query: {qs}")
    print(f"  words {show_list(q.words)} phrases {len(q.phrases)} excluded {len(q.excluded)} tags {len(q.tags)}")
    for text, tags in docs:
        if matches(q, text, tags):
            print(f"  -> {text}")
