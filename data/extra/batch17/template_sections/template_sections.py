def render(t, vars, lists):
    open_ = "{{"
    shut = "}}"
    out = []
    rest = t
    while True:
        at = rest.find(open_)
        if at < 0:
            out.append(rest)
            break
        out.append(rest[:at])
        after = rest[at + 2:]
        close = after.find(shut)
        if close < 0:
            close = len(after)
        tag = after[:close]
        rest = after[min(close + 2, len(after)):]
        if tag.startswith("#") or tag.startswith("^"):
            name = tag[1:]
            end_tag = open_ + "/" + name + shut
            end = rest.find(end_tag)
            if end < 0:
                end = len(rest)
            body = rest[:end]
            rest = rest[min(end + len(end_tag), len(rest)):]
            items = lists.get(name, [])
            if tag.startswith("#"):
                for it in items:
                    inner = dict(vars)
                    inner["."] = it
                    out.append(render(body, inner, lists))
            elif len(items) == 0:
                out.append(render(body, vars, lists))
        else:
            out.append(vars.get(tag, ""))
    return "".join(out)

t = "Order for {{name}}:\n{{#items}}  - {{.}} ({{shop}})\n{{/items}}{{^items}}  nothing yet\n{{/items}}Thanks, {{name}}!"
print(render(t, {"name": "Ana", "shop": "Corner"}, {"items": ["bread", "milk", "eggs"]}))
print(render(t, {"name": "Ben", "shop": "Corner"}, {"items": []}))
