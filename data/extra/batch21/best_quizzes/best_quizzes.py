pupils = [("Aoife", [14, 17, 9, 18, 16, 20, 11], 72, 68), ("Bilal", [12, 0, 15, 13, 0, 16, 14], 65, 59), ("Carys", [19, 18, 20, 17, 19, 15, 20], 88, 91), ("Deon", [8, 10, 7, 12, 9, 11, 6], 55, 47)]

def grade(t):
    return "A" if t >= 700 else ("B" if t >= 600 else ("C" if t >= 500 else "D"))

for name, qs, project, exam in pupils:
    q = sum(sorted(qs, reverse=True)[:5])
    dropped = sorted(qs)[:2]
    t = (q * 30 + project * 30 + exam * 40) // 10
    print(f"{name:<6} quizzes {q}% (dropped [{', '.join(str(x) for x in dropped)}]), project {project}%, exam {exam}%: {t // 10}.{t % 10}% {grade(t)}")
best = max(pupils, key=lambda p: p[3])
print(f"top exam mark: {best[0]} with {best[3]}%")
