import re
def tags(t):
    return re.findall(r"<([^>]*)>", t)
def check(text):
    st = []
    for i, t in enumerate(tags(text)):
        if t.endswith("/"):
            continue
        if t.startswith("/"):
            name = t[1:]
            if not st:
                return f"tag {i + 1}: </{name}> closes nothing"
            top = st.pop()
            if top != name:
                return f"tag {i + 1}: </{name}> closes <{top}>"
        else:
            st.append(t.split()[0] if t.split() else t)
    return "balanced" if not st else f"unclosed <{st[-1]}>"
for d in ["<p><b>hi</b> there</p>", "<div><p>text</div></p>", "<ul><li>one<li>two</ul>", "</em>", "<img src=x/><br/><p class=a>ok</p>", "<p>left open"]:
    print(f"{check(d)}: {d}")
print(",".join(tags("<a><b/></a>")))
