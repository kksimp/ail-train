songs = ["intro", "rain", "drive", "glow", "echo", "outro"]
for k in [0, 1, 2, 6, 8]:
    n = k % len(songs)
    a = songs[n:] + songs[:n]
    print(f"left {k}: {' '.join(a)} ok")
n = (len(songs) - 2) % len(songs)
print("right 2: " + " ".join(songs[n:] + songs[:n]))
print(" ".join(songs))
