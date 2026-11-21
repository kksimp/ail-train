def pieces(word, vocab):
    out = []
    start = 0
    while start < len(word):
        end = len(word)
        found = ""
        while end > start:
            core = word[start:end]
            cand = "##" + core if start > 0 else core
            if cand in vocab:
                found = cand
                break
            end -= 1
        if found == "":
            return ["[UNK]"]
        out.append(found)
        start = end
    return out

vocab = {"un", "##aff", "##able", "play", "##ing", "##ed", "##er", "##s", "run", "##n", "token", "##ize", "##iz", "##ation", "a", "##b", "##c"}
text = "unaffable playing played runner tokenization players xyz abc"
total = 0
for w in text.split(" "):
    ps = pieces(w, vocab)
    total += len(ps)
    print(f"{w:<13} " + " ".join(ps))
print(f"{len(text.split(' '))} words became {total} tokens")
