from client import HammingSECDED

data = [1, 0, 1, 1]
encoded = HammingSECDED.encode_8_4(data)
print(f"Encoded 8-bit Word: {encoded}")

# Inject 1 bit flip
corrupted = list(encoded)
corrupted[2] ^= 1
res = HammingSECDED.decode_8_4(corrupted)
print(f"Decoded with Single Error: {res['status']} | Recovered: {res['data']}")
