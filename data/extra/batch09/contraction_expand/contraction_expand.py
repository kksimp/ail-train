def expand_word(word):
    core = word
    tail = ""
    while len(core) > 0 and core[-1] in ".,!?":
        tail = core[-1] + tail
        core = core[:-1]
    lower = core.lower()
    special = {"won't": "will not", "can't": "cannot", "shan't": "shall not", "it's": "it is", "that's": "that is"}
    out = core
    if lower in special:
        out = special[lower]
    else:
        for ending, full in [("n't", " not"), ("'re", " are"), ("'ll", " will"), ("'ve", " have"), ("'m", " am"), ("'d", " would")]:
            if lower.endswith(ending):
                out = lower[:len(lower) - len(ending)] + full
                break
    if out != core and core[0].isupper():
        out = out[0].upper() + out[1:]
    return out + tail

lines = ["I'm sure we'll win; we won't lose!", "They're late and it's raining.", "You'd think she'd know.", "Can't stop, I've got to go!", "That's what we're doing."]
changed = 0
for line in lines:
    out = []
    for w in line.split(" "):
        e = expand_word(w)
        if e != w:
            changed += 1
        out.append(e)
    print(" ".join(out))
print(f"{changed} contractions expanded")
