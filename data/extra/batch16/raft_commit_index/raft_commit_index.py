def advance(log, term, commit, matched):
    majority = len(matched) // 2 + 1
    n = len(log)
    while n > commit:
        copies = sum(1 for m in matched if m >= n)
        if copies >= majority:
            if log[n - 1] == term:
                return n
            print(f"  index {n} is on {copies} servers but has old term {log[n - 1]}, not counted")
        n -= 1
    return commit

log = [1, 1, 2, 2, 3, 3, 3]
term = 3
commit = 2
print(f"leader term {term}, log terms {log}, commit index {commit}")
for matched in [[7, 4, 4, 2, 1], [7, 6, 5, 4, 2], [7, 7, 7, 3, 6]]:
    print(f"match indexes {matched}:")
    commit = advance(log, term, commit, matched)
    print(f"  commit index now {commit}")
