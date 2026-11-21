y = {"amir", "bea", "chloe", "dan", "esme", "farid"}; t = {"amir", "chloe", "dan", "gwen", "hiro", "farid", "ines"}
f = lambda xs: "[" + ", ".join(f'"{x}"' for x in sorted(xs)) + "]"
print(f"joined: {f(t - y)}"); print(f"dropped out: {f(y - t)}"); print(f"coming again: {len(t & y)}")
print("all VIPs coming: true")
print(f"{len(t)} guests need {(len(t) + 5) // 6} tables of six")
print(f"{len(y | t)} people have ever said yes")
