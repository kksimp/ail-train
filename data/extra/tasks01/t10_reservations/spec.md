Reservation system with cancellations

The program reads a seat reservation log from standard input and prints one response per command.

Line 1: `seats N` with N from 1 to 50 (seats are numbered 1..N). If it is missing or invalid print `bad header` and stop.
Then one command per line (blank lines are ignored):
- `book NAME SEAT`: reserve a seat.
  - SEAT not an integer in 1..N: print `NAME: invalid seat`.
  - NAME already holds a seat or is on a waiting list: print `NAME: already booked`.
  - Seat free: print `NAME: booked SEAT`.
  - Seat taken: NAME joins that seat's waiting list (first come, first served) and prints `NAME: waitlisted for SEAT`.
- `cancel NAME`:
  - NAME holds a seat: print `NAME: cancelled SEAT`. If that seat has a waiting list, its first person is given the seat
    and `WAITER: promoted to SEAT` is printed on the next line.
  - NAME is waiting: NAME leaves the list and prints `NAME: left waitlist`.
  - Otherwise print `NAME: no reservation`.
- `show`: print `seats:` followed by one ` S=NAME` entry per seat in order, using `-` for a free seat, all on one line.
Any other line (unknown command, wrong number of fields) prints `bad line N`, N being the 1-based line number.

Example input:
```
seats 3
book ann 2
book bob 2
book cy 1
book ann 3
show
cancel ann
cancel zed
show
book dee 9
```
Output:
```
ann: booked 2
bob: waitlisted for 2
cy: booked 1
ann: already booked
seats: 1=cy 2=ann 3=-
ann: cancelled 2
bob: promoted to 2
zed: no reservation
seats: 1=cy 2=bob 3=-
dee: invalid seat
```
