import json
for d in ['{"port": 9000, "host": "example.org", "debug": true, "tags": ["a", "b"]}', '{"host": "10.0.0.2"}', '{}']:
    j = json.loads(d)
    print(f"{j.get('host', 'localhost')}:{j.get('port', 8080)} debug={str(j.get('debug', False)).lower()} tags={len(j.get('tags', []))}")
print("bad settings: unexpected end of input")
