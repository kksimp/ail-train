def matches(job, rule):
    for i in range(len(job)):
        if rule[i] != "*" and rule[i] != job[i]:
            return False
    return True

systems = ["linux", "macos", "windows"]
versions = ["3.10", "3.12"]
dbs = ["sqlite", "postgres"]
excludes = [["windows", "*", "postgres"], ["macos", "3.10", "*"]]
includes = [["linux", "3.13-dev", "sqlite"]]
jobs = []
dropped = 0
for os_ in systems:
    for v in versions:
        for db in dbs:
            job = [os_, v, db]
            if any(matches(job, r) for r in excludes):
                dropped += 1
            else:
                jobs.append(job)
jobs.extend(includes)
for i, j in enumerate(jobs):
    print(f"job {i + 1:>2}: {j[0]}-py{j[1]}-{j[2]}")
print(f"{len(systems) * len(versions) * len(dbs)} combinations, {dropped} excluded, {len(includes)} added, {len(jobs)} jobs")
