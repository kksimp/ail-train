import base64
for s in ["Man", "Ma", "M", "hello world", "AIL"]: print(f"{s} -> {base64.b64encode(s.encode()).decode()}")
