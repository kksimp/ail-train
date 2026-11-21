def sh(v): return " ".join(f"{k}:{v[k]}" for k in sorted(v))
def ad(a, b):
    o = dict(a)
    for k in b:
        o[k] = o.get(k, 0) + b[k]
        if o[k] == 0: del o[k]
    return o
A = {0: 3, 4: -2, 9: 5, 100: 1}; B = {4: 2, 9: 1, 50: 7, 0: -1}
print(f"a = {sh(A)}"); print(f"b = {sh(B)}"); print(f"a + b = {sh(ad(A, B))}"); print(f"a . b = {sum(A[k] * B[k] for k in A if k in B)}")
