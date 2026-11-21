L = ["A man and his dog ran up a hill", "This is a story without that symbol", "Every letter here is tested", "Big cats sit on warm rugs"]
for b in ["e", "a"]:
    print(f"banned '{b}':")
    for l in L:
        bad = [w for w in l.split(" ") if b in w.lower()]; t = len(l.split(" "))
        print(f"  ok: {l}" if not bad else f"  {t - len(bad)}/{t} clean, fails on {', '.join(bad)}")
