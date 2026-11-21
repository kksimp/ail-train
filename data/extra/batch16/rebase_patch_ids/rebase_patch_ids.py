def patch_id(diff):
    h = 0
    for c in diff:
        if not c.isspace():
            h = (h * 257 + ord(c)) % 999983
    return h

upstream = [["u1", "+add retries"], ["u2", "-old flag\n+new flag"], ["u3", "+fix typo in help"]]
topic = [["t1", "+cache layer"], ["t2", "-old flag\n+new  flag"], ["t3", "+metrics"], ["t4", "+fix typo  in help"], ["t5", "+docs for cache"]]
known = set(patch_id(u[1]) for u in upstream)
tip = upstream[-1][0]
replayed = 0
for t in topic:
    pid = patch_id(t[1])
    if pid in known:
        print(f"{t[0]} skipped: same change already upstream (patch id {pid})")
    else:
        print(f"{t[0]}' replayed on {tip} (patch id {pid})")
        tip = f"{t[0]}'"
        replayed += 1
print(f"{replayed} commits replayed, new tip {tip}")
