# checksums

Reads text from standard input and prints two checksums for every line. Each input line (including empty ones, but not the empty piece after the final newline) is taken as its bytes (the lines are ASCII, line ending not included).

For each line print `adler32=AAAAAAAA crc8=CC`:
- Adler-32: start with a = 1 and b = 0; for each byte, a = (a + byte) mod 65521 and then b = (b + a) mod 65521. The checksum is b * 65536 + a, printed as 8 lower-case hexadecimal digits.
- CRC-8 (polynomial 0x07, initial value 0, no reflection, no final xor): for each byte, crc = crc xor byte, then 8 times: if the top bit (0x80) of crc is set, crc = ((crc << 1) xor 0x07) and 0xFF, otherwise crc = (crc << 1) and 0xFF. Printed as 2 lower-case hexadecimal digits.

After all lines, print `lines=N` where N is the number of lines read.

Example input `Wikipedia` (one line) prints
```
adler32=11e60398 crc8=0e
lines=1
```

