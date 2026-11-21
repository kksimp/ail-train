def relative(from_dir, target):
    a = [s for s in from_dir.split("/") if s != ""]
    b = [s for s in target.split("/") if s != ""]
    common = 0
    while common < len(a) and common < len(b) and a[common] == b[common]:
        common += 1
    parts = []
    for i in range(common, len(a)):
        parts.append("..")
    parts.extend(b[common:])
    if len(parts) == 0:
        return "."
    return "/".join(parts)

pairs = [("/home/ana/projects/app/src", "/home/ana/docs/notes.txt"), ("/home/ana", "/home/ana/music/song.mp3"), ("/var/log", "/var/log"), ("/srv/www/site", "/etc/nginx/site.conf"), ("/a/b/c", "/a/b/c/d/e.txt"), ("/data/2024", "/data/2025/jan.csv")]
for from_dir, target in pairs:
    rel = relative(from_dir, target)
    ups = len([s for s in rel.split("/") if s == ".."])
    print(f"{from_dir:<27} -> {rel:<24} ({ups} up)")
