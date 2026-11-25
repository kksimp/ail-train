# Sentence splitter with statistics

Standard input is free text over several lines. A sentence ends at each `.`, `!` or `?` character.
Cut the whole text (newlines count as ordinary whitespace) at every such character. Each piece is a
sentence if it contains at least one word; pieces without words (for example the empty piece between
`?!` or after the last terminator) are skipped. Text after the final terminator that holds a word
is a last sentence without a terminator. A word is a whitespace-separated token.

For each sentence in order print `N: W words, C chars` where N counts from 1, W is the number of words
and C is the length of the sentence after collapsing all whitespace runs to single spaces and trimming
the ends (the terminator itself is not part of the piece).

After the list print `sentences=S words=T longest=L`, where S is the number of sentences, T the total
words and L the largest word count of any single sentence.

Edge cases: when there are no sentences print only `no sentences`.

Example input:
Hello there.  How
are you?! Fine
thanks

Example output:
1: 2 words, 11 chars
2: 3 words, 11 chars
3: 2 words, 11 chars
sentences=3 words=7 longest=3
