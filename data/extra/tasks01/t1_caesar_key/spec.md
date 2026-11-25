# Caesar / ROT cipher by key line

The first input line is the key line: `enc K` or `dec K`, where K is an integer (an optional `-` and digits; it may be
negative or larger than 26). Every following line is text to transform.

`enc` shifts each ASCII letter forward by K positions in the alphabet, wrapping around; `dec` shifts it backward by K.
Upper and lower case are kept; every other character (digits, spaces, punctuation) is left unchanged. Print each
text line transformed, one output line per input line.

If the input is empty, or the key line is not exactly one of the two words followed by one space and a valid
integer, print `bad key` and nothing else.

Example input:

    enc 3
    Hello, World!
    xyz ABC 123

Example output:

    Khoor, Zruog!
    abc DEF 123

`enc 13` is ROT13 (and is its own inverse); `dec -3` equals `enc 3`.
