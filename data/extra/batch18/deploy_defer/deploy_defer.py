def deploy(svc, steps, failing):
    print(f"lock {svc}")
    ok = True
    for s in steps:
        if s == failing:
            print(f"  {s} FAILED"); print(f"  logged {s}"); ok = False; break
        print(f"  {s} ok"); print(f"  logged {s}")
    print(f"unlock {svc}")
    return ok
print(f"api deployed: {str(deploy('api', ['build', 'ship'], '')).lower()}")
print(f"web deployed: {str(deploy('web', ['build', 'test', 'ship'], 'test')).lower()}")
print("all deploys attempted")
