# Payroll deductions

Each non-blank line of standard input is `NAME GROSS`: an employee name (one word) and the gross pay for the period
in cents (an integer 0..10000000). Per employee, all amounts in cents, each rounded half up:

- pension = 5% of GROSS.
- taxable = GROSS - pension. Income tax is 10% of the first 2000.00 (200000 cents) of taxable plus 20% of the part above
  it; the two parts are rounded separately and added.
- social = 6.2% of GROSS, but only on the first 6000.00 (600000 cents) of GROSS.
- net = GROSS - pension - tax - social.

Lines are numbered by their position in the input (blank lines count in the numbering). A line with the wrong number of
fields, or a non-integer or out-of-range GROSS, is reported as `line K: bad record` and left out. Reports come first, in order.

Then print a header and one tab-separated row per valid employee, in input order, and a TOTAL row (all zeros when there
are no valid employees). Money prints as `DOLLARS.CENTS`:

    name<TAB>gross<TAB>pension<TAB>tax<TAB>social<TAB>net
    NAME<TAB>G<TAB>P<TAB>T<TAB>S<TAB>N
    TOTAL<TAB>sum of each column

Example, input `ann 250000` and `bob x` (tabs shown as TAB):

    line 2: bad record
    nameTABgrossTABpensionTABtaxTABsocialTABnet
    annTAB2500.00TAB125.00TAB275.00TAB155.00TAB1945.00
    TOTALTAB2500.00TAB125.00TAB275.00TAB155.00TAB1945.00
