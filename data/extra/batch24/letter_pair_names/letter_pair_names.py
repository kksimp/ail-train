state = 3141
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
sample = ["marta", "loren", "tobias", "selma", "orin", "talia", "bram", "elena", "rosamund", "milo"]
follow = {}
for word in sample:
    prev = '^'
    for ch in word:
        follow.setdefault(prev, []).append(ch); prev = ch
    follow.setdefault(prev, []).append('$')
made = []; tries = 0
while len(made) < 8:
    tries += 1
    letters = []; cur = '^'
    while len(letters) < 9:
        if cur not in follow: break
        options = follow[cur]
        cur = options[below(len(options))]
        if cur == '$': break
        letters.append(cur)
    word = "".join(letters)
    if 4 <= len(word) <= 8 and word not in sample and word not in made:
        made.append(word)
print(", ".join(made[:4]))
print(", ".join(made[4:]))
print(f"{tries} walks for 8 new names; {len(follow['^'])} start letters seen")
