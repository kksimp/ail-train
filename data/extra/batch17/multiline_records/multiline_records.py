def starts_record(line):
    return len(line) > 0 and line[0].isdigit()

def show(n, head, extra):
    frames = len([l for l in extra if l.strip().startswith("at ")])
    print(f"#{n} {head[11:]} ({frames} frames)")
    for l in extra:
        if l.startswith("Caused by: "):
            print(f"   root cause: {l[len('Caused by: '):]}")

lines = ["2025-03-12 10:00:01 INFO server started", "2025-03-12 10:00:05 ERROR request failed", "    at handler.run(handler.py:42)", "    at server.loop(server.py:10)", "Caused by: timeout after 30s", "    at net.read(net.py:7)", "2025-03-12 10:00:09 WARN slow query 1200ms", "2025-03-12 10:00:12 ERROR cannot open file", "    at store.load(store.py:88)", "2025-03-12 10:00:15 INFO shutdown"]
head = ""
extra = []
n = 0
with_trace = 0
for line in lines:
    if starts_record(line):
        if head != "":
            n += 1
            show(n, head, extra)
            if len(extra) > 0:
                with_trace += 1
        head = line
        extra = []
    else:
        extra.append(line)
n += 1
show(n, head, extra)
if len(extra) > 0:
    with_trace += 1
print(f"{n} records from {len(lines)} lines, {with_trace} with traces")
