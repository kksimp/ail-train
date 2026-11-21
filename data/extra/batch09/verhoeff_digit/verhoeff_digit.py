D = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9, 5], [2, 3, 4, 0, 1, 7, 8, 9, 5, 6], [3, 4, 0, 1, 2, 8, 9, 5, 6, 7], [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], [5, 9, 8, 7, 6, 0, 4, 3, 2, 1], [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], [7, 6, 5, 9, 8, 2, 1, 0, 4, 3], [8, 7, 6, 5, 9, 3, 2, 1, 0, 4], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
P = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 7, 6, 2, 8, 3, 0, 9, 4], [5, 8, 0, 3, 7, 9, 6, 1, 4, 2], [8, 9, 1, 6, 0, 4, 3, 5, 2, 7], [9, 4, 5, 3, 1, 2, 8, 7, 0, 6], [4, 2, 8, 6, 5, 7, 3, 9, 0, 1], [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]

def run(digits, offset):
    c = 0
    for i, ch in enumerate(reversed(digits)):
        c = D[c][P[(i + offset) % 8][int(ch)]]
    return c

def check_digit(digits):
    inv = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]
    return inv[run(digits, 1)]

def valid(full):
    return run(full, 0) == 0

for num in ["236", "12345", "142857", "8473643095483"]:
    print(f"{num} -> check digit {check_digit(num)}")
good = "2363"
print(f"{good} valid: {'true' if valid(good) else 'false'}")
for bad in ["2263", "3263", "2633", "2336"]:
    print(f"{bad} valid: {'true' if valid(bad) else 'false'}")
