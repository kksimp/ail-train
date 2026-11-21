cards = {}; refused = 0
for kind, card, room in [("issue", 501, 12), ("issue", 502, 14), ("issue", 503, 12), ("swipe", 502, 14), ("swipe", 503, 14), ("revoke", 501, 0), ("swipe", 501, 12), ("issue", 504, 15), ("swipe", 503, 12)]:
    if kind == "issue":
        cards[card] = room; print(f"card {card} issued for room {room}")
    elif kind == "revoke":
        cards.pop(card, None); print(f"card {card} revoked")
    else:
        o = cards.get(card, -1)
        if o == room: print(f"card {card} opens room {room}")
        else:
            refused += 1
            why = "unknown card" if o < 0 else f"card is for room {o}"
            print(f"card {card} refused at room {room}: {why}")
br = {}
for c, r in cards.items(): br.setdefault(r, []).append(c)
for r in sorted(br): print(f"room {r}: cards {br[r]}")
print(f"{refused} refused swipes")
