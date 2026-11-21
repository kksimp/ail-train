days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
week = [("sun", 7), ("rain", 4), ("rain", 18), ("fog", 0), ("wind", 62), ("snow", 3), ("sun", 3)]
def adv(k, v):
    if k == "sun": return "t-shirt, hat and sun cream" if v >= 6 else "t-shirt"
    if k == "rain": return "raincoat and boots" if v > 10 else "umbrella"
    if k == "snow": return f"warm coat, {v} cm of snow"
    if k == "wind": return "stay in if you can" if v >= 50 else "windproof jacket"
    return "bright jacket, drive slowly"
for i, (k, v) in enumerate(week): print(f"{days[i]}: {adv(k, v)}")
print(f"{sum(1 for k, v in week if k in ('rain', 'snow'))} wet days this week")
