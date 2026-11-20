scores = [72, 85, 91, 60, 85, 77, 98, 85, 66, 70]
def rt(s):
    b = sum(1 for x in scores if x < s); e = sum(1 for x in scores if x == s)
    return (b * 2 + e) * 1000 // (len(scores) * 2)
for s in sorted(scores):
    r = rt(s)
    print(f"{s}: {r // 10}.{r % 10}")
srt = sorted(scores)
for p in [25, 50, 90]:
    k = (p * len(srt) + 99) // 100
    print(f"p{p} = {srt[max(k - 1, 0)]}")
