def to_ms(t):
    parts = t.replace(",", ":").split(":")
    nums = [int(p) for p in parts]
    return ((nums[0] * 60 + nums[1]) * 60 + nums[2]) * 1000 + nums[3]

def stamp(ms):
    h = ms // 3600000
    m = ms // 60000 % 60
    s = ms // 1000 % 60
    return f"{h:02}:{m:02}:{s:02},{ms % 1000:03}"

srt = "1\n00:00:01,200 --> 00:00:02,000\nHello.\n\n2\n00:00:02,500 --> 00:00:04,100\nWho's there?\n\n3\n00:00:05,000 --> 00:00:07,750\nIt's me,\nyour neighbour.\n\n4\n00:01:00,000 --> 00:01:02,500\nThe end."
shift = -2300
blocks = srt.split("\n\n")
n = 0
dropped = 0
for b in blocks:
    lines = b.split("\n")
    times = lines[1].split(" --> ")
    start = to_ms(times[0]) + shift
    end = to_ms(times[1]) + shift
    if end <= 0:
        dropped += 1
        continue
    n += 1
    print(f"{n}")
    print(f"{stamp(max(start, 0))} --> {stamp(end)}")
    for t in lines[2:]:
        print(t)
print(f"({dropped} cue(s) dropped, shift {shift} ms)")
