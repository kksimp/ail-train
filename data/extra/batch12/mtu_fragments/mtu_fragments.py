def fragment(f, mtu):
    offset, size, more = f
    room = (mtu - 20) // 8 * 8
    if size <= mtu - 20:
        return [f]
    out = []
    done = 0
    while done < size:
        part = min(room, size - done)
        last = done + part >= size
        out.append((offset + done // 8, part, more or not last))
        done += part
    return out

def show(fs):
    return " ".join(f"{o}/{s}{'+' if m else ''}" for o, s, m in fs)

packet = (0, 3980, False)
first = fragment(packet, 1500)
print(f"after MTU 1500: {show(first)}")
second = []
for f in first:
    second.extend(fragment(f, 576))
print(f"after MTU 576:  {show(second)}")
total = sum(f[1] for f in second)
print(f"{len(second)} fragments carry {total} data bytes plus {len(second) * 20} header bytes")
print("offset/size, + means more fragments follow")
