def expose(n, secs):
    print(f"  print {n}: expose {secs} s")
    try:
        if secs > 20:
            print(f"  print {n}: overexposed, binned")
            return False
        return True
    finally:
        print(f"  print {n}: into the wash")
def session(name, times):
    print(f"{name}: safelight on")
    kept = 0
    for i, t in enumerate(times):
        if expose(i + 1, t): kept += 1
    print(f"{name}: safelight off")
    return kept
print(f"kept {session('contact sheet', [8])}")
print(f"kept {session('enlargement', [15, 25])}")
print("darkroom locked")
