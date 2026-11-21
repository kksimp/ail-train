cfg = {"m": False, "max": 20}
def handle(name, mb):
    if cfg["m"]: return f"{name}: 503 down for maintenance"
    if mb > cfg["max"]: return f"{name}: 413 upload of {mb} MB too large"
    return f"{name}: 200 ok"
print(handle("api", 5)); print(handle("web", 35))
cfg["m"] = True
print(handle("web", 5))
cfg["m"] = False; cfg["max"] = 50
print(handle("api", 35)); print(handle("web", 35))
print("start-of-day copy: maintenance false, limit 20 MB")
