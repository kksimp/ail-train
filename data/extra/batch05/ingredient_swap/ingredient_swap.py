S = {"butter": "olive oil", "egg": "flax egg", "milk": "oat milk", "honey": "maple syrup"}; B = {"butter", "egg", "milk", "honey", "gelatine"}; o = []; m = []
for i in ["flour", "butter", "sugar", "egg", "milk", "honey", "vanilla", "gelatine"]:
    if i in B:
        if i in S: o.append(f"{S[i]} (for {i})")
        else: m.append(i)
    else: o.append(i)
for l in o: print(f"- {l}")
print("fully vegan" if not m else f"no swap for: {', '.join(m)}")
