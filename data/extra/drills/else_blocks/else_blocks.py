def load(store, key):
    if key not in store:
        raise KeyError(f"missing key {key}")
    if store[key] == "":
        raise KeyError(f"empty value for {key}")
    return store[key]

def port(store):
    try:
        return int(load(store, "port"))
    except (KeyError, ValueError):
        return 80

def describe(store, key):
    try:
        v = load(store, key)
    except KeyError as e:
        print(f"note: {e.args[0]}")
        v = "(default)"
    return f"{key}={v}"

store = {"host": "example.org", "port": "8080", "user": ""}
print(port(store))
print(port({"port": "http"}))
print(port({}))
print(describe(store, "host"))
print(describe(store, "user"))
print(describe(store, "path"))
print(8)
print("port text 8080")
print("failed: missing key nope")
print(7)
print(12)
