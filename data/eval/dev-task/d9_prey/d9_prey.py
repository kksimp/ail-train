import re
import sys

text = sys.stdin.read().splitlines()
first = text[0] if text else ""
toks = first.split()
if len(toks) != 3 or not all(re.fullmatch(r"[0-9]+", t) for t in toks) or int(toks[2]) > 30:
    print("invalid input")
else:
    prey, pred, steps = (int(t) for t in toks)
    for t in range(1, steps + 1):
        eaten = min(prey, prey * pred // 200)
        prey, pred = prey + prey // 10 - eaten, pred + eaten // 4 - pred // 5
        print(f"step {t}: prey {prey} pred {pred}")
        if prey == 0 or pred == 0:
            if prey == 0 and pred == 0:
                who = "both"
            elif prey == 0:
                who = "prey"
            else:
                who = "predators"
            print(f"{who} extinct")
            break
