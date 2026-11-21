def spread(px):
    best = 0
    chan = 0
    for c in range(3):
        vals = [p[c] for p in px]
        r = max(vals) - min(vals)
        if r > best:
            best = r
            chan = c
    return (best, chan)

def hexs(px):
    parts = []
    for c in range(3):
        total = 0
        for p in px:
            total = total + p[c]
        avg = total // len(px)
        parts.append(f"{avg:02x}")
    return "#" + "".join(parts)

pixels = [[250, 240, 230], [245, 235, 220], [30, 40, 60], [25, 35, 70], [200, 60, 50], [210, 70, 40], [190, 50, 60], [60, 150, 70], [70, 160, 60], [50, 140, 80], [240, 230, 240], [20, 30, 50]]
boxes = [pixels]
while len(boxes) < 4:
    pick = 0
    for i in range(len(boxes)):
        if spread(boxes[i])[0] > spread(boxes[pick])[0]:
            pick = i
    chan = spread(boxes[pick])[1]
    srt = sorted(boxes[pick], key=lambda p: p[chan])
    half = len(srt) // 2
    boxes.pop(pick)
    boxes.append(srt[:half])
    boxes.append(srt[half:])
    print(f"split on {['red', 'green', 'blue'][chan]} at {srt[half][chan]}")
for b in boxes:
    print(f"{len(b)} pixels -> {hexs(b)}")
