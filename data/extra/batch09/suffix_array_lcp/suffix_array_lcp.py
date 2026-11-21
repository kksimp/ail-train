def suffix_array(s):
    return sorted(range(len(s)), key=lambda i: s[i:])

def lcp_array(s, sa):
    n = len(sa)
    rank = [0] * n
    lcp = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
        else:
            h = 0
    return lcp

word = "banana"
sa = suffix_array(word)
lcp = lcp_array(word, sa)
for i in range(len(sa)):
    print(f"{i} start {sa[i]} lcp {lcp[i]}  {word[sa[i]:]}")
for w in ["banana", "mississippi", "abracadabra", "tattarrattat"]:
    a = suffix_array(w)
    l = lcp_array(w, a)
    n = len(w)
    distinct = n * (n + 1) // 2 - sum(l)
    best = 0
    for k in range(1, n):
        if l[k] > l[best]:
            best = k
    rep = w[a[best]:a[best] + l[best]]
    print(f"{w:<12} distinct substrings {distinct:>3}, longest repeat '{rep}'")
