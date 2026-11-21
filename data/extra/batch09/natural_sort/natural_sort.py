def natural_key(s):
    out = []
    digits = []
    for c in s:
        if c.isdigit():
            digits.append(c)
        else:
            if digits:
                out.append("".join(digits).rjust(12, '0'))
                digits = []
            out.append(c.lower())
    if digits:
        out.append("".join(digits).rjust(12, '0'))
    return "".join(out)

files = ["file10.txt", "file2.txt", "File1.txt", "file1b.txt", "img12.png", "img2.png", "img100.png", "track 9.mp3", "track 10.mp3", "v1.10.0", "v1.9.2"]
plain = " ".join(sorted(files))
natural = " ".join(sorted(files, key=natural_key))
print(f"plain:   {plain}")
print(f"natural: {natural}")
print(f"key of v1.10.0: {natural_key('v1.10.0')}")
