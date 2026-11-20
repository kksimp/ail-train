import json
ms = [{"name": "Ivo", "hours": 32, "status": "Active", "lead": None}, {"name": "Pia", "hours": 0, "status": "Away", "lead": "Ivo"}, {"name": "Qin", "hours": 40, "status": "Active", "lead": "Ivo"}]
d = lambda v: json.dumps(v, separators=(",", ":"))
print(d({"team": "infra", "total": sum(m["hours"] for m in ms), "members": ms}))
print(d([m["name"] for m in ms if m["status"] == "Away"]))
print(len(d(ms[0])))
