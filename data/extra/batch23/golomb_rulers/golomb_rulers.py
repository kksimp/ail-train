def place(marks, order, length, used, nodes):
    nodes[0] += 1
    if len(marks) == order:
        return True
    last = marks[-1]
    for m in range(last + 1, length + 1):
        if len(marks) == order - 1 and m != length:
            continue
        ok = True
        for x in marks:
            if used[m - x]:
                ok = False
        if ok:
            for x in marks:
                used[m - x] = True
            marks.append(m)
            if place(marks, order, length, used, nodes):
                return True
            marks.pop()
            for x in marks:
                used[m - x] = False
    return False

def optimal(order):
    length = order - 1
    while True:
        marks = [0]
        used = [False] * (length + 1)
        nodes = [0]
        if place(marks, order, length, used, nodes):
            marks.append(nodes[0])
            return marks
        length += 1

for order in range(2, 7):
    r = optimal(order)
    nodes = r[-1]
    marks = r[0:len(r) - 1]
    print(f"{order} marks: length {marks[-1]:>2}, ruler {marks} ({nodes} nodes in the last search)")
