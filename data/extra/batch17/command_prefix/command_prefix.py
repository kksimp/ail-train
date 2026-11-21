def resolve(word, commands, aliases):
    if word in commands:
        return word, None
    if word in aliases:
        return aliases[word], None
    hits = [c for c in commands if c.startswith(word)]
    if len(hits) == 1:
        return hits[0], None
    if len(hits) == 0:
        return None, f"unknown command '{word}'"
    shown = ", ".join(hits)
    return None, f"'{word}' is ambiguous: {shown}"

commands = ["status", "stash", "commit", "checkout", "cherry-pick", "push", "pull", "log"]
aliases = {"co": "checkout", "ci": "commit", "st": "status"}
for word in ["st", "sta", "stas", "c", "che", "cherry", "co", "pu", "pus", "log", "lo", "merge"]:
    cmd, err = resolve(word, commands, aliases)
    if cmd is not None:
        print(f"{word:<7} -> {cmd}")
    else:
        print(f"{word:<7} !! {err}")
