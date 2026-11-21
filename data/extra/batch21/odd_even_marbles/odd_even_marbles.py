def next_state(s):
    return (s * 1103515245 + 12345) % 2147483648

def pick(s, n):
    return (s >> 16) % n

names = ["Mina", "Theo"]
marbles = [10, 10]
s = 2468
r = 0
while r < 12 and marbles[0] > 0 and marbles[1] > 0:
    hider = r % 2
    guesser = 1 - hider
    s = next_state(s)
    hidden = pick(s, marbles[hider]) + 1
    s = next_state(s)
    bet = min(pick(s, 3) + 1, marbles[guesser], marbles[hider])
    s = next_state(s)
    says_odd = pick(s, 2) == 0
    right = says_odd == (hidden % 2 == 1)
    guess = "odd" if says_odd else "even"
    if right:
        marbles[guesser] += bet
        marbles[hider] -= bet
    else:
        marbles[guesser] -= bet
        marbles[hider] += bet
    r += 1
    print(f"round {r:>2}: {names[hider]} hides {hidden}, {names[guesser]} bets {bet} on {guess} and {'wins' if right else 'loses'} ({marbles[0]}-{marbles[1]})")
leader = names[0] if marbles[0] > marbles[1] else (names[1] if marbles[1] > marbles[0] else "neither")
print(f"after {r} rounds: {leader} ahead")
