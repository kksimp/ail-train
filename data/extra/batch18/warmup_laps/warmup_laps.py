laps = [102, 98, 95, 84, 82, 83, 81, 85, 97, 104]
import itertools
warm = list(itertools.takewhile(lambda t: t > 90, laps))
after = list(itertools.dropwhile(lambda t: t > 90, laps))
ms = list(itertools.takewhile(lambda t: t <= 90, after))
cool = list(itertools.dropwhile(lambda t: t <= 90, after))
print(f"warm-up {warm}"); print(f"main set {ms}"); print(f"cool-down {cool}")
print(f"main set mean {float(sum(ms)) / float(len(ms)):.1f} s, best lap {min(ms)} s")
t = sum(laps)
print(f"session {t // 60} min {t % 60} s over {len(laps)} laps")
