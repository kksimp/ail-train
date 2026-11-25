# fuel_eff

Write a command-line program that reads a fuel log from standard input and prints the fuel efficiency of each vehicle.

## Input

Zero or more lines. A line is a fill-up record of exactly three whitespace-separated words:

    VEHICLE LITERS KM

`VEHICLE` is any word. `LITERS` is the fuel added (whole litres) and `KM` is the distance driven (whole kilometres). Both must consist only of the digits `0`-`9` (zero is allowed; no sign, no decimals). Numbers never have more than 9 digits. Every other line (blank lines, lines with a different number of words, lines where LITERS or KM is not all digits) is ignored silently.

## Rules

For each vehicle, sum its LITERS and sum its KM over all of its valid records. Vehicles are reported in the order of their first valid record.

Let `t = (litres * 2000 + km) / (2 * km)` using integer division (rounds down); this is litres per 100 km in tenths, rounded half up. The efficiency prints as `t / 10` (integer division), a dot, then `t % 10`. For example `t = 76` prints `7.6` and `t = 5` prints `0.5`.

If the vehicle's total KM is 0 the efficiency prints as `n/a` instead.

## Output

One line per vehicle: `VEHICLE KM LITERS EFFICIENCY` (total km first, then total litres, separated by single spaces). Nothing is printed when there is no valid record (including empty input).

## Example

Input:

    van 40 520
    bike 3 90
    van 35 480
    junk
    truck 0 0
    bike x 10
    bike 2 60
    car 50 -4

Output:

    van 1000 75 7.5
    bike 150 5 3.3
    truck 0 0 n/a
