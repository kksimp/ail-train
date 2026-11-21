hits = ["kettle", "toaster", "blender", "mixer", "scale", "grinder", "juicer"]
def count(items, size): return (len(items) + size - 1) // size
def page(items, size, n):
    start = (n - 1) * size
    return items[start:min(start + size, len(items))]
print(f"{len(hits)} hits on {count(hits, 3)} pages")
for n in range(1, count(hits, 3) + 1):
    more = "more" if n < count(hits, 3) else "end"
    print(f"page {n}: {', '.join(page(hits, 3, n))} ({more})")
orders = [1042, 1043, 1050, 1061, 1077]
last = page(orders, 2, count(orders, 2))
print(f"orders: {count(orders, 2)} pages, last page {last}")
print(f"empty search: {count([], 4)} pages")
