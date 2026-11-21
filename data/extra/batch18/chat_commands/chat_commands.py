lines = ["hello all", "/nick Juno", "/join #gardening", "anyone grow chillies?", "/me waves", "/join", "/shout", "/leave", "bye"]
nick = "guest"; room = "#lobby"; log = []
for l in lines:
    if l.startswith("/"):
        p = l[1:].split(" ", 1); cmd = p[0]; arg = p[1].strip() if len(p) > 1 else ""
        if cmd == "nick": log.append(f"* {nick} is now {arg}"); nick = arg
        elif cmd == "join":
            if arg.startswith("#"): room = arg; log.append(f"* {nick} joined {room}")
            else: log.append("! join needs a #room")
        elif cmd == "leave": log.append(f"* {nick} left {room}"); room = "#lobby"
        elif cmd == "me": log.append(f"* {nick} {arg}")
        else: log.append(f"! unknown command /{cmd}")
    else: log.append(f"[{room}] {nick}: {l}")
for e in log: print(e)
print(f"{len(log)} lines, ending in {room}")
