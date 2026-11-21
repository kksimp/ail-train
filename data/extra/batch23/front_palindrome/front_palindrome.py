def prefix_fn(cs):
    pi = [0]
    for i in range(1, len(cs)):
        k = pi[i - 1]
        while k > 0 and cs[i] != cs[k]:
            k = pi[k - 1]
        if cs[i] == cs[k]:
            k += 1
        pi.append(k)
    return pi

def make_palindrome(s):
    rev = s[::-1]
    joined = f"{s}#{rev}"
    pi = prefix_fn(list(joined))
    keep = pi[len(pi) - 1]
    extra = s[keep:][::-1]
    return f"{extra}{s}"

for s in ["abcd", "aacecaaa", "racecar", "banana", "abab", "noonday"]:
    p = make_palindrome(s)
    added = len(p) - len(s)
    print(f"{s:<9} +{added} -> {p}")
