class Mmu:
    def __init__(self, table, next_frame):
        self.tlb = []; self.table = table; self.next_frame = next_frame; self.faults = 0; self.tlb_hits = 0
    def translate(self, addr):
        page = addr // 256
        off = addr % 256
        how = ""
        frame = -1
        for i in range(len(self.tlb)):
            if self.tlb[i][0] == page:
                frame = self.tlb[i][1]
                self.tlb.pop(i)
                self.tlb_hits += 1
                how = "TLB hit"
                break
        if frame < 0:
            if page in self.table:
                frame = self.table[page]
                how = "table"
            else:
                frame = self.next_frame
                self.next_frame += 1
                self.table[page] = frame
                self.faults += 1
                how = "page fault"
            if len(self.tlb) == 2:
                self.tlb.pop(0)
        self.tlb.append([page, frame])
        phys = frame * 256 + off
        return f"{addr:x} -> page {page}, offset {off:>3} ({how}) -> {phys:x}"

m = Mmu({0: 5, 1: 9}, 10)
for a in [0x012, 0x1a4, 0x0ff, 0x2c3, 0x105, 0x2ff, 0x330, 0x011, 0x3a0]:
    print(m.translate(a))
print(f"TLB hits {m.tlb_hits}, page faults {m.faults}, frames used {len(m.table)}")
