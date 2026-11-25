# Readability score (integer formula)

Standard input is free text. Replace every `!` and `?` by `.`, then cut the text at every `.`.
A word is a whitespace-separated token that contains at least one ASCII letter (a-z, A-Z).
A sentence is a piece between cuts that contains at least one word.

Syllables of a word: take only its letters, lower-cased; count the maximal runs of consecutive vowels
(`a e i o u y`) in that letter sequence (non-letters inside the token are simply ignored, so they do not
break a run); a word with no vowel run counts as 1 syllable.

Let W = words, S = sentences, Y = syllables (all integers). Compute with integer division:
    a = W * 100 / S
    b = Y * 100 / W
    milli = 206835 - a * 1015 / 100 - b * 846
    score = 0 if milli < 0, otherwise milli / 1000

Level: score >= 90 `very easy`; >= 60 `standard`; >= 30 `difficult`; otherwise `very difficult`.

Output five lines: `words=W`, `sentences=S`, `syllables=Y`, `score=SCORE`, `level=LEVEL`.
If there are no words print only `no words`.

Example input:
The cat sat. Dogs run!

Example output:
words=5
sentences=2
syllables=5
score=119
level=very easy
