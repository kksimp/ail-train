# Club membership renewals

Line 1 is `today YYYY-MM` (word `today`, then a year-month). Otherwise print `error: bad date` and stop.
A YYYY-MM is 4 digits, `-`, and a month of exactly 2 digits from 01 to 12.

Each later non-blank line is a member: `NAME PLAN EXPIRY`. PLAN is `monthly`, `quarterly`, `annual` or `life`. EXPIRY is
the last paid month as a YYYY-MM, except that `life` members must have the single character `-` instead (and others
must not). Any other line is skipped and counted.

Months are counted as year x 12 + month. Let D = expiry minus today in months. A `life` member is `active` always.
Others are `lapsed` if D < 0, `expiring` if 0 <= D <= 2, otherwise `active`.
Plans have a term in months and a base fee: monthly 1 / 15, quarterly 3 / 40, annual 12 / 140.
- `active`: renews to `-`, fee 0.
- `expiring`: renews to expiry + term, fee = base fee.
- `lapsed`: renews to today + term; fee = base fee, plus a late surcharge of 10% of it (integer division rounding down)
  if D < -3.

Print one line per member sorted by expiry (earliest first, `life` members last) then NAME (byte order):
`NAME PLAN EXPIRY STATUS RENEWS FEE`, where EXPIRY and RENEWS are YYYY-MM (or `-`).
Then `due: TOTAL (N renewals)` with the sum of fees and the number of non-active members (`1 renewals` is written as is).
Then `skipped: K` if K > 0. If there are no valid members print `no members` instead of the `due` line.

Example: today 2026-05, `amy annual 2026-06` gives `amy annual 2026-06 expiring 2027-06 140` and `due: 140 (1 renewals)`.
