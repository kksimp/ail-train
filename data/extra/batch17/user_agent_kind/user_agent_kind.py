def browser(ua):
    low = ua.lower()
    if "bot" in low or "spider" in low or "crawl" in low:
        return "bot"
    rules = [("Edg/", "Edge"), ("OPR/", "Opera"), ("Firefox/", "Firefox"), ("Chrome/", "Chrome"), ("Safari/", "Safari"), ("curl/", "curl")]
    for key, name in rules:
        if key in ua:
            return name
    return "other"

def system(ua):
    if "Android" in ua:
        return "Android"
    if "iPhone" in ua or "iPad" in ua:
        return "iOS"
    if "Windows" in ua:
        return "Windows"
    if "Mac OS X" in ua:
        return "macOS"
    if "Linux" in ua:
        return "Linux"
    return "-"

agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36 Edg/120.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15", "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 Version/17.2 Mobile Safari/604.1", "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 Chrome/120.0 Mobile Safari/537.36", "Googlebot/2.1 (+http://www.google.com/bot.html)", "curl/8.4.0"]
counts = {}
for ua in agents:
    b = browser(ua)
    counts[b] = counts.get(b, 0) + 1
    print(f"{b:<8} {system(ua):<8} {ua[:min(40, len(ua))].rstrip()}")
for k in sorted(counts.keys()):
    print(f"{k}: {counts[k]}")
