class Zipper:
    def __init__(s, xs):
        s.before, s.focus, s.after = [], xs[0], list(reversed(xs[1:]))
    def next(s):
        if s.after:
            n = s.after.pop()
            s.before.append(s.focus)
            s.focus = n
    def prev(s):
        if s.before:
            p = s.before.pop()
            s.after.append(s.focus)
            s.focus = p
    def insert(s, song):
        s.before.append(s.focus)
        s.focus = song
    def delete(s):
        if s.after:
            s.focus = s.after.pop()
        elif s.before:
            s.focus = s.before.pop()
    def show(s):
        return f"[{' '.join(s.before)}] <{s.focus}> [{' '.join(reversed(s.after))}]"

z = Zipper(["intro", "rain", "drift", "pulse", "outro"])
print(f"start      {z.show()}")
for op in ["next", "next", "insert", "prev", "delete", "next", "next", "next", "delete"]:
    if op == "next":
        z.next()
    elif op == "prev":
        z.prev()
    elif op == "insert":
        z.insert("echo")
    else:
        z.delete()
    print(f"{op:<10} {z.show()}")
