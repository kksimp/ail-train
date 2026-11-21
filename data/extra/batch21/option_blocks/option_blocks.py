from itertools import permutations
blocks = {'A': ["History", "Art", "Computing"], 'B': ["Geography", "Music", "Computing", "French"], 'C': ["History", "Drama", "Spanish", "Art"]}
pupils = [("Ivy", ["History", "Computing", "Art"]), ("Jake", ["Art", "Drama", "Spanish"]), ("Kia", ["Music", "French", "History"]), ("Leo", ["Computing", "Geography", "Drama"]), ("Mae", ["Art", "History", "French"])]

def fits(choices):
    for order in permutations("ABC"):
        if all(choices[k] in blocks[order[k]] for k in range(3)):
            return list(order)
    return []

clashes = 0
for name, picks in pupils:
    order = fits(picks)
    if not order:
        clashes += 1
        print(f"{name}: {', '.join(picks)} clash, choose again")
    else:
        print(f"{name}: {', '.join(f'{picks[k]} ({order[k]})' for k in range(3))}")
print(f"{clashes} pupils need to change a choice")
