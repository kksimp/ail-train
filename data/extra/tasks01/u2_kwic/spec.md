# Keyword in context

Standard input: line 1 is a keyword, line 2 is a non-negative integer W (the context width), and the
remaining lines are text.

Tokens are the whitespace-separated pieces of the text lines, numbered from 1 over the whole text.
To compare tokens, convert to lower case and strip any leading and trailing characters from the set
`. , ; : ! ? " ' ( )`. The keyword (trimmed, lower-cased, stripped the same way) matches a token if they are equal.

For each matching token in order print `IDX: ` followed by the parts joined with single spaces: up to W
original tokens before it, then the matching token in square brackets `[tok]`, then up to W original tokens after it.
After all hits print `matches=K`. When nothing matches print only `no matches`.

Edge cases:
- Fewer than 2 input lines, or an empty keyword after normalising: print `bad input`.
- Line 2 is not a non-negative integer (after trimming): print `bad width`.

Example input:
cat
1
The cat sat. A Cat, naps.

Example output:
2: The [cat] sat.
5: A [Cat,] naps.
matches=2
