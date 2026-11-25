Read sales records from standard input, one per line: `region,month,amount_cents`. Blank lines are ignored.
`region` (trimmed) must be non-empty, `month` an integer 1 to 12, `amount_cents` an integer that may be negative
(a refund). Exactly 3 fields are required. A line that is not valid is counted as skipped.

Print one block per region, regions in alphabetical (byte) order. A block is the line `REGION: TOTAL` followed by one
line `  MM: AMOUNT` (two leading spaces, month zero-padded to 2 digits) for each month in which that region has at
least one valid record, in month order; AMOUNT is the sum for that region and month. Then print
`all regions: TOTAL` and `best month: MM (AMOUNT)` where the month has the largest total over all regions (the
earliest month wins a tie; only months with at least one record count). Then, only if at least one line was skipped,
print `skipped: K`. Money is dollars with two decimals; negative amounts are written `-12.50`.

Example input:
    north,2,10000
    south,2,-250
    north,1,5050
Output:
    north: 150.50
      01: 50.50
      02: 100.00
    south: -2.50
      02: -2.50
    all regions: 148.00
    best month: 02 (97.50)

With no valid records print only `no sales` (followed by the skipped line if any).
