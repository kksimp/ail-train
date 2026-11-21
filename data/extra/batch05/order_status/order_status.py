T = {("Placed", "pay"): "Paid", ("Placed", "cancel"): "Cancelled", ("Paid", "ship"): "Shipped", ("Paid", "cancel"): "Cancelled", ("Shipped", "deliver"): "Delivered"}
O = {"A100": "Placed", "A101": "Placed", "A102": "Placed"}
for i, e in [("A100", "pay"), ("A101", "ship"), ("A100", "ship"), ("A102", "cancel"), ("A101", "pay"), ("A102", "pay"), ("A100", "deliver"), ("A101", "cancel")]:
    n = T.get((O[i], e))
    if n: O[i] = n; print(f"{i} {e}: now State.{n}")
    else: print(f"{i} {e}: not allowed from State.{O[i]}")
for i in ["A100", "A101", "A102"]: print(f"{i}: State.{O[i]}")
