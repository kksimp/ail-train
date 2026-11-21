names = ["General works", "Philosophy", "Religion", "Social sciences", "Language", "Science", "Technology", "Arts", "Literature", "History"]

def main_class(c):
    return names[int(c[0])]

books = [("Learning Python", "005.133", "LUT"), ("Brief History of Time", "523.1", "HAW"), ("The Second World War", "940.53", "BEE"), ("Data Structures", "005.73", "WIR"), ("Football Tactics", "796.334", "WIL"), ("Indian Cooking", "641.5954", "JAF"), ("Beloved", "813.54", "MOR"), ("Networks", "302.23", "CAS"), ("Compilers", "005.453", "AHO"), ("Cosmos", "523.1", "SAG"), ("Ethics", "170", "SIN"), ("Usability", "005.2", "NIE")]
shelf = sorted(books, key=lambda b: (b[1], b[2]))
for title, c, author in shelf:
    call = f"{c} {author}"
    print(f"{call:<13} {title:<22} {main_class(c)}")
counts = {}
for title, c, author in shelf:
    k = main_class(c)
    counts[k] = counts.get(k, 0) + 1
busiest = sorted(counts.keys(), key=lambda k: -counts[k])[0]
print(f"{len(counts)} main classes used; busiest: {busiest} ({counts[busiest]} books)")
