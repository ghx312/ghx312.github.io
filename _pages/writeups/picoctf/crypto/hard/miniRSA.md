---
layout: terminal_centered
title: miniRSA
permalink: /writeups/picoctf/crypto/hard/miniRSA/
date: 2026-04-28
category: writeups
---

# Challenge Description  
**Author:** speeeday/Danny  
**Description**  
Let's decrypt this.  
Can you decrypt this [ciphertext](/assets/downloads/picoctf/crypto/hard/miniRSA/ciphertext)? Something seems a bit small.  

Hint 1: RSA tutorial  
Hint 2: How could having too small an e affect the security of this 2048 bit key?  
Hint 3: Make sure you don't lose precision, the numbers are pretty big (besides the e value)  

### Writeup  
We are given a file with N, e and the ciphertext. I noticed that the e is equals to 3. This means that this is a small e attack.  
Where the e is small so we are able to take the cube root of the ciphertext and obtain the original plaintext.  

I used gmpy2's iroot function in order to get the exact cube root of the ciphertext. This gives me the original plaintext.  
This challenge felt like a medium at best LOL.  

### Solve Script
Here is the [solve script](/assets/downloads/picoctf/crypto/hard/miniRSA/solve.py) that I used for this challenge