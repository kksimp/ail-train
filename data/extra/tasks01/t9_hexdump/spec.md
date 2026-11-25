# hexdump

Print a hex dump of the bytes of standard input (the text is UTF-8, so non-ASCII characters are several bytes).

The bytes are shown 16 per line. Each line is made of:
- the offset of its first byte as 8 lowercase hex digits;
- two spaces;
- the hex bytes (two lowercase digits each) separated by single spaces, followed by spaces so this field is always 47 characters wide;
- two spaces;
- `|`, then one character per byte (the byte itself if it is a printable ASCII character, codes 32 to 126, otherwise `.`), then `|`.

After the last line print one more line with the total byte count as 8 hex digits. Empty input prints only `00000000`.

Example input (the text `Hi, you!` and a newline, then `é` and a newline):
```
Hi, you!
é
```
Example output:
```
00000000  48 69 2c 20 79 6f 75 21 0a c3 a9 0a              |Hi, you!....|
0000000c
```
(`c3 a9` are the two bytes of `é`; they and the newlines show as `.`.)
