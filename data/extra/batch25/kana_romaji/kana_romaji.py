def table():
    rows = [("あいうえお", "a i u e o"), ("かきくけこ", "ka ki ku ke ko"), ("がぎぐげご", "ga gi gu ge go"), ("さしすせそ", "sa shi su se so"), ("ざじずぜぞ", "za ji zu ze zo"), ("たちつてと", "ta chi tsu te to"), ("だでど", "da de do"), ("なにぬねの", "na ni nu ne no"), ("はひふへほ", "ha hi fu he ho"), ("ばびぶべぼ", "ba bi bu be bo"), ("まみむめも", "ma mi mu me mo"), ("やゆよ", "ya yu yo"), ("らりるれろ", "ra ri ru re ro"), ("わを", "wa o")]
    m = {}
    for kana, roman in rows:
        romans = roman.split(" ")
        for i, k in enumerate(kana):
            m[k] = romans[i]
    return m

def romanise(word, m):
    small = {'ゃ': "a", 'ゅ': "u", 'ょ': "o"}
    out = []
    double = False
    for i, c in enumerate(word):
        r = ""
        if c == 'っ':
            double = True
            continue
        elif c in small:
            prev = out.pop() if out else ""
            stem = prev[:len(prev) - 1]
            glide = "y" if len(stem) == 1 and stem != "j" else ""
            r = f"{stem}{glide}{small[c]}"
        elif c == 'ん':
            nxt = word[i + 1] if i + 1 < len(word) else ' '
            r = "n'" if nxt in "あいうえおやゆよ" else "n"
        else:
            r = m.get(c, "?")
        if double:
            lead = "t" if r.startswith("ch") else r[0:1]
            r = f"{lead}{r}"
            double = False
        out.append(r)
    return "".join(out)

m = table()
words = ["さくら", "きょうと", "しんぶん", "がっこう", "まっちゃ", "きんようび", "ふじさん", "ちゅうしゃ", "じゃま", "ほっかいどう"]
for w in words:
    print(f"{w}: {romanise(w, m)}")
print(f"{len(m)} kana in the table")
