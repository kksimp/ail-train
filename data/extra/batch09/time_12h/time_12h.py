def parse(text):
    t = text.lower().replace(".", "").replace(" ", "")
    pm = False
    if t.endswith("pm"):
        pm = True
        body = t[:-2]
    elif t.endswith("am"):
        body = t[:-2]
    else:
        return None, "no am or pm"
    parts = body.split(":")
    try:
        h = int(parts[0])
    except ValueError:
        return None, "bad hour"
    if len(parts) > 1:
        try:
            m = int(parts[1])
        except ValueError:
            m = -1
    else:
        m = 0
    if h < 1 or h > 12:
        return None, f"hour {h} is not 1 to 12"
    if m < 0 or m > 59:
        return None, "bad minutes"
    base = 0 if h == 12 else h
    return (base + (12 if pm else 0)) * 60 + m, None

for t in ["7:05 pm", "12:00 am", "12:30 PM", "11:59 p.m.", "9 am", "6:15am", "13:00 pm", "4:75 pm", "noon"]:
    mins, err = parse(t)
    if mins is not None:
        print(f"{t:<11} -> {mins // 60:02}:{mins % 60:02}")
    else:
        print(f"{t:<11} -> error: {err}")
