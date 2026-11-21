import math
PI = 3.141592653589793

def snr_db(bits, n):
    levels = math.pow(2.0, float(bits - 1)) - 1.0
    sig = 0.0
    noise = 0.0
    for i in range(n):
        x = math.sin(2.0 * PI * 37.3 * float(i) / float(n))
        q = math.floor(x * levels + 0.5) / levels
        sig += x * x
        noise += (x - q) * (x - q)
    return 10.0 * math.log10(sig / noise)

for bits in [4, 6, 8, 10, 12, 16]:
    measured = snr_db(bits, 1000)
    theory = 6.02 * float(bits) + 1.76
    print(f"{bits:>2} bits: measured {measured:.1f} dB, rule of thumb {theory:.1f} dB")
print(f"CD audio (16 bits) gives about {6.02 * 16.0 + 1.76:.0f} dB of range")
