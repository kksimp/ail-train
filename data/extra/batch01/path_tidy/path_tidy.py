def tidy(p):
    ab = p.startswith("/")
    parts = []
    for x in p.split("/"):
        if x in ("", "."):
            continue
        if x == "..":
            if not parts or parts[-1] == "..":
                if not ab:
                    parts.append("..")
            else:
                parts.pop()
        else:
            parts.append(x)
    j = "/".join(parts)
    return "/" + j if ab else (j or ".")
for p in ["/home//user/./docs/../pics/", "a/b/../../..", "./x/./y", "/../etc", "", "../../a/b/..", "/"]:
    print(f"'{p}' -> '{tidy(p)}'")
