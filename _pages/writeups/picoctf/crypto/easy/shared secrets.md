---
layout: terminal_centered
title: Shared Secrets
permalink: /writeups/picoctf/crypto/easy/sharedsecrets
date: 2026-04-28
category: writeups
---

# Challenge Description  
**Author:** Yahaya Meddy  
**Description**  
A message was encrypted using a shared secret... but it looks like one side of the exchange leaked something. Can you piece together the secret and get the flag?
Download the [message](/assets/downloads/picoctf/crypto/easy/shared%20secrets/message.txt). And source [code](/assets/downloads/picoctf/crypto/easy/shared%20secrets/encryption.py)  

Hint 1: What do you get if you combine a public key with a known private one?  

### Writeup  
Viewing the encryption file, we can see that this is a classic Diffie-Hellman Key Exchange.  
Looking at the message.txt, we are given g, p, A, b and enc (Ciphertext).  
This is how the Diffie-Hellman Key Exchange works:  
Alice and Bob both agree on a public modulo and generator, in this case, the modulo is p and the generator is g.  
They then each select a secret key that remains secret (a, b), they then use the public modulo and generator to calculate their public keys (A, B).  
They then send each other their private keys and apply their private key on the other person's public key.  
The resultant calculation will be their shared key.  
As we are given one of the private key (b), we can combine it with the other public key (A) in order to receive the shared secret and decrypted the ciphertext.  