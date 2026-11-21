def marker(ext):
    return {"py": "#", "sh": "#", "sql": "--"}.get(ext, "//")

files = [("app.py", "import os\n\n# entry point\ndef main():\n    print(1)  # inline\n"), ("util.js", "// helpers\n/* block\n   comment */\nfunction f() {\n\n  return 1\n}\n"), ("setup.sh", "#!/bin/sh\n# install\necho hi\n"), ("query.sql", "-- totals\nSELECT 1;\n\n"), ("main.js", "const x = 1 // one\n\n")]
stats = {}
for name, text in files:
    ext = name.split(".")[1]
    mark = marker(ext)
    in_block = False
    counts = list(stats.get(ext, [0, 0, 0, 0]))
    counts[0] += 1
    for raw in text.splitlines():
        line = raw.strip()
        if in_block:
            counts[2] += 1
            if "*/" in line:
                in_block = False
        elif line == "":
            counts[1] += 1
        elif line.startswith(mark):
            counts[2] += 1
        elif mark == "//" and line.startswith("/*"):
            counts[2] += 1
            in_block = "*/" not in line
        else:
            counts[3] += 1
    stats[ext] = counts
print("lang  files blank comment code")
total = [0, 0, 0, 0]
for ext in sorted(stats.keys()):
    c = stats[ext]
    print(f"{ext:<5} {c[0]:>5} {c[1]:>5} {c[2]:>7} {c[3]:>4}")
    for i in range(4):
        total[i] += c[i]
print(f"total {total[0]:>5} {total[1]:>5} {total[2]:>7} {total[3]:>4}")
