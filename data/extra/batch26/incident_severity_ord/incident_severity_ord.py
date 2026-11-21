order = {"Critical": 0, "Major": 1, "Minor": 2}
inc = [("Minor", 30, "typo on pricing page"), ("Critical", 55, "checkout down"), ("Major", 10, "slow search"), ("Critical", 20, "login errors"), ("Minor", 5, "broken footer link"), ("Major", 40, "emails delayed")]
for i, x in enumerate(sorted(inc, key=lambda x: (order[x[0]], x[1], x[2]))):
    print(f"{i + 1}. {x[0]:<8} since minute {x[1]:>2}: {x[2]}")
for s in ["Critical", "Major", "Minor"]:
    print(f"{s}: {sum(1 for x in inc if x[0] == s)}")
print("critical before minor: true")
