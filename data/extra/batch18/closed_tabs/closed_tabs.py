closed = [("Mail", True), ("Docs", False), ("Weather", False), ("Calendar", True), ("News", False), ("Video", False)]
print(f"next to reopen: {closed[-1][0]}")
op = []
while closed:
    t = closed.pop(); op.append(t[0]); print(f"reopened {t[0]}")
    if t[1]:
        print(f"stopped at pinned tab {t[0]}"); break
print(f"open now: {', '.join(op)}")
print("closed: [" + ", ".join(f'"{t[0]}"' for t in closed) + "]")
print(f"next would be {closed[-1][0] if closed else 'nothing'}")
