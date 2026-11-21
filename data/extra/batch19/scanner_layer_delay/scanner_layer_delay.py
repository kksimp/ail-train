def caught(depth, size, delay):
    return (delay + depth) % (2 * (size - 1)) == 0

lines = ["0: 6", "2: 5", "4: 4", "5: 2", "6: 4", "8: 3"]
layers = [[int(x) for x in l.split(": ")] for l in lines]
severity = 0
for l in layers:
    if caught(l[0], l[1], 0):
        print(f"caught at layer {l[0]} (range {l[1]})")
        severity += l[0] * l[1]
print(f"part 1: severity {severity}")
delay = 0
while any(caught(l[0], l[1], delay) for l in layers):
    delay += 1
print(f"part 2: wait {delay} picoseconds to pass unseen")
