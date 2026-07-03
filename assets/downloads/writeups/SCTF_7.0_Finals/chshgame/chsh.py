#!/usr/bin/env python3
import hashlib
import threading
import math
import os
import random
import socket
import struct
import sys

FLAG   = os.environ.get("FLAG", "sctf{fake_flag}")
ROUNDS = 1000
_WIN   = 0.84

_PHI = [math.pi / 8, 5 * math.pi / 8]
_PSI = [3 * math.pi / 8, -math.pi / 8]


def _seed(token: bytes, n: int) -> bytes:
    return hashlib.sha256(token + struct.pack(">I", n)).digest()


def _measure(s: bytes, x: int) -> int:
    phase = int.from_bytes(s[0:8], "big") / 2**64 * math.tau
    return 0 if math.cos(phase - _PHI[x]) >= 0 else 1


def _correlate(s: bytes, x: int, y: int) -> int:
    a = _measure(s, x)
    r = int.from_bytes(s[8:16], "big") / 2**64
    p = math.cos((_PHI[x] - _PSI[y]) / 2) ** 2
    return a if r < p else 1 - a


def handle(conn: socket.socket, addr):
    print(f"[+] {addr}", flush=True)
    try:
        f = conn.makefile("rwb", buffering=0)

        token = os.urandom(16)

        f.write(
            b"=== Correlation Game ===\n"
            b"\n"
            b"Each round I send you a bit.  You send me a bit back.\n"
            b"I independently produce my own bit from a private input.\n"
            b"You win the round if:  your_bit XOR my_bit == your_input AND my_input\n"
            b"\n"
            b"Win " + f"{int(_WIN * 100)}%".encode() + b" of rounds to receive the flag.\n"
            b"\n"
            + f"sid: {token.hex()}\n".encode()
            + f"rounds: {ROUNDS}\n\n".encode()
        )

        wins = 0

        for i in range(ROUNDS):
            x = random.randint(0, 1)
            y = random.randint(0, 1)

            s = _seed(token, i)
            b = _correlate(s, x, y)

            f.write(f"{x}\n".encode())

            line = f.readline().strip()
            if not line:
                f.write(b"No response.\n")
                return
            try:
                a = int(line)
                if a not in (0, 1):
                    raise ValueError
            except ValueError:
                f.write(b"Expected 0 or 1.\n")
                return

            if (a ^ b) == (x & y):
                wins += 1

        rate = wins / ROUNDS
        f.write(f"\n{wins}/{ROUNDS} ({rate:.4f})\n".encode())

        if rate >= _WIN:
            f.write(f"flag: {FLAG}\n".encode())
        else:
            f.write(b"Not enough.\n")

    except (ConnectionResetError, BrokenPipeError):
        pass
    finally:
        conn.close()
        print(f"[-] {addr}", flush=True)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5337
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("0.0.0.0", port))
        srv.listen(8)
        print(f"[*] :{port}", flush=True)

        while True:
            conn, addr = srv.accept()
            t = threading.Thread(target=handle, args=(conn, addr), daemon=True)
            t.start()

if __name__ == "__main__":
    main()

#https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/entanglement-in-action/chsh-game
#Use the angles given in the chal as the communication and simmulate quantum mechanics to win. 85% WR > 84% WR