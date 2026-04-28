---
layout: terminal_centered
title: b00tl3gRSA3
permalink: /writeups/picoctf/crypto/hard/b00tl3gRSA3
date: 2026-04-28
category: writeups
---

# Challenge Description  
**Author:** invisibility  
**Challenge Description**  
Why use p and q when I can use more?  
Additional details will be available after launching your challenge instance.  

Hint 1: There's more prime factors than p and q, finding d is going to be different.  

### Writeup  
After connecting to the netcat we are given N, e and the ciphertext. In the first hint it says that there are more prime factors that are used than p and q.  
This means that N has multiple prime factors and we have to factor them in order to recover d.  
Using [FactorDB](https://factordb.com/index.php) to lookup the factorised version of the numbers.  
This allowed me to recover totient N as Eucild's Totient function is actually multiplicative, hence we can just multiply all the primes - 1 together to recover Totient N.  
Using this we can find d and recover the flag.  