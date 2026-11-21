def strip_comments(lines):
    out = []
    in_block = False
    for line in lines:
        cs = list(line)
        kept = []
        in_str = False
        i = 0
        while i < len(cs):
            c = cs[i]
            nc = cs[i + 1] if i + 1 < len(cs) else ' '
            if in_block:
                if c == '*' and nc == '/':
                    in_block = False
                    i += 2
                else:
                    i += 1
            elif in_str:
                kept.append(c)
                if c == '"':
                    in_str = False
                i += 1
            elif c == '"':
                in_str = True
                kept.append(c)
                i += 1
            elif c == '/' and nc == '/':
                break
            elif c == '/' and nc == '*':
                in_block = True
                i += 2
            else:
                kept.append(c)
                i += 1
        text = "".join(kept).rstrip()
        if text.strip() != "" or line.strip() == "":
            out.append(text)
    return out

src = ["/* config loader", "   written in a hurry */", "int port = 8080; // default", 'char *url = "http://example.com"; /* keep the // */', "", "int retries = /* inline */ 3;", "// int debug = 1;", 'char *s = "/* not a comment */";']
result = strip_comments(src)
for r in result:
    print(f"|{r}")
print(f"{len(src)} lines -> {len(result)} lines")
