# Savings goal months

Each non-blank line of standard input is one scenario: `GOAL START DEPOSIT RATE`, four integers.
GOAL, START and DEPOSIT are in cents, RATE is the annual rate in basis points.
Valid: GOAL 1..1000000000, START 0..1000000000, DEPOSIT 0..1000000000, RATE 0..2000, exactly four integers.

Each month, in this order: monthly interest is added, then the deposit is added.
Monthly interest is `balance * RATE / 120000` in cents (annual rate divided by 12), rounded half up, computed on the
balance at the start of the month. Count the months until the balance is at least GOAL.
If START is already at least GOAL the answer is 0 months. If the goal is not reached within 600 months,
the scenario is unreachable.

Scenarios are numbered 1, 2, ... counting only non-blank lines (a blank line is empty or only spaces and is skipped).
Output one line per scenario:

    scenario K: N months, balance B
    scenario K: unreachable in 600 months
    scenario K: bad input

Money prints as `DOLLARS.CENTS` with two digits of cents. Empty input prints nothing.

Example, input:

    100000 0 20000 0
    100000 0 0 500
    abc

Output:

    scenario 1: 5 months, balance 1000.00
    scenario 2: unreachable in 600 months
    scenario 3: bad input
