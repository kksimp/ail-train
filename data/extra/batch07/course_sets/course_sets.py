S = [("Ali", {"maths", "physics", "art", "music"}), ("Bea", {"maths", "physics", "history"}), ("Cal", {"maths", "art", "music", "drama"}), ("Dev", {"maths", "physics", "music"})]
c = set(S[0][1])
for s in S: c &= s[1]
print("everyone takes: " + ", ".join(sorted(c))); b = ("", "", -1)
for i in range(len(S)):
    for j in range(i + 1, len(S)):
        n = len(S[i][1] & S[j][1])
        if n > b[2]: b = (S[i][0], S[j][0], n)
print(f"most in common: {b[0]} and {b[1]} ({b[2]})"); print("ready for engineering: " + ", ".join(s[0] for s in S if {"maths", "physics"} <= s[1]))
