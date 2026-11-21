tree = {"Home": ["Tickets", "Account", "Help"], "Tickets": ["Single", "Day pass", "Season"], "Account": ["Top up", "History"], "Season": ["Monthly", "Annual"]}
out = []
def walk(node, path):
    here = path + [node]
    kids = tree.get(node, [])
    if not kids:
        out.append(" > ".join(here)); return
    for k in kids: walk(k, here)
walk("Home", [])
for c in out: print(c)
print(f"{len(out)} screens, deepest {max(len(c.split(' > ')) for c in out)} levels")
print(f"season screens: {sum(1 for c in out if 'Season' in c)}")
