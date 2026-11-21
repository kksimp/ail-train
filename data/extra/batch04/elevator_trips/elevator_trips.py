R = [5, 3, 8, 3, 2, 9, 5, 1, 7, 4, 6]; i = 0; tr = 1; fm = 0
while i < len(R):
    g = R[i:i + 4]; i += len(g); st = sorted(set(g)); fm += 2 * st[-1]
    print(f"trip {tr}: {len(g)} riders, stops {', '.join(map(str, st))}, up to {st[-1]}"); tr += 1
print(f"floors travelled: {fm}")
