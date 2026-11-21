def th(r): return r * 0.1 - 20.0
def ga(r): return 15.0 + r * 0.25
def hu(r): return r * 100.0 / 1024.0
frames = [[452, 330, 700], [467, 342, 731], [431, 350, 650]]
for t, f in enumerate(frames):
    print(f"t{t}: temp: {th(f[0]):.1f} C | pressure: {ga(f[1]):.1f} kPa | humidity 2: {hu(f[2]):.1f} %")
temps = [th(f[0]) for f in frames]
print(f"hottest {max(temps):.1f} C over {len(temps)} frames")
