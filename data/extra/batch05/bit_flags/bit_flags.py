def sh(p): return "".join(l if p & (1 << (2 - i)) else "-" for i, l in enumerate("rwx"))
p = 6; print(f"start  {sh(p)} {p}"); p |= 1; print(f"+x     {sh(p)} {p}"); p &= ~2; print(f"-w     {sh(p)} {p}"); p ^= 4; print(f"^r     {sh(p)} {p}")
for v in range(8): print(f"{v} = {sh(v)}")
