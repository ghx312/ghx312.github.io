---
layout: terminal_centered
title: Shift Registers
permalink: /writeups/picoctf/crypto/medium/shiftregisters
date: 2026-05-01
category: writeups
---

# Challenge Description  
**Author:** Philip Thayer  
**Description**
I learned about lfsr today in school so i decided to implement it in my program. It must be safe right? [chall.py](/assets/downloads/picoctf/crypto/medium/shiftregisters/chall.py) [output.txt](/assets/downloads/picoctf/crypto/medium/shiftregisters/output.txt)  

### What is LFSR?  
Started off this challenge by learning about LFSR. Here is a quick summary.  
We start off with an n-bit length string of 1s and 0s. Then we select a set few bits to XOR together.  
For this challenge, the bits used were the 8th, 6th, 5th and 4th, these are known as the taps.  
We XOR these bits together and input the the result into the left of the string and output the last bit on the right of the string.  

Example:  
Original: 01010101  
Calculated Bit: $$0 \oplus 0 \oplus 1 \oplus 0 = 1$$  
We then input this bit into the left and output the rightmost bit.  
Final: 10101010  

Something important to remember is that we cannot recover anything from a string of bits that only contain 0.  

### Writeup  
Having a look at the programme, we can see that it randomly selects it starting point and uses that as the key for encryption.  
It iteratively encrypts all the bits in the flag by XORing with the resulting LFSR of the ranomly selected starting point.  

The vulnerability here is that there are only 255 possible start point (Minusing the fully 0 bit-string)  
Hence, we can bruteforce through all of it.  

### Solve  
Simply try all possible initial states and decrypt, filter outputs that only contain picoCTF{  
[solve.py](/assets/downloads/picoctf/crypto/medium/shiftregisters/shift_registers_solve.py)  
