for P in [["Gentle rain on the roof", "Over the hills it rolls", "Light returns by noon", "Dawn will bring it again"], ["Silver moon above", "Under quiet trees", "Night birds call softly"], ["Morning comes", "Answers wait", "Pages turn", "Evening falls"]]:
    print(f"down the left: {''.join(l[0] for l in P).upper()}, down the right: {''.join(l[-1] for l in P).upper()}")
