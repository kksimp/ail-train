# Elevator simulation

Standard input: the first line is `F S`: the number of floors F (floors are 1..F) and the starting floor S. Every following line is a request `T N`:
at time T a rider presses the button for floor N. Request lines may be in any order.

The elevator starts at floor S at time 0, heading up. Time advances in steps of 1; at each time T, in this order:
1. all requests with time T are added to the pending set (duplicates merge);
2. if the current floor is pending it is served: print `t=T floor=N` and remove it;
3. if anything is still pending: when heading up with nothing pending above, or heading down with nothing pending below, reverse direction; then move one floor in the heading direction.
The simulation ends at the first time T that is not before the last request time and has nothing pending after step 2. Finally print `moves=M`, the total number of floors moved.

Request lines that do not read as two integers, or with a floor outside 1..F or a negative time, are ignored. If the first line is not two integers with 1 <= S <= F, print `bad header` and nothing else.
Empty input prints `bad header`.

Example:
    input:  5 1
            0 3
            1 5
            2 2
    output: t=2 floor=3
            t=4 floor=5
            t=7 floor=2
            moves=7
