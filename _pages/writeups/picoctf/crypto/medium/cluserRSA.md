---
layout: terminal_centered
title: Cluster RSA
permalink: /writeups/picoctf/crypto/medium/clusterRSA
date: 2026-04-29
category: writeups
---

# Challenge Description  
**Author:** Yahaya Meddy
**Description** 
A message has been encrypted using RSA, but this time something feels... more crowded than usual. Can you decrypt it?  
Download the [message](/assets/downloads/picoctf/crypto/medium/cluster%20RSA/message.txt).  

Hint 1: RSA usually means two primes... but what if someone got greedy?  
Hint 2: Prime factors decomposition  

### Writeup  
Hint 1 and 2 tells us that the encryption protocol probably uses more than just p and q.  
Hence, we can factor N into its prime factors, I used [factor.db](https://factordb.com/index.php) to factor the number into its prime factors.  
Afterwards, we can simply recover totient N by using Euclid's totient function which is multiplicative, hence, we can do (p - 1)(q - 1)(r - 1)(s - 1)... to recover totient N.  
We can then find the multiplicative inverse of e and recover d to decrypt the message.  