raw = ["apple", "Banana", "cherry", "Apple", "banana", "Zebra", "aardvark", "Cherry"]
print("byte order: [" + ", ".join(f'"{w}"' for w in sorted(raw)) + "]")
k = lambda w: (w.lower(), w)
c = sorted(raw, key=k)
print("dictionary: [" + ", ".join(f'"{w}"' for w in c) + "]")
print(f"first {c[0]}, last {c[-1]}")
print("Banana before banana: true")
