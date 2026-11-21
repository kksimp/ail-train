def longest_unique(items):
    last = {}
    start = 0
    best_start = 0
    best_len = 0
    for i, s in enumerate(items):
        prev = last.get(s, -1)
        if prev >= start:
            start = prev + 1
        last[s] = i
        if i - start + 1 > best_len:
            best_len = i - start + 1
            best_start = start
    return [best_start, best_len]

plays = "rain sun wind rain moon star sun tide moon wind rain star dusk".split(" ")
r = longest_unique(plays)
run = ", ".join(plays[r[0]:r[0] + r[1]])
print(f"playlist of {len(plays)} plays: longest fresh run is {r[1]} songs from play {r[0] + 1}")
print(f"  {run}")
for word in ["abcabcbb", "bbbbb", "pwwkew", "dvdf", "abcdefg"]:
    q = longest_unique(list(word))
    piece = word[q[0]:q[0] + q[1]]
    print(f"{word:<9} {q[1]} distinct letters: {piece}")
