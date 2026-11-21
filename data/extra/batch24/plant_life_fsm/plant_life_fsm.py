days = "WS WS W. WS WS .S .S WS WS WS WS .S .S .S .S"
stage = "Seed"; progress = 0; dry = 0; before_wilt = "Seed"
codes = days.split(" ")
for i, code in enumerate(codes):
    watered = code[0] == 'W'; sunny = code[1] == 'S'
    before = stage
    if stage != "Dead":
        if watered: dry = 0
        else: dry += 1
        if stage == "Seed":
            if watered: progress += 1
            if progress >= 3: stage = "Sprout"; progress = 0
        elif stage == "Sprout":
            if watered and sunny: progress += 1
            if progress >= 4: stage = "Bloom"
        elif stage == "Wilting":
            if watered: stage = before_wilt
            elif dry >= 4: stage = "Dead"
        if dry == 2 and stage != "Wilting" and stage != "Dead":
            before_wilt = stage; stage = "Wilting"
    if stage != before:
        print(f"day {i + 1:>2}: Stage.{before} -> Stage.{stage}")
print(f"after {len(codes)} days the plant is Stage.{stage}")
