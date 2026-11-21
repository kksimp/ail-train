def blob_id(content):
    h = 7
    for c in content:
        h = (h * 131 + ord(c)) % 1000003
    return h

commits = [[["README", "hello"], ["main.c", "int main v1"], ["util.c", "helpers"]], [["README", "hello"], ["main.c", "int main v2"], ["util.c", "helpers"]], [["README", "hello world"], ["main.c", "int main v2"], ["util.c", "helpers"], ["old_main.c", "int main v1"]], [["README", "hello world"], ["main.c", "int main v3"], ["lib/util.c", "helpers"]]]
store = {}
written = 0
for n, files in enumerate(commits):
    fresh = 0
    parts = []
    for f in files:
        i = blob_id(f[1])
        written += 1
        if i not in store:
            store[i] = f[1]
            fresh += 1
        parts.append(f"{f[0]}:{i:x}")
    print(f"commit {n + 1}: {fresh} new blob(s) | {' '.join(parts)}")
total = sum(len(s) for s in store.values())
print(f"files written {written}, blobs stored {len(store)}, {total} bytes kept")
