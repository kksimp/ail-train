## mustache-like templates
import sys

NAME_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")


def is_name(s):
    return s != "" and all(c in NAME_CHARS for c in s)


class RenderError(Exception):
    pass


def expand(tag, vars_):
    t = tag.strip()
    if "|" in t:
        name, _, default = t.partition("|")
        has_default = True
        default = default.strip()
    else:
        name, has_default, default = t, False, ""
    name = name.strip()
    if not is_name(name):
        raise RenderError("bad tag")
    val = vars_.get(name, "")
    if val != "":
        return val
    if has_default:
        return default
    if name in vars_:
        return ""
    raise RenderError("undefined " + name)


def render(line, vars_):
    out = ""
    pos = 0
    while True:
        a = line.find("{{", pos)
        if a < 0:
            return out + line[pos:]
        b = line.find("}}", a + 2)
        if b < 0:
            raise RenderError("unclosed tag")
        out += line[pos:a] + expand(line[a + 2:b], vars_)
        pos = b + 2


def control(line):
    t = line.strip()
    if t == "{{else}}":
        return ("else", None)
    if t == "{{/if}}":
        return ("end", None)
    if t.startswith("{{#if ") and t.endswith("}}"):
        return ("if", t[6:-2].strip())
    if t.startswith("{{#unless ") and t.endswith("}}"):
        return ("unless", t[10:-2].strip())
    return None


lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
vars_ = {}
k = 0
while k < len(lines) and lines[k] != "---":
    line = lines[k]
    k += 1
    if line.strip() == "":
        continue
    if "=" not in line or not is_name(line.split("=", 1)[0].strip()):
        print("error: definition %d: malformed" % k)
        continue
    n, v = line.split("=", 1)
    vars_[n.strip()] = v
tmpl = lines[k + 1:]
stack = []  # entries: [parent_on, cond, seen_else]


def is_on():
    if not stack:
        return True
    p, c, e = stack[-1]
    return p and (not c if e else c)


for t, line in enumerate(tmpl, 1):
    on = is_on()
    ctl = control(line)
    if ctl:
        kind, name = ctl
        if kind in ("if", "unless"):
            truth = vars_.get(name, "") != ""
            stack.append([on, truth if kind == "if" else not truth, False])
        elif kind == "else":
            if not stack:
                print("error: line %d: unexpected else" % t)
            elif stack[-1][2]:
                print("error: line %d: duplicate else" % t)
            else:
                stack[-1][2] = True
        else:
            if not stack:
                print("error: line %d: unexpected /if" % t)
            else:
                stack.pop()
    elif on:
        try:
            print(render(line, vars_))
        except RenderError as e:
            print("error: line %d: %s" % (t, e))
if stack:
    print("error: unclosed block")
