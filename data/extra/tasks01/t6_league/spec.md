# League table from results

Standard input: one match result per line, `HOME,AWAY,HG,AG`: two team names (non-empty, no commas) and the goals scored by each side (non-negative integers).
A win is worth 3 points, a draw 1, a loss 0. A line is bad when it does not have exactly four comma-separated fields, a name is empty, a goal count is not a non-negative integer, or HOME equals AWAY.
Bad lines are skipped for the table, and every bad line is reported after the table as `bad line K` (K counts input lines from 1). Blank lines are bad lines.

Print the table first: teams ordered by points (high first), then goal difference (high first), then goals scored (high first), then name (plain byte order).
Each row is `RANK. NAME P W D L GF GA GD PTS` laid out with the format `{rank:>2}. {name:<10} {p:>2} {w:>2} {d:>2} {l:>2} {gf:>3} {ga:>3} {gd:>4} {pts:>3}`
(names longer than 10 characters are not cut). Ranks are consecutive 1, 2, 3, ... even for equal teams. If no good result exists, print nothing for the table.

Example:
    input:  Ajax,Roma,2,1
            Roma,Lyon,0,0
            Ajax,Lyon,1,3
    output:  1. Lyon        2  1  1  0   3   1    2   4
             2. Ajax        2  1  0  1   3   4   -1   3
             3. Roma        2  0  1  1   1   2   -1   1
