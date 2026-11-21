h = [12, 15, 11, 9, 18, 14, 13, 7, 6, 10, 16, 12]
mx = [max(h[i:i + 3]) for i in range(len(h) - 2)]
print(f"hourly heights: {h}")
print(f"3-hour maxima:  {mx}")
calm = [f"{i:02}:00-{i + 3:02}:00" for i, m in enumerate(mx) if m < 15]
print(f"small boats may go out: {', '.join(calm)}")
print(f"worst window peak {max(mx)} dm")
