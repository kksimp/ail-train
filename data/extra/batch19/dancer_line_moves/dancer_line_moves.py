def dance(line, moves):
    d = list(line)
    for m in moves:
        body = m[1:]
        if m[0] == "s":
            n = int(body); d = d[len(d) - n:] + d[:len(d) - n]
        elif m[0] == "x":
            a, b = body.split("/"); a = int(a); b = int(b)
            d[a], d[b] = d[b], d[a]
        else:
            i = d.index(body[0]); j = d.index(body[2])
            d[i], d[j] = d[j], d[i]
    return d

moves = "s2,x3/6,pa/e,x0/7,s5,pc/h,x2/4,pb/g".split(",")
start = list("abcdefgh")
print(f"part 1: after one dance {''.join(dance(start, moves))}")
seen = {}; order = []; d = start
while "".join(d) not in seen:
    seen["".join(d)] = len(order); order.append("".join(d)); d = dance(d, moves)
first = seen["".join(d)]; period = len(order) - first
print(f"the line repeats every {period} dances (from dance {first})")
total = 1000000
print(f"part 2: after {total} dances {order[first + (total - first) % period]}")
