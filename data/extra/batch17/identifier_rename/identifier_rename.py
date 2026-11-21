def is_ident(c):
    return c.isalnum() or c == '_'

def rename(line, old, new, counts):
    cs = list(line)
    out = []
    i = 0
    in_str = False
    while i < len(cs):
        c = cs[i]
        if not in_str and c == '#':
            rest = line[i:]
            counts[1] += rest.count(old)
            out.append(rest)
            break
        if c == '"':
            in_str = not in_str
        if is_ident(c) and (i == 0 or not is_ident(cs[i - 1])):
            j = i
            while j < len(cs) and is_ident(cs[j]):
                j += 1
            word = line[i:j]
            after_dot = i > 0 and cs[i - 1] == '.'
            if word == old and not in_str and not after_dot:
                out.append(new)
                counts[0] += 1
            else:
                if word == old:
                    counts[1] += 1
                out.append(word)
            i = j
        else:
            out.append(c)
            i += 1
    return "".join(out)

src = ["count = 0", "for item in items:", "    count += item.count", "    recount = count * 2", 'print("count is", count)  # count shown', "max_count = count_all(count)"]
counts = [0, 0]
for line in src:
    print(rename(line, "count", "total", counts))
print(f"renamed {counts[0]}, left alone (fields, strings, comments) {counts[1]}")
