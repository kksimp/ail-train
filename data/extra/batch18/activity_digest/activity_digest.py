feed = [("like", "kai", 12), ("follow", "noor"), ("like", "lu", 12), ("reply", "kai", "great shot!"), ("mention", "ren", 15), ("like", "noor", 15), ("like", "ren", 12), ("follow", "max")]
likes = {}; fol = []; lines = []
for n in feed:
    if n[0] == "like": likes[n[2]] = likes.get(n[2], 0) + 1
    elif n[0] == "follow": fol.append(n[1])
    elif n[0] == "mention": lines.append(f"{n[1]} mentioned you on post {n[2]}")
    else: lines.append(f"{n[1]} replied: {n[2]}")
for p in sorted(likes): print(f"post {p}: {likes[p]} likes")
print(f"new followers: {' and '.join(fol)}")
for l in lines: print(l)
print(f"{len(feed)} notifications in one digest")
