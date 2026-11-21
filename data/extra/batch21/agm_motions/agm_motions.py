members, present, proxies = 132, 29, 6
voters = present + proxies
quorum = (members + 3) // 4
print(f"quorate: {voters} voting, {quorum} needed")
motions = [("approve accounts", "Ordinary", 30, 2, 3), ("raise fees 5%", "Ordinary", 15, 15, 5), ("change constitution", "Special", 26, 9, 0), ("new trophy", "Special", 27, 8, 0), ("merge with rowing club", "Special", 20, 4, 11), ("buy a minibus", "Ordinary", 22, 10, 9)]

def passes(m):
    cast = m[2] + m[3]
    if m[1] == "Ordinary":
        return m[2] > m[3]
    return cast > 0 and m[2] * 100 >= cast * 75

carried = 0
for m in motions:
    if m[2] + m[3] + m[4] > voters:
        print(f"{m[0]}: count error, recount")
        continue
    cast = m[2] + m[3]
    pct = 0 if cast == 0 else m[2] * 100 // cast
    if passes(m):
        carried += 1
    print(f"{m[0]} ({m[1]}): {m[2]}-{m[3]}, {pct}% for: {'carried' if passes(m) else 'lost'}")
print(f"{carried} motions carried")
