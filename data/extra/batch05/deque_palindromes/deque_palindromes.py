def ck(s):
    c = [x for x in s.lower() if x.isalnum()]; i = 0; j = len(c) - 1
    while i < j:
        if c[i] != c[j]: return f"no ({c[i]} vs {c[j]})"
        i += 1; j -= 1
    return "yes"
for s in ["A man, a plan, a canal: Panama", "Was it a car or a cat I saw?", "No lemon, no melon", "Hello, world", "Step on no pets!", "Palindrome"]: print(f"{s}: {ck(s)}")
