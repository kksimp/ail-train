Read the first non-blank line of standard input (later lines are ignored): `principal_cents,rate_bp,payment_cents`
where rate_bp is the annual rate in basis points (500 means 5.00% per year) and the payment is the fixed amount paid
each month. All three are integers (trimmed), principal > 0, rate_bp >= 0, payment > 0; exactly 3 fields. If the line
is missing or not valid print `invalid input` and stop.

Each month: interest = (balance * rate_bp + 60000) / 120000 with integer division (monthly interest, rounded half up);
due = balance + interest; the payment made is min(payment, due); principal paid = payment made - interest;
the new balance = due - payment made. Print one line per month:
`N: pay=P interest=I principal=R balance=B` (money in dollars with two decimals, N the month number from 1).
If the payment is not larger than the first month's interest, print only `payment too small` instead of the schedule.
Stop when the balance reaches 0, and then print `months: N`, `total paid: X`, `total interest: Y`.
If the balance is still above 0 after month 36, stop the schedule there and print `not repaid after 36 months`
(no totals).

Example input: `100000,1200,51000`
Output:
    1: pay=510.00 interest=10.00 principal=500.00 balance=500.00
    2: pay=505.00 interest=5.00 principal=500.00 balance=0.00
    months: 2
    total paid: 1015.00
    total interest: 15.00
