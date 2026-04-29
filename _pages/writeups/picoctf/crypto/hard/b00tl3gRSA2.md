---
layout: terminal_centered
title: b00tl3gRSA2
permalink: /writeups/picoctf/crypto/hard/b00tl3gRSA2/
date: 2026-04-28
category: writeups
---

# Challenge Description
**Author:** invisibility  
**Description**  
In RSA d is a lot bigger than e, why don't we use d to encrypt instead of e?  
Additional details will be available after launching your challenge instance.  

Hint 1: What is e generally?  

### Writeup 
Once we start the instance and connect to the netcat given. We are provided with N, e and c.  
The e is unsually large, to decrypt we need to find d. A big e usually means that the d is small.  
Hence, we can use Weiner's Attack in order to recover the d as it is small.  