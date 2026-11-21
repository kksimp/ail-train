def note_name(m):
    names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return f"{names[m % 12]}{m // 12 - 1}"

tab = ["e|-------3-----0---|", "B|-------0---1-----|", "G|---0---0-2-------|", "D|-2-----0---------|", "A|-------2-------3-|", "E|-------3---------|"]
open_ = [64, 59, 55, 50, 45, 40]
rows = tab
width = len(rows[0])
lowest = 200
highest = 0
events = 0
for col in range(2, width):
    notes = []
    for s in range(6):
        c = rows[s][col]
        if c.isdigit():
            notes.append(open_[s] + int(c))
    if not notes:
        continue
    events += 1
    notes.sort()
    lowest = min(lowest, notes[0])
    highest = max(highest, notes[-1])
    names = " ".join(note_name(m) for m in notes)
    kind = "chord" if len(notes) > 1 else "note"
    print(f"column {col:>2}: {kind} {names}")
print(f"{events} events, range {note_name(lowest)} to {note_name(highest)}")
