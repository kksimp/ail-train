function_words = {"a", "an", "the", "and", "or", "but", "of", "to", "in", "on", "at", "for", "with", "by", "from", "is", "are", "was", "were", "be", "been", "it", "i", "you", "he", "she", "we", "they", "that", "this", "so", "do", "did", "not", "just", "then", "there", "what", "my", "your", "its", "will", "shall", "any", "all", "as", "if", "me", "oh", "well", "yeah", "like"}
texts = [("news", "Heavy rainfall flooded several coastal towns overnight and emergency crews evacuated hundreds of residents"), ("chat", "oh well I did not think that it was there so I just went in and it was like what"), ("legal", "The tenant shall maintain the premises in good repair and shall not sublet any part without written consent"), ("recipe", "Whisk the eggs with sugar until pale then fold in sifted flour and bake for twenty minutes"), ("poem", "So we will go no more a roving so late into the night")]
for label, text in texts:
    words = text.lower().split()
    content = [w for w in words if w not in function_words]
    density = len(content) / len(words) * 100.0
    longest = sorted(content, key=lambda w: -len(w))[0]
    print(f"{label:<7} {len(content):>2}/{len(words):<2} words = {density:>5.1f}% content, longest {longest}")
