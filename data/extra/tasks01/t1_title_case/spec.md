# Title-casing rules

Read standard input as lines. Title-case each line and print it, one output line per input line.

A line's words are its runs of non-whitespace characters (spaces and tabs separate words); the output joins the
words with single spaces, so repeated spaces collapse and leading/trailing spaces vanish. A line with no words
prints as an empty line.

Each word is converted as follows:

1. A word that is entirely one of the small words `a an and as at but by for in nor of on or the to up`
   (compared in lower case, with no punctuation attached) becomes all lower case, unless it is the first or the
   last word of the line.
2. Every other word (and a small word in first or last position) is lower-cased, then the first character of each
   hyphen-separated part is upper-cased if it is a letter (`well-known` becomes `Well-Known`). Characters other
   than letters are left alone, so `(the` stays `(the` and `don't` becomes `Don't`.

Example input:

    the lord of the rings
    a tale OF two cities, and a well-known fable
    "stop" -  go to

Example output:

    The Lord of the Rings
    A Tale of Two Cities, and a Well-Known Fable
    "stop" - Go To

(`a` is capitalized only because it is first; `to` because it is last; `"stop"` starts with a quote, which is not a letter.)
