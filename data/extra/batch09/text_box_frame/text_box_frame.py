def frame(title, lines, right):
    width = len(title) + 2
    for l in lines:
        width = max(width, len(l))
    label = f" {title} "
    left_dashes = (width + 2 - len(label)) // 2
    right_dashes = width + 2 - len(label) - left_dashes
    out = ["+" + "-" * left_dashes + label + "-" * right_dashes + "+"]
    for l in lines:
        body = l.rjust(width) if right else l.ljust(width)
        out.append(f"| {body} |")
    out.append("+" + "-" * (width + 2) + "+")
    return out

note = ["Bins go out Tuesday night.", "Spare key is under the pot.", "Feed the cat twice a day."]
for line in frame("NOTE", note, False):
    print(line)
prices = ["tea 2.50", "scone 3.25", "jam 0.75"]
for line in frame("MENU", prices, True):
    print(line)
