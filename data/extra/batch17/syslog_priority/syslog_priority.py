facs = ["kern", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]
sevs = ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug"]

def pri_of(line):
    if not line.startswith("<"):
        return -1
    close = line.find(">")
    if close < 2:
        return -1
    s = line[1:close]
    if not s.isdigit():
        return -1
    n = int(s)
    if n > 191:
        return -1
    return n

lines = ["<34>su: 'su root' failed for kim on /dev/pts/8", "<165>app: user login ok", "<0>kernel: panic in scheduler", "<86>sshd: session opened for user kim", "<13>backup: nightly job done", "<200>bogus: out of range", "no priority here", "<27>disk: write error on sda1"]
urgent = 0
counts = {}
for line in lines:
    p = pri_of(line)
    if p < 0:
        print(f"invalid: {line}")
        continue
    close = line.find(">")
    msg = line[close + 1:]
    print(f"<{p}> {facs[p // 8]}.{sevs[p % 8]}: {msg}")
    counts[sevs[p % 8]] = counts.get(sevs[p % 8], 0) + 1
    if p % 8 <= 3:
        urgent += 1
parts = [f"{s}={c}" for s, c in counts.items()]
print(f"by severity: {', '.join(parts)}")
print(f"err or worse: {urgent}")
