R = [23, 25, -1, 22, 31, 24, -1, 26, 58, 25, 24, 23]; P = [r for r in R if r >= 0]
print(f"{len(R)} sent, {len(P)} received, {(len(R) - len(P)) * 100 // len(R)}% loss")
print(f"min {min(P)} ms, avg {sum(P) / len(P):.1f} ms, max {max(P)} ms, jitter {sum(abs(P[i] - P[i - 1]) for i in range(1, len(P))) / (len(P) - 1):.2f} ms")
