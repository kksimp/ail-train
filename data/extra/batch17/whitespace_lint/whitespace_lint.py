def check(text, limit):
    problems = []
    lines = text.split("\n")
    for i, raw in enumerate(lines):
        n = i + 1
        if i == len(lines) - 1:
            if raw != "":
                problems.append(f"line {n}: no newline at end of file")
            continue
        line = raw
        if line.endswith("\r"):
            problems.append(f"line {n}: CRLF line ending")
            line = line[:-1]
        trimmed = line.rstrip()
        if len(trimmed) < len(line):
            problems.append(f"line {n}: {len(line) - len(trimmed)} trailing whitespace characters")
        tabs = len([c for c in line if ord(c) == 9])
        if tabs > 0:
            problems.append(f"line {n}: {tabs} tab(s)")
        if len(line) > limit:
            problems.append(f"line {n}: {len(line)} characters, limit {limit}")
    return problems

tc = chr(9)
cr = chr(13)
text = f"def total(xs):   \n{tc}return sum(xs)\nprint(total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))\nx = 1{cr}\nok = True\ny = 2 {tc}"
problems = check(text, 40)
for p in problems:
    print(p)
print(f"{len(problems)} problems in {len(text.split(chr(10)))} lines")
clean = check("a = 1\nb = 2\n", 40)
print(f"clean file: {len(clean)} problems")
