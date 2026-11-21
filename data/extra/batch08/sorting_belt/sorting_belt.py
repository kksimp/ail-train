C = ["red", "blue", "green"]; H = [0, 0, 0]; E = [0, 0, 0]; r = 0
for i, t in enumerate(["red", "blue", "red", "green", "red", "yellow", "blue", "red", "blue", "blue", "green", "red", "pink", "red"]):
    if t in C:
        c = C.index(t); H[c] += 1
        if H[c] == 3: E[c] += 1; H[c] = 0; print(f"parcel {i + 1}: {t} chute full, emptied")
    else: r += 1; print(f"parcel {i + 1}: {t} rejected")
for i, n in enumerate(C): print(f"{n}: emptied {E[i]} times, {H[i]} waiting")
print(f"{r} rejects")
