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
| held out | ail-plain | 36 | 36/36 | 29/36 | 1.42 | 0.47 | 3 | 0.00 | 28.2 | -0.00 to +0.64 | tied |
| held out | ail-tools | 36 | 24/36 | 24/36 | 1.08 | 0.08 | 3 | 0.00 | 45.8 | -0.17 to +0.14 | tied |
| held out | ail-core-card | 36 | 31/36 | 23/36 | 1.29 | 0.29 | 4 | 0.39 | 13.5 | -0.01 to +0.37 | tied |
| held out | c | 36 | 35/36 | 32/36 | 1.11 | 0.11 | 0 | 0.00 | 45.9 | - | - |
| held out | rust | 36 | 33/36 | 36/36 | 1.00 | 0.00 | 0 | 0.00 | 43.9 | -0.23 to -0.03 | tied |

A pilot makes no call: its cells are too small; the column is for the full run.

| task | arm | trials | correct | stopped by a cap | median cost USD | median out tokens | median fix rounds | median versions to green | median debug rounds (calls) | median min | interventions | first check clean | median toolchain tokens | median calls to green | used agent tools | median DOCS KB received | median USD cache write / read / output |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| calc | ail-plain | 12 | 12/12 | 0 | 0.14 | 5604 | 1.0 | 2.0 | 1.0 | 0.8 | 0 | 3/10 | 662.0 | 4.0 | 0/12 | 28.3 | 0.063 / 0.020 / 0.056 |
| calc | ail-tools | 12 | 0/12 | 0 | 0.16 | 5206 | 1.0 | 2.0 | 1.0 | 0.8 | 0 | 1/7 | 790.6 | 3.5 | 0/12 | 46.3 | 0.085 / 0.024 / 0.052 |
| calc | ail-core-card | 12 | 7/12 | 0 | 0.11 | 4880 | 1.0 | 2.0 | 1.0 | 0.7 | 0 | 4/11 | 1419.4 | 5.5 | 0/12 | 13.6 | 0.050 / 0.016 / 0.049 |
| calc | c | 12 | 11/12 | 0 | 0.15 | 5175 | 0.0 | 1.0 | 0.0 | 0.7 | 0 | 6/6 | 7.2 | 1.0 | 0/12 | 45.9 | 0.081 / 0.014 / 0.052 |
| calc | rust | 12 | 9/12 | 0 | 0.13 | 4242 | 0.0 | 1.0 | 0.0 | 0.5 | 0 | 3/3 | 7.2 | 1.0 | 0/12 | 45.3 | 0.076 / 0.013 / 0.042 |
| invjson | ail-plain | 12 | 12/12 | 0 | 0.10 | 2640 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 8/9 | 766.1 | 4.0 | 0/12 | 28.2 | 0.056 / 0.018 / 0.026 |
| invjson | ail-tools | 12 | 12/12 | 0 | 0.12 | 2739 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 4/7 | 7.2 | 2.0 | 0/12 | 45.8 | 0.075 / 0.013 / 0.027 |
| invjson | ail-core-card | 12 | 12/12 | 0 | 0.08 | 2749 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 6/10 | 887.8 | 5.0 | 0/12 | 13.5 | 0.042 / 0.013 / 0.028 |
| invjson | c | 12 | 12/12 | 0 | 0.13 | 4380 | 0.0 | 1.0 | 0.0 | 0.6 | 0 | 6/6 | 7.2 | 2.0 | 0/12 | 45.8 | 0.077 / 0.013 / 0.044 |
| invjson | rust | 12 | 12/12 | 0 | 0.11 | 2750 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 2/2 | 7.2 | 1.0 | 0/12 | 43.8 | 0.073 / 0.012 / 0.028 |
| maze | ail-plain | 12 | 12/12 | 0 | 0.09 | 2540 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 7/7 | 7.2 | 2.0 | 0/12 | 27.9 | 0.053 / 0.011 / 0.025 |
| maze | ail-tools | 12 | 12/12 | 0 | 0.12 | 2682 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 10/12 | 7.2 | 2.0 | 0/12 | 44.5 | 0.074 / 0.015 / 0.027 |
| maze | ail-core-card | 12 | 12/12 | 0 | 0.07 | 2629 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 11/11 | 42.6 | 2.0 | 0/12 | 13.2 | 0.038 / 0.010 / 0.026 |
| maze | c | 12 | 12/12 | 0 | 0.11 | 2918 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 9/9 | 7.2 | 2.0 | 0/12 | 45.7 | 0.073 / 0.012 / 0.029 |
| maze | rust | 12 | 12/12 | 0 | 0.11 | 2908 | 0.0 | 1.0 | 0.0 | 0.4 | 0 | 0/0 | 7.2 | 1.0 | 0/12 | 43.3 | 0.073 / 0.012 / 0.029 |
commit: 511d5efa314b1298ce2be153f4dd8be90d60f509
