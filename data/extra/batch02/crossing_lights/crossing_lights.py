order = ["CarsGo", "CarsAmber", "WalkOn", "WalkFlash"]
dur = {"CarsGo": 6, "CarsAmber": 2, "WalkOn": 4, "WalkFlash": 2}
st = "CarsGo"; left = 6
for t in range(26):
    if t in (3, 20) and st == "CarsGo" and left > 2:
        left = 2; print(f"t{t}: button")
    left -= 1
    if left == 0:
        st = order[(order.index(st) + 1) % 4]; left = dur[st]
        print(f"t{t + 1}: {st}")
