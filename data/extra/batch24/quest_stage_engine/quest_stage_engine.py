stages = [("talk to the miller", "talk:miller", 1), ("gather 3 wheat", "pick:wheat", 3), ("scare off 2 crows", "scare:crow", 2), ("return to the miller", "talk:miller", 1)]
events = ["pick:wheat", "talk:miller", "pick:wheat", "scare:crow", "pick:wheat", "pick:berry", "pick:wheat", "scare:crow", "scare:crow", "talk:smith", "talk:miller"]
stage = 0; count = 0; ignored = 0
for i, e in enumerate(events):
    if stage >= len(stages): break
    if e != stages[stage][1]:
        ignored += 1; continue
    count += 1
    if count == stages[stage][2]:
        print(f"event {i + 1:>2} ({e}): done - {stages[stage][0]}")
        stage += 1; count = 0
if stage == len(stages):
    print("quest complete: 50 gold and the miller's thanks")
else:
    print(f"quest stuck at: {stages[stage][0]}")
print(f"{ignored} events did not count")
