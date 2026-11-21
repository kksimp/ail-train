text = "first line\nsecond\n\nfourth has more words\nfive\nsix\nseven\n\neight\nnine\nten is here"
ls = text.split("\n")
w = len(str(sum(1 for l in ls if l.strip())))
n = 0
for l in ls:
    if not l.strip(): print(f"{'':>{w}} |")
    else: n += 1; print(f"{n:>{w}} | {l}")
lg = max(ls, key=len)
print(f'longest: "{lg}" ({len(lg)} chars)')
