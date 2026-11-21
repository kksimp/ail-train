def c10(s):
    t = sum(int(s[i]) * (10 - i) for i in range(9)); w = (11 - t % 11) % 11; l = 10 if s[9] == "X" else int(s[9])
    return "valid" if l == w else f"invalid, expected {'X' if w == 10 else w}"
def c13(s):
    t = sum(int(s[i]) * (1 if i % 2 == 0 else 3) for i in range(12)); w = (10 - t % 10) % 10
    return "valid" if int(s[12]) == w else f"invalid, expected {w}"
for s in ["0-306-40615-2", "0-306-40615-3", "0-8044-2957-X", "978-0-306-40615-7", "978-0-306-40615-1", "12345"]:
    d = s.replace("-", ""); print(f"{s}: {c10(d) if len(d) == 10 else c13(d) if len(d) == 13 else 'wrong length'}")
