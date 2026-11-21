class Nat:
    def __init__(self, public, next_port):
        self.public = public; self.next_port = next_port; self.out_map = {}; self.in_map = {}
    def outbound(self, src, dst):
        if src not in self.out_map:
            self.out_map[src] = self.next_port
            self.in_map[self.next_port] = src
            self.next_port += 1
        port = self.out_map[src]
        return f"{src} -> {dst} becomes {self.public}:{port} -> {dst}"
    def inbound(self, port, frm):
        if port in self.in_map:
            return f"{frm} -> :{port} delivered to {self.in_map[port]}"
        return f"{frm} -> :{port} dropped, no mapping"

nat = Nat("203.0.113.5", 40000)
print(nat.outbound("192.168.0.10:51000", "93.184.216.34:443"))
print(nat.outbound("192.168.0.11:51000", "93.184.216.34:443"))
print(nat.outbound("192.168.0.10:51000", "93.184.216.34:443"))
print(nat.outbound("192.168.0.12:6000", "8.8.8.8:53"))
print(nat.inbound(40001, "93.184.216.34:443"))
print(nat.inbound(40002, "8.8.8.8:53"))
print(nat.inbound(40007, "198.51.100.9:23"))
print(f"{len(nat.out_map)} mappings in use")
