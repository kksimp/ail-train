L = ["GET /index.html 200 512", "GET /about 301 0", "POST /api/order 201 88", "GET /missing 404 0", "GET /api/search 500 0", "GET /img/logo.png 200 20480", "PUT /api/user 403 0", "GET /api/report 503 0", "GET /index.html 304 0", "GET /api/order 200 940"]
C = {}; E = []; b = 0
for l in L:
    p = l.split(" "); c = int(p[2]); b += int(p[3]); k = f"{c // 100}xx"; C[k] = C.get(k, 0) + 1
    if c >= 500: E.append(f"{p[1]} ({c})")
for k in sorted(C): print(f"{k}: {C[k]}")
print(f"server errors: {', '.join(E)}"); print(f"{b} bytes sent in {len(L)} requests")
