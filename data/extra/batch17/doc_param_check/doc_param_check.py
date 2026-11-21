def params_of(sig):
    open_at = sig.find("(")
    close_at = sig.rfind(")")
    inner = sig[open_at + 1:close_at]
    if inner.strip() == "":
        return []
    ps = [p.split("=")[0].split(":")[0].strip() for p in inner.split(",")]
    return [p for p in ps if p != "self"]

def documented(doc):
    out = []
    for l in doc:
        t = l.strip()
        if t.startswith(":param "):
            out.append(t[7:].split(":")[0].strip())
    return out

funcs = [("def area(width, height, unit='m'):", [":param width: in metres", ":param height: in metres", ":param unit: label"]), ("def send(self, to: str, body: str, retries=3):", [":param to: address", ":param subject: line", ":param body: text"]), ("def ping():", []), ("def load(path, strict=False):", ["Load a file.", ":param path: where"])]
clean = 0
for sig, doc in funcs:
    ps = params_of(sig)
    ds = documented(doc)
    missing = [p for p in ps if p not in ds]
    extra = [d for d in ds if d not in ps]
    name = sig[4:sig.find("(")]
    if len(missing) == 0 and len(extra) == 0:
        clean += 1
        print(f"{name}: ok ({len(ps)} params)")
    else:
        m = ", ".join(missing)
        e = ", ".join(extra)
        print(f"{name}: undocumented [{m}] unknown [{e}]")
print(f"{clean} of {len(funcs)} functions fully documented")
