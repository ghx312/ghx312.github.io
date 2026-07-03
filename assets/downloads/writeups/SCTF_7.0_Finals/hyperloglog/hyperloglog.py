#https://en.wikipedia.org/wiki/HyperLogLog
from Crypto.Hash import SHA256
from Crypto.Util.number import long_to_bytes
import os 
FLAG = "sctf{REDACTED}"

class HyperLogLog:
    def __init__(self):
        self.m = 16
        self.am = 0.673
        self.M = [0] * self.m 
        self.secret = os.urandom(16)
    def add(self, x):
        h = SHA256.new()
        h.update(self.secret + long_to_bytes(x))
        vl = int(h.hexdigest(), 16)
        idx = vl >> 252
        vl -= idx << 252
        self.M[idx] = max(self.M[idx], 253 - vl.bit_length())
        print(f"Hash value = {vl}, inserted into set {idx}. Number of leading 0s = {253 - vl.bit_length()}.")
    def count(self):
        Z = 0
        for i in range(self.m):
            Z += 2 ** (-self.M[i])
        Z = 1 / Z 
        E = self.am * Z * self.m ** 2
        return round(E, 1)

Counter = HyperLogLog()

print("Try out HyperLogLog!")
print("Insert 20 numbers, and let HyperLogLog estimate the number of distinct values inputted.")
for i in range(20):
    try:
        val = int(input(f"Number {i+1}: "))
        Counter.add(val)
    except:
        print("An error occurred")
        exit(0)

print(f"Estimate: {Counter.count()}")
if Counter.count() >= 1000:
    print("How did this happen...")
    print(FLAG)