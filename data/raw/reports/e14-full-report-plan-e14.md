Void (read the harness, a hidden case or another trial; left out below):
- till-returns ail-tools 3: Bash: cd /private/tmp/trial-rj984mnn/ws/src; cat pricing/pricing.ail; grep -n "fn \|credit" customers/customers.ail; head -c 600 ../.bench/visible.jsonl
- till-returns ail-tools 2: Bash: cd /private/tmp/trial-1qjbktls/ws/src; cat pricing/pricing.ail; grep -n "fn \|Usage\|struct\|enum" cli/cli.ail fields/fields.ail | head -50; ls ../.bench
- till-returns ail-core-card 8: Bash: cd /private/tmp/trial-qa08vvvg/ws/src; cat pricing/*.ail catalog/*.ail fields/fields.ail | head -150; ls ../.bench
- till-returns c 9: Bash: cd /private/tmp/trial-ccxmha0_/src 2>/dev/null; cd /private/tmp/trial-ccxmha0_/ws/src && python3 - <<'E'
import re
def sub(f,a,b,c=1):
    s=open(f).read(
- till-returns rust 4: Bash: cd /private/tmp/trial-gwtnmpjc/ws/src; cat main.rs journal.rs shop.rs orders.rs reports.rs pricing.rs customers.rs fields.rs; ls ../.bench 2>&1 | head
- till-returns ail-tools 6: Bash: cd /private/tmp/trial-bw5bts1x/ws/src; cat pricing/*.ail reports/*.ail catalog/catalog.ail customers/*.ail money/*.ail; ls ../.bench
- till-returns ail-plain 11: Bash: cd /private/tmp/trial-ufkv3egk/ws/src; cat pricing/pricing.ail; head -c 1500 ../.bench/visible.jsonl
- stock-decimal ail-plain 2: Bash: cd /private/tmp/trial-fzg2ipm6/ws/src; for f in main.ail */*.ail; do echo "=== $f"; cat $f; done; ls ../.bench
- stock-decimal ail-plain 5: Bash: cd /private/tmp/trial-po7qt2od/ws/src; for f in main.ail */*.ail; do echo "=== $f"; cat $f; done; ls ../.bench
- stock-locations c 2: Bash: cd /private/tmp/trial-dw47b7nw/ws/src; for f in event.h event.c store.h store.c report.h report.c main.c; do echo "=== $f"; cat $f; done; ls ../.bench
- stock-locations rust 7: Bash: cd /private/tmp/trial-238dxird/ws/src; for f in main event store report; do echo "=== $f"; cat $f.rs; done; ls ../.bench
- stock-locations rust 9: Bash: cd /private/tmp/trial-iipvuil0/ws/src; for f in main event store report; do echo "=== $f"; cat $f.rs; done; ls ../.bench
- stock-locations ail-plain 7: Bash: cd /private/tmp/trial-jryyz3nf/ws/src; for f in main.ail */*.ail; do echo "=== $f"; cat $f; done; ls ../.bench
- stock-locations c 7: Bash: cd /private/tmp/trial-s0nz4x67/ws/src; for f in event.h event.c store.h store.c report.h report.c main.c; do echo "=== $f"; cat $f; done; head -c 1500 ../
- stock-locations c 1: Bash: cd /private/tmp/trial-a74dkh3m/ws/src; cat event.h event.c main.c report.h report.c store.h store.c; ls ../.bench
- stock-locations c 11: Bash: cd /private/tmp/trial-3gidvjll/ws/src; for f in *.h *.c; do echo "=== $f"; cat $f; done; ls ../.bench
- stock-locations rust 2: Bash: cd /private/tmp/trial-rjetjdgq/ws/src; cat main.rs event.rs store.rs report.rs; ls ../.bench
- stock-locations ail-plain 11: Bash: cd /private/tmp/trial-2e0p4_w4/ws/src; for f in main.ail event/event.ail report/report.ail store/store.ail; do echo "=== $f"; cat $f; done; head -c 1500 .
- stock-locations ail-plain 10: Bash: cd /private/tmp/trial-yi2u8y7d/ws/src; cat main.ail report/report.ail event/event.ail store/store.ail; head -c 1500 ../.bench/visible.jsonl

Primary measure: iterations to working code (fewer is better).

| class | arm | trials | correct | first version green | mean versions to green (correct) | mean fix rounds (correct) | builds that rewrote src | scratch compiles per trial | DOCS KB before first write (median) | vs c: 95% interval of the difference | call |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| from scratch | ail-plain | 36 | 36/36 | 27/36 | 1.28 | 0.28 | 9 | 0.00 | 28.0 | +0.08 to +0.42 | lost |
| from scratch | ail-tools | 36 | 36/36 | 27/36 | 1.28 | 0.28 | 0 | 0.00 | 45.6 | +0.08 to +0.44 | lost |
| from scratch | ail-core-card | 36 | 36/36 | 30/36 | 1.19 | 0.19 | 12 | 0.00 | 13.5 | +0.03 to +0.33 | lost |
| from scratch | c | 36 | 36/36 | 35/36 | 1.03 | 0.03 | 0 | 0.00 | 45.9 | - | - |
| from scratch | rust | 36 | 36/36 | 36/36 | 1.00 | 0.00 | 0 | 0.00 | 43.9 | -0.08 to +0.00 | tied |
| change | ail-plain | 90 | 90/90 | 71/90 | 1.22 | 0.22 | 2 | 0.00 | 30.6 | +0.01 to +0.22 | lost |
| change | ail-tools | 93 | 93/93 | 75/93 | 1.20 | 0.20 | 1 | 0.00 | 47.9 | -0.01 to +0.20 | tied |
| change | ail-core-card | 95 | 95/95 | 82/95 | 1.17 | 0.17 | 3 | 0.00 | 16.5 | -0.05 to +0.17 | tied |
| change | c | 91 | 91/91 | 81/91 | 1.11 | 0.11 | 0 | 0.00 | 48.2 | - | - |
| change | rust | 92 | 92/92 | 75/92 | 1.22 | 0.22 | 0 | 0.00 | 46.8 | -0.00 to +0.23 | tied |

A pilot makes no call: its cells are too small; the column is for the full run.

| task | arm | trials | correct | stopped by a cap | median cost USD | median out tokens | median fix rounds | median versions to green | median debug rounds (calls) | median min | interventions | first check clean | median toolchain tokens | median calls to green | used agent tools | median DOCS KB received | median USD cache write / read / output |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| depgraph | ail-plain | 12 | 12/12 | 0 | 0.09 | 2637 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 8/8 | 7.2 | 2.0 | 0/12 | 28.0 | 0.054 / 0.011 / 0.026 |
| depgraph | ail-tools | 12 | 12/12 | 0 | 0.12 | 2854 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 8/9 | 7.2 | 2.0 | 0/12 | 44.5 | 0.075 / 0.016 / 0.029 |
| depgraph | ail-core-card | 12 | 12/12 | 0 | 0.08 | 2676 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 1/12 | 101.8 | 2.0 | 0/12 | 13.3 | 0.039 / 0.010 / 0.027 |
| depgraph | c | 12 | 12/12 | 0 | 0.13 | 4054 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 8/8 | 7.2 | 2.0 | 0/12 | 45.6 | 0.077 / 0.014 / 0.041 |
| depgraph | rust | 12 | 12/12 | 0 | 0.11 | 2872 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 1/1 | 7.2 | 1.0 | 0/12 | 43.2 | 0.072 / 0.012 / 0.029 |
| ledger | ail-plain | 12 | 12/12 | 0 | 0.12 | 3754 | 0.0 | 1.0 | 0.0 | 0.6 | 0 | 2/10 | 313.0 | 4.0 | 0/12 | 27.8 | 0.058 / 0.019 / 0.038 |
| ledger | ail-tools | 12 | 12/12 | 0 | 0.13 | 3582 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 2/2 | 7.2 | 1.5 | 0/12 | 45.5 | 0.079 / 0.019 / 0.036 |
| ledger | ail-core-card | 12 | 12/12 | 0 | 0.10 | 3866 | 0.0 | 1.0 | 0.0 | 0.6 | 0 | 9/12 | 597.7 | 4.0 | 0/12 | 13.1 | 0.044 / 0.016 / 0.039 |
| ledger | c | 12 | 12/12 | 0 | 0.15 | 5164 | 0.0 | 1.0 | 0.0 | 0.7 | 0 | 9/9 | 7.2 | 2.0 | 0/12 | 45.4 | 0.081 / 0.020 / 0.052 |
| ledger | rust | 12 | 12/12 | 0 | 0.12 | 3098 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 1/1 | 7.2 | 1.0 | 0/12 | 44.9 | 0.074 / 0.016 / 0.031 |
| ledger-fix | ail-plain | 12 | 12/12 | 0 | 0.10 | 2236 | 1.0 | 2.0 | 1.0 | 0.4 | 0 | 0/1 | 297.0 | 3.0 | 0/12 | 28.6 | 0.057 / 0.018 / 0.022 |
| ledger-fix | ail-tools | 12 | 12/12 | 0 | 0.11 | 2114 | 0.5 | 1.5 | 0.5 | 0.4 | 0 | 1/3 | 78.0 | 2.0 | 0/12 | 45.2 | 0.078 / 0.017 / 0.021 |
| ledger-fix | ail-core-card | 12 | 12/12 | 0 | 0.06 | 1138 | 0.0 | 1.0 | 0.0 | 0.2 | 0 | 6/6 | 7.2 | 1.5 | 0/12 | 13.2 | 0.038 / 0.010 / 0.011 |
| ledger-fix | c | 12 | 12/12 | 0 | 0.11 | 1820 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 0/0 | 7.2 | 1.0 | 0/12 | 46.2 | 0.078 / 0.013 / 0.018 |
| ledger-fix | rust | 12 | 12/12 | 0 | 0.10 | 1108 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 0/0 | 7.2 | 1.0 | 0/12 | 43.8 | 0.073 / 0.013 / 0.011 |
| stock | ail-plain | 12 | 12/12 | 0 | 0.09 | 2374 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 5/8 | 44.6 | 2.0 | 0/12 | 28.8 | 0.054 / 0.011 / 0.024 |
| stock | ail-tools | 12 | 12/12 | 0 | 0.11 | 2525 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 6/7 | 7.2 | 2.0 | 0/12 | 46.1 | 0.075 / 0.013 / 0.025 |
| stock | ail-core-card | 12 | 12/12 | 0 | 0.07 | 2255 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 11/11 | 82.6 | 2.0 | 0/12 | 14.0 | 0.039 / 0.010 / 0.023 |
| stock | c | 12 | 12/12 | 0 | 0.13 | 3836 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 4/4 | 7.2 | 1.0 | 0/12 | 46.4 | 0.077 / 0.013 / 0.038 |
| stock | rust | 12 | 12/12 | 0 | 0.11 | 2827 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 1/1 | 7.2 | 1.0 | 0/12 | 43.9 | 0.073 / 0.013 / 0.028 |
| stock-bugfix | ail-plain | 12 | 12/12 | 0 | 0.08 | 1138 | 0.0 | 1.0 | 0.0 | 0.2 | 0 | 3/3 | 7.2 | 1.0 | 0/12 | 29.7 | 0.056 / 0.011 / 0.011 |
| stock-bugfix | ail-tools | 12 | 12/12 | 0 | 0.10 | 1226 | 0.0 | 1.0 | 0.0 | 0.2 | 0 | 2/2 | 7.2 | 1.0 | 0/12 | 46.7 | 0.078 / 0.013 / 0.012 |
| stock-bugfix | ail-core-card | 12 | 12/12 | 0 | 0.06 | 1028 | 0.0 | 1.0 | 0.0 | 0.2 | 0 | 8/8 | 7.2 | 2.0 | 0/12 | 14.6 | 0.040 / 0.010 / 0.010 |
| stock-bugfix | c | 12 | 12/12 | 0 | 0.11 | 1436 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 0/0 | 7.2 | 1.0 | 0/12 | 47.3 | 0.081 / 0.013 / 0.014 |
| stock-bugfix | rust | 12 | 12/12 | 0 | 0.10 | 1378 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 1/1 | 7.2 | 1.0 | 0/12 | 46.8 | 0.077 / 0.013 / 0.014 |
| stock-decimal | ail-plain | 10 | 10/10 | 0 | 0.09 | 2018 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 6/6 | 7.2 | 2.0 | 0/10 | 29.9 | 0.058 / 0.015 / 0.020 |
| stock-decimal | ail-tools | 12 | 12/12 | 0 | 0.12 | 2042 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 6/6 | 7.2 | 1.5 | 0/12 | 46.9 | 0.080 / 0.017 / 0.020 |
| stock-decimal | ail-core-card | 12 | 12/12 | 0 | 0.08 | 2007 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 10/10 | 7.2 | 2.0 | 0/12 | 15.5 | 0.045 / 0.013 / 0.020 |
| stock-decimal | c | 12 | 12/12 | 0 | 0.12 | 2248 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 3/3 | 7.2 | 1.0 | 0/12 | 47.4 | 0.083 / 0.017 / 0.022 |
| stock-decimal | rust | 12 | 12/12 | 0 | 0.11 | 1960 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 1/1 | 7.2 | 1.0 | 0/12 | 45.1 | 0.079 / 0.013 / 0.020 |
| stock-locations | ail-plain | 9 | 9/9 | 0 | 0.12 | 3772 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 6/6 | 7.2 | 2.0 | 0/9 | 30.6 | 0.064 / 0.015 / 0.038 |
| stock-locations | ail-tools | 12 | 12/12 | 0 | 0.14 | 3668 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 4/6 | 7.2 | 2.0 | 0/12 | 47.9 | 0.087 / 0.018 / 0.037 |
| stock-locations | ail-core-card | 12 | 12/12 | 0 | 0.10 | 3573 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 5/7 | 7.2 | 2.0 | 0/12 | 16.6 | 0.049 / 0.016 / 0.036 |
| stock-locations | c | 8 | 8/8 | 0 | 0.17 | 5735 | 0.0 | 1.0 | 0.0 | 0.7 | 0 | 3/3 | 7.2 | 1.0 | 0/8 | 48.2 | 0.093 / 0.018 / 0.057 |
| stock-locations | rust | 9 | 9/9 | 0 | 0.14 | 3688 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 3/3 | 7.2 | 1.0 | 0/9 | 46.0 | 0.084 / 0.017 / 0.037 |
| stock-refactor | ail-plain | 12 | 12/12 | 0 | 0.10 | 2998 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 7/11 | 14.4 | 1.5 | 0/12 | 29.6 | 0.061 / 0.013 / 0.030 |
| stock-refactor | ail-tools | 12 | 12/12 | 0 | 0.13 | 2710 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 6/10 | 10.8 | 2.0 | 0/12 | 46.2 | 0.082 / 0.017 / 0.027 |
| stock-refactor | ail-core-card | 12 | 12/12 | 0 | 0.09 | 2726 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 5/10 | 7.2 | 2.0 | 0/12 | 15.1 | 0.046 / 0.013 / 0.027 |
| stock-refactor | c | 12 | 12/12 | 0 | 0.12 | 1928 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 9/10 | 7.2 | 2.0 | 0/12 | 47.2 | 0.083 / 0.013 / 0.019 |
| stock-refactor | rust | 12 | 12/12 | 0 | 0.12 | 1983 | 1.0 | 2.0 | 1.5 | 0.4 | 0 | 5/12 | 160.6 | 3.5 | 0/12 | 45.2 | 0.080 / 0.015 / 0.020 |
| till-bugfix | ail-plain | 12 | 12/12 | 0 | 0.09 | 1272 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 3/3 | 8.0 | 1.0 | 0/12 | 37.6 | 0.064 / 0.012 / 0.013 |
| till-bugfix | ail-tools | 12 | 12/12 | 0 | 0.11 | 1242 | 0.0 | 1.0 | 0.0 | 0.2 | 0 | 7/7 | 8.0 | 2.0 | 0/12 | 54.5 | 0.083 / 0.014 / 0.012 |
| till-bugfix | ail-core-card | 12 | 12/12 | 0 | 0.07 | 1176 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 10/10 | 8.0 | 2.0 | 0/12 | 21.9 | 0.047 / 0.011 / 0.012 |
| till-bugfix | c | 12 | 12/12 | 0 | 0.11 | 1362 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 2/2 | 8.0 | 1.0 | 0/12 | 55.1 | 0.086 / 0.014 / 0.014 |
| till-bugfix | rust | 12 | 12/12 | 0 | 0.11 | 1300 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 0/0 | 8.0 | 1.0 | 0/12 | 52.7 | 0.086 / 0.014 / 0.013 |
| till-rename | ail-plain | 12 | 12/12 | 0 | 0.10 | 1429 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 6/6 | 8.0 | 1.5 | 0/12 | 38.0 | 0.067 / 0.015 / 0.014 |
| till-rename | ail-tools | 12 | 12/12 | 0 | 0.12 | 1382 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 5/5 | 8.0 | 1.0 | 0/12 | 54.5 | 0.089 / 0.018 / 0.014 |
| till-rename | ail-core-card | 12 | 12/12 | 0 | 0.08 | 1330 | 0.0 | 1.0 | 0.0 | 0.3 | 0 | 8/8 | 12.0 | 2.0 | 0/12 | 22.6 | 0.054 / 0.011 / 0.013 |
| till-rename | c | 12 | 12/12 | 0 | 0.12 | 1505 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 3/3 | 16.0 | 1.0 | 0/12 | 55.6 | 0.088 / 0.018 / 0.015 |
| till-rename | rust | 12 | 12/12 | 0 | 0.12 | 1434 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 5/5 | 16.0 | 1.0 | 0/12 | 53.4 | 0.087 / 0.018 / 0.014 |
| till-returns | ail-plain | 11 | 11/11 | 0 | 0.17 | 4209 | 0.0 | 1.0 | 0.0 | 0.6 | 0 | 7/7 | 8.0 | 2.0 | 0/11 | 39.0 | 0.102 / 0.026 / 0.042 |
| till-returns | ail-tools | 9 | 9/9 | 0 | 0.20 | 4320 | 0.0 | 1.0 | 0.0 | 0.6 | 0 | 1/3 | 8.0 | 1.0 | 0/9 | 55.7 | 0.125 / 0.031 / 0.043 |
| till-returns | ail-core-card | 11 | 11/11 | 0 | 0.15 | 3975 | 1.0 | 2.0 | 1.0 | 0.6 | 0 | 4/7 | 91.4 | 2.0 | 0/11 | 24.0 | 0.088 / 0.024 / 0.040 |
| till-returns | c | 11 | 11/11 | 0 | 0.19 | 3684 | 0.0 | 1.0 | 0.0 | 0.6 | 0 | 2/2 | 8.0 | 1.0 | 0/11 | 56.6 | 0.122 / 0.026 / 0.037 |
| till-returns | rust | 11 | 11/11 | 0 | 0.21 | 4575 | 1.0 | 2.0 | 1.0 | 0.7 | 0 | 1/11 | 1348.0 | 3.0 | 0/11 | 54.4 | 0.128 / 0.033 / 0.046 |
commit: 511d5efa314b1298ce2be153f4dd8be90d60f509
