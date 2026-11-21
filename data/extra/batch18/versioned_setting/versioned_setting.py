vals = [19]
for t in [20, 21, 18]:
    vals.append(t); print(f"thermostat set to {t}")
print(f"now {vals[-1]} after {len(vals)} versions")
if len(vals) >= 2:
    vals.pop(); print(f"undo: back to {vals[-1]}")
def at(v): return vals[v - 1] if 1 <= v <= len(vals) else -1
print(f"version 2 was {at(2)}, version 9 is {at(9)}")
theme = ["light", "dark"]
def undo(h):
    if len(h) < 2: return False
    h.pop(); return True
a = undo(theme); b = undo(theme)
print(f"theme {theme[-1]}, undo results {str(a).lower()} {str(b).lower()}")
