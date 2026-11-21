def hu(n):
    U = ["B", "KiB", "MiB", "GiB", "TiB"]
    if n < 1024: return f"{n} B"
    s = float(n); u = 0
    while s >= 1024.0 and u < 4: s /= 1024.0; u += 1
    return f"{s:.1f} {U[u]}"
T = 0
for n, b in [("notes.txt", 812), ("photo.jpg", 3460211), ("song.flac", 31812664), ("backup.tar", 5370000000), ("thumb.png", 20890), ("movie.mkv", 1610612736)]: T += b; print(f"{n:<11} {hu(b):>10}")
print(f"{'total':<11} {hu(T):>10}")
