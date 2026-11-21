drives = [("conveyor", 1.5, 1440.0, [5.0, 4.0]), ("mixer", 4.0, 960.0, [3.0]), ("winch", 2.2, 1420.0, [6.0, 5.0, 2.0]), ("fan", 0.75, 2850.0, [])]
def output(d):
    torque = 9550.0 * d[1] / d[2]
    speed = d[2]
    for r in d[3]:
        torque = torque * r * 0.95
        speed = speed / r
    return (torque, speed)
for d in drives:
    motor = 9550.0 * d[1] / d[2]
    torque, speed = output(d)
    print(f"{d[0]:<9} motor {motor:>6.2f} Nm at {d[2]:>6.1f} rpm -> {torque:>7.1f} Nm at {speed:>6.1f} rpm")
drum = 0.2
t, s = output(drives[0])
pull = t / drum
belt = s * 2.0 * 3.141592653589793 * drum / 60.0
print(f"conveyor drum 0.2 m: pull {pull:.1f} N, belt {belt:.2f} m/s")
