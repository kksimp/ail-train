Read shared expenses from standard input, one per line: `payer,amount_cents,p1;p2;...`. The payer paid the whole amount;
it is split equally among the listed participants (the payer need not be one). Fields and names are trimmed. The payer must
be non-empty, the amount an integer >= 1 (digits only), the participant list non-empty with no empty or duplicate
names, and there must be exactly 3 fields. Blank lines are ignored. Any other line prints `line N: invalid` (N is the
1-based line number, blank lines counted) and is skipped.

Splitting: with k participants, each owes amount / k (integer division) and the remainder cents are given one each
to the first (amount % k) participants in the order listed. A person's balance is what they paid minus what they owe,
summed over all valid lines.

After the input print `balances:` then one line `  NAME: B` per person with a non-zero or zero balance, for everybody
seen in a valid line, in alphabetical (byte) order. B is `+12.50` for positive, `-3.05` for negative, `0.00` for zero.
Then print `settlements:` and settle greedily: repeatedly take the debtor owing the most (ties: alphabetically first)
and the creditor owed the most (ties: alphabetically first), print `  D pays C X.XX` for the smaller of the two amounts and
reduce both, until all balances are zero. If there is nothing to settle print `  none`.

Example input:
    ann,3000,ann;bob;cy
    bob,500,ann;bob
Output:
    balances:
      ann: +17.50
      bob: -7.50
      cy: -10.00
    settlements:
      cy pays ann 10.00
      bob pays ann 7.50
