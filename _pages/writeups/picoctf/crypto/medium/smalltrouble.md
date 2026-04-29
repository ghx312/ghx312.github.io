---
layout: terminal_centered
title: Small Trouble
permalink: /writeups/picoctf/crypto/medium/smalltrouble
date: 2026-04-29
category: writeups
---

# Challenge Description  
**Author:** Yahaya Meddy  
**Description**  
Everything seems secure; strong numbers, familiar parameters but something small might ruin it all. Can you recover the message?  
Download the [message](/assets/downloads/picoctf/crypto/medium/small%20trouble/message.txt). And source [code](/assets/downloads/picoctf/crypto/medium/small%20trouble/encryption.py)  

Hint 1: This might be a job for Boneh-Durfee.  

### Writeup  
The encryption protocol generates a large prime for d instead of using a traditional fermat prime for e. They then calculate e.  
From the file, we can see that e is relatively the same size as N, this means that d is rather small. The hint tells us to use the Boneh-Durfee attack.  
The Boneh-Durfee attack is an extension of the Wenier's Attack where the conditions for d are more relaxed, allowing it to be slightly bigger.  
However, for this challenge it is possible to still recover d using Wenier's attack.  