# Palindromic lines report

Read standard input as lines (a final line ending does not start another line). For each line, build its
normalized form: keep only ASCII letters and digits, converted to lower case. A line is a palindrome when its
normalized form is not empty and reads the same forwards and backwards.

For every palindromic line, in input order, print `N: TEXT` where N is its 1-based line number and TEXT is the line
exactly as given. Then print `palindromes: K` with the number of palindromic lines, and `total lines: T`.

If a line number has more than one palindrome, nothing special happens; lines are independent. Blank lines and
lines with no letters or digits are never palindromes but still count in T and in numbering.

Example input:

    A man, a plan, a canal: Panama
    hello
    ---
    Was it a car or a cat I saw?
    ab

Example output:

    1: A man, a plan, a canal: Panama
    4: Was it a car or a cat I saw?
    palindromes: 2
    total lines: 5
