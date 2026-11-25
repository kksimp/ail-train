# Packet reassembly

Reassemble fragmented messages from packets that arrive in any order.

Input: one packet per line, `ID SEQ TOTAL PAYLOAD` (exactly four words): ID is a message name, SEQ the fragment index and TOTAL the number of
fragments in the message (integers, TOTAL >= 1, 0 <= SEQ < TOTAL), PAYLOAD a word. Blank lines are ignored.
A line is malformed if it does not have four words, if a number is invalid or out of range, or if its TOTAL differs from the TOTAL of the
first valid packet seen for that ID. Malformed lines are counted and otherwise ignored.
If a valid packet repeats a (ID, SEQ) pair already received it is a duplicate: counted, and the first payload is kept.

Output: one line per message ID, in order of first valid packet.
- All fragments present: `ID complete data=P0P1...` (payloads concatenated in SEQ order, no separators).
- Otherwise: `ID incomplete have=H/T missing=S1,S2,...` (H distinct fragments received, T = TOTAL, missing indexes ascending).
Last line: `malformed=M duplicates=D`.

Example input:
    m1 1 3 lo
    m1 0 3 hel
    m2 0 1 x
    m1 1 3 zz
    m1 2 3 !
Output:
    m1 complete data=hello!
    m2 complete data=x
    malformed=0 duplicates=1
