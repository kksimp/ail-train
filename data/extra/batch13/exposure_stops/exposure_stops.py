shutters = ["1/30", "1/40", "1/50", "1/60", "1/80", "1/100", "1/125", "1/160", "1/200", "1/250", "1/320", "1/400", "1/500", "1/640", "1/800", "1/1000"]
apertures = ["2.8", "3.2", "3.5", "4", "4.5", "5", "5.6", "6.3", "7.1", "8", "9", "10", "11"]
isos = [100, 125, 160, 200, 250, 320, 400, 500, 640, 800]
base_s = shutters.index("1/125")
base_a = apertures.index("8")
base_i = 0
print(f"metered: {shutters[base_s]} s at f/{apertures[base_a]}, ISO {isos[base_i]}")
for wanted in ["5.6", "4", "2.8", "11"]:
    a = apertures.index(wanted)
    thirds = base_a - a
    s = base_s + thirds
    if 0 <= s < len(shutters):
        print(f"f/{wanted:<4} {thirds:>3} thirds brighter -> {shutters[s]} s at ISO {isos[base_i]}")
    else:
        iso_shift = -s if s < 0 else 0
        print(f"f/{wanted:<4} off the shutter scale, needs {iso_shift} thirds more ISO")
for wanted_iso in [400, 800]:
    steps = isos.index(wanted_iso)
    s = base_s + steps
    print(f"ISO {wanted_iso}: {steps} thirds more light -> {shutters[s]} s at f/8")
