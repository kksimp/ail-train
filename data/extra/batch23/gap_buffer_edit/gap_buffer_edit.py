class GapBuffer:
    def __init__(self, capacity):
        self.cells = ['_'] * capacity
        self.start = 0
        self.end = capacity

    def type_text(self, s):
        for c in s:
            self.cells[self.start] = c
            self.start += 1

    def left(self, n):
        for i in range(n):
            if self.start > 0:
                self.start -= 1
                self.end -= 1
                self.cells[self.end] = self.cells[self.start]
                self.cells[self.start] = '_'

    def right(self, n):
        for i in range(n):
            if self.end < len(self.cells):
                self.cells[self.start] = self.cells[self.end]
                self.cells[self.end] = '_'
                self.start += 1
                self.end += 1

    def text(self):
        return "".join(self.cells[0:self.start]) + "".join(self.cells[self.end:])

def show(step, g):
    raw = "".join(g.cells)
    print(f"{step:<16} [{raw}] -> {g.text()}")

g = GapBuffer(16)
g.type_text("helo world")
show("type", g)
g.left(7)
show("left 7", g)
g.type_text("l")
show("type l", g)
g.right(7)
show("right 7", g)
g.type_text("!")
show("type !", g)
