# Predator-prey model

Simulate a small integer predator-prey population model.

## Input (standard input)

The first line holds three whitespace-separated tokens: `PREY PRED STEPS` (starting prey, starting predators, number of steps). Only the first line is used; any further lines are ignored.

The input is valid only if there are exactly three tokens, each made of decimal digits only (no sign, no decimal point), and `STEPS <= 30`. Otherwise (including empty input) print only `invalid input`. Valid numbers have at most 6 digits.

## Rules

Keep two integers, `prey` and `pred`. For each step `t` from 1 to `STEPS`, using the values from before the step for every term (all divisions are integer division, rounding down):

- `eaten = min(prey, prey * pred / 200)`
- new `prey` = `prey + prey / 10 - eaten`
- new `pred` = `pred + eaten / 4 - pred / 5`

After computing the step print:

```
step T: prey P pred Q
```

with the new values. Then, if the new prey or the new predator count is 0, print one more line and stop the simulation (no further steps):

- `both extinct` if both are 0
- `prey extinct` if only prey is 0
- `predators extinct` if only predators are 0

If `STEPS` is 0, nothing is printed for a valid input.

## Example

Input:

```
200 40 12
```

Output:

```
step 1: prey 180 pred 42
step 2: prey 161 pred 43
step 3: prey 143 pred 43
step 4: prey 127 pred 42
step 5: prey 113 pred 40
step 6: prey 102 pred 37
step 7: prey 94 pred 34
step 8: prey 88 pred 31
step 9: prey 83 pred 28
step 10: prey 80 pred 25
step 11: prey 78 pred 22
step 12: prey 77 pred 20
```
