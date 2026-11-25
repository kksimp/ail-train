import sys

msgs = {}
bad = dup = 0
for raw in sys.stdin.read().splitlines():
    if not raw.strip():
        continue
    w = raw.split()
    try:
        if len(w) != 4:
            raise ValueError
        seq, total = int(w[1]), int(w[2])
        if total < 1 or seq < 0 or seq >= total:
            raise ValueError
    except ValueError:
        bad += 1
        continue
    m = msgs.get(w[0])
    if m is None:
        m = msgs[w[0]] = [total, {}]
    elif m[0] != total:
        bad += 1
        continue
    if seq in m[1]:
        dup += 1
    else:
        m[1][seq] = w[3]
out = []
for k, (total, got) in msgs.items():
    if len(got) == total:
        out.append(f"{k} complete data={''.join(got[i] for i in range(total))}")
    else:
        miss = ",".join(str(i) for i in range(total) if i not in got)
        out.append(f"{k} incomplete have={len(got)}/{total} missing={miss}")
out.append(f"malformed={bad} duplicates={dup}")
print("\n".join(out))
