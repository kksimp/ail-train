class Layer:
    def __init__(self, name, values):
        self.name, self.values = name, values

layers = [Layer("default", {"server.port": "8080", "server.host": "127.0.0.1", "log.level": "info", "db.pool": "4", "db.url": "sqlite://dev.db"}), Layer("file", {"server.host": "0.0.0.0", "db.url": "postgres://db/shop", "db.pool": "8"}), Layer("env", {"db.pool": "16", "log.level": "warn"}), Layer("flag", {"log.level": "debug"})]
value = {}
source = {}
overrides = 0
for layer in layers:
    for k, v in layer.values.items():
        if k in value:
            overrides += 1
        value[k] = v
        source[k] = layer.name
for k in sorted(value.keys()):
    print(f"{k:<12} = {value[k]:<20} ({source[k]})")
for layer in layers:
    n = len([s for s in source.values() if s == layer.name])
    print(f"{layer.name:<7} wins {n} key(s)")
print(f"{overrides} overrides")
