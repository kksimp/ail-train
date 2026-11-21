table = {
    "Closed": {"connect": "SynSent", "listen": "Listen"},
    "Listen": {"syn": "SynReceived"},
    "SynSent": {"synack": "Established"},
    "SynReceived": {"ack": "Established"},
    "Established": {"close": "FinWait1", "fin": "CloseWait"},
    "FinWait1": {"ack": "FinWait2"},
    "FinWait2": {"fin": "TimeWait"},
    "CloseWait": {"close": "LastAck"},
    "LastAck": {"ack": "Closed"},
    "TimeWait": {"timeout": "Closed"},
}

def run(label, events):
    s = "Closed"
    trail = []
    for ev in events:
        if ev in table[s]:
            s = table[s][ev]
            trail.append(s)
        else:
            trail.append(f"[{ev} not allowed in Tcp.{s}]")
    print(f"{label}: {' > '.join(trail)}")

run("client", ["connect", "synack", "close", "ack", "fin", "timeout"])
run("server", ["listen", "syn", "ack", "fin", "close", "ack"])
run("broken", ["connect", "ack", "synack", "listen", "fin"])
