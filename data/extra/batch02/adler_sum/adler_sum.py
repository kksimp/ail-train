import zlib
for t in ["Wikipedia", "wikipedia", "", "a", "The quick brown fox jumps over the lazy dog"]:
    print(f"{zlib.adler32(t.encode()):08x}  '{t}'")
print(f"{zlib.adler32(('ab' * 5000).encode()):08x}  ab x 5000")
