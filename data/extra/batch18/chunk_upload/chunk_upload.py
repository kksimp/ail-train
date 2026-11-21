def upload(name, chunks, flaky, bad):
    sent = 0; retries = 0
    for c in range(chunks):
        attempt = 0
        while True:
            if c == bad:
                print(f"{name}: aborted at chunk {c}, server said 413"); return
            if c in flaky and attempt < 2:
                attempt += 1; retries += 1
                if attempt <= 2: continue
                print(f"{name}: gave up, chunk {c} timed out"); return
            sent = c * 64; break
    print(f"{name}: {chunks} chunks, {sent} KB sent, {retries} retries")
upload("photos.zip", 6, [1, 4], -1)
upload("video.mp4", 5, [0], 3)
upload("notes.txt", 2, [], -1)
