fiction = ["Austen", "Bronte", "Dickens", "Eliot", "Hardy", "Woolf"]; overflow = ["Zola"]; cart = []
caps = {"overflow": 3, "cart": 10}
def transfer(src, dst, cap, n):
    moved = 0
    while moved < n and len(dst) < cap:
        if not src: break
        dst.append(src.pop()); moved += 1
    return moved
sz = lambda: f"fiction {len(fiction)}, overflow {len(overflow)}, cart {len(cart)}"
m1 = transfer(fiction, overflow, 3, 4); print(f"asked 4, moved {m1}: {sz()}")
m2 = transfer(overflow, cart, 10, 5); print(f"asked 5, moved {m2}: {sz()}")
m3 = transfer(fiction, cart, 10, 2); print(f"asked 2, moved {m3}: {sz()}")
print(f"cart order: {', '.join(cart)}")
