def parse(raw):
    blank = raw.find("\r\n\r\n")
    if blank < 0:
        return None, "no blank line after headers"
    head = raw[:blank].split("\r\n")
    body = raw[blank + 4:]
    first = head[0].split(" ")
    if len(first) != 3:
        return None, f"bad request line '{head[0]}'"
    if not first[2].startswith("HTTP/"):
        return None, f"bad version {first[2]}"
    headers = {}
    for line in head[1:]:
        at = line.find(":")
        if at < 0:
            return None, f"header without colon: {line}"
        headers[line[:at].strip().lower()] = line[at + 1:].strip()
    try:
        want = int(headers.get("content-length", "0"))
    except ValueError:
        want = -1
    if want != len(body):
        return None, f"body is {len(body)} bytes, header says {want}"
    target = first[1]
    q = target.find("?")
    if q < 0:
        q = len(target)
    query = target[q + 1:] if q < len(target) else ""
    return (first[0], target[:q], query, headers, body), None

crlf = "\r\n"
reqs = [["GET /search?q=tea&page=2 HTTP/1.1", "Host: shop.test", "Accept: text/html", "", ""], ["POST /orders HTTP/1.1", "Host: shop.test", "Content-Type: application/json", "Content-Length: 10", "", "{\"tea\": 2}"], ["POST /orders HTTP/1.1", "Content-Length: 50", "", "short"], ["FETCH /x", "", ""]]
for parts in reqs:
    raw = crlf.join(parts)
    r, err = parse(raw)
    if r is not None:
        method, path, query, headers, body = r
        host = headers.get("host", "?")
        print(f"{method} {path} query '{query}' host {host}, {len(headers)} headers, body '{body}'")
    else:
        print(f"rejected: {err}")
