import string
for s in ["The quick brown fox jumps over the lazy dog", "Hello world", "Pack my box with five dozen liquor jugs", "Sphinx of black quartz judge my vow", ""]:
    gaps = sorted(set(string.ascii_lowercase) - set(c for c in s.lower() if c.isalpha()))
    if not gaps:
        print(f"pangram: {s}")
    else:
        print(f"{26 - len(gaps)}/26, missing {len(gaps)}: {''.join(gaps)}")
