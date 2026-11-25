# Integer SIR epidemic

Simulate an epidemic with three groups of people: susceptible (S), infected (I) and recovered (R), day by day, using integer arithmetic only.

## Input (standard input)

Only the first line is used. It holds six whitespace-separated tokens:

```
S I R BETA GAMMA DAYS
```

initial susceptible, infected and recovered counts; the infection rate `BETA` and recovery rate `GAMMA` in percent; and the number of days to simulate. The input is valid only if there are exactly six tokens, each made of decimal digits only (no sign, no decimal point), `BETA <= 100`, `GAMMA <= 100`, `DAYS <= 30` and `S + I + R > 0`. Otherwise (including empty input) print only `invalid input`. Valid numbers have at most 6 digits.

## Rules

Let `N = S + I + R` from the starting values (N never changes). For each day `d` from 1 to `DAYS`, using the values from before the day:

- `new_inf = S * I * BETA / (N * 100)`
- `new_rec = I * GAMMA / 100`
- then `S = S - new_inf`, `I = I + new_inf - new_rec`, `R = R + new_rec`

All divisions are integer division rounding down.

## Output

First print the starting state as day 0, then one line per day, all in the form:

```
day D: S=<s> I=<i> R=<r>
```

Then print:

- `peak infected P at day D`: the largest value of I over days 0 to DAYS, and the earliest day (0 for the start) on which I had that value.
- `ended on day E` where E is the earliest day (0 for the start) on which I was 0; or `still active` if I is never 0.

## Example

Input:

```
990 10 0 60 20 5
```

Output:

```
day 0: S=990 I=10 R=0
day 1: S=985 I=13 R=2
day 2: S=978 I=18 R=4
day 3: S=968 I=25 R=7
day 4: S=954 I=34 R=12
day 5: S=935 I=47 R=18
peak infected 47 at day 5
still active
```
