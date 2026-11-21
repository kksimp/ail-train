from collections import deque
free = 3
full = 0
buf = deque()
steps = "CPPCPPPPCCCC"
item = 0
blocked = 0
waiting = []
for st in steps:
    acts = waiting + [st]
    waiting = []
    for k, who in enumerate(acts):
        fresh = k == len(acts) - 1
        if who == 'P':
            if free > 0:
                free -= 1
                item += 1
                buf.append(item)
                full += 1
                print(f"produce {item:>2}  buffer {list(buf)}")
            else:
                waiting.append(who)
                if fresh:
                    blocked += 1
                    print("producer waits: no free slot")
        else:
            if full > 0:
                full -= 1
                got = buf.popleft()
                free += 1
                print(f"consume {got:>2}  buffer {list(buf)}")
            else:
                waiting.append(who)
                if fresh:
                    blocked += 1
                    print("consumer waits: nothing to take")
print(f"{item} produced, {blocked} blocked calls, {len(buf)} left in the buffer")
