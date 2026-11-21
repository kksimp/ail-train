buf = "demo moved to friday"
print(f"start: {buf}")
def ins(b, at, t): return b[:at] + t + b[at:]
steps = [("insert 'Dear team, ' at 0", lambda b: ins(b, 0, "Dear team, ")),
         ("replace 'friday' with 'Thursday'", lambda b: b.replace("friday", "Thursday")),
         ("delete 5 at 11", lambda b: b[:11] + b[min(16, len(b)):]),
         ("insert 'our call ' at 11", lambda b: ins(b, 11, "our call ")),
         ("upper-case all", lambda b: b.upper())]
for d, f in steps:
    buf = f(buf); print(f"{d} -> {buf}")
print(f"{len(buf)} characters")
