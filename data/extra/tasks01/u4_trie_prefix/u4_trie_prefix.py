import sys

class Node:
    def __init__(self):
        self.kids = {}
        self.pass_ = 0
        self.end = 0

root = Node()

def valid(s):
    return len(s) > 0 and all("a" <= c <= "z" for c in s)

def walk(word):
    n = root
    for c in word:
        n = n.kids.get(c)
        if n is None:
            return None
    return n

def add(word):
    n = root
    for c in word:
        if c not in n.kids:
            n.kids[c] = Node()
        n = n.kids[c]
        n.pass_ += 1
    n.end += 1

def delete(word):
    n = walk(word)
    if n is None or n.end == 0:
        return False
    n = root
    for c in word:
        n = n.kids[c]
        n.pass_ -= 1
    n.end -= 1
    return True

for line in sys.stdin.read().splitlines():
    w = line.split()
    if not w:
        continue
    c = w[0]
    if c in ("add", "del", "has", "count", "longest") and len(w) == 2 and valid(w[1]):
        word = w[1]
        if c == "add":
            add(word)
            print("ok")
        elif c == "del":
            print("ok" if delete(word) else "missing")
        elif c == "has":
            n = walk(word)
            print(n.end if n else 0)
        elif c == "count":
            n = walk(word)
            print(n.pass_ if n else 0)
        else:
            n = walk(word)
            if n is None or n.pass_ == 0:
                print("none")
            else:
                s = word
                while n.end == 0:
                    live = [(k, v) for k, v in n.kids.items() if v.pass_ > 0]
                    if len(live) != 1:
                        break
                    s += live[0][0]
                    n = live[0][1]
                print(s)
    else:
        print("error")
