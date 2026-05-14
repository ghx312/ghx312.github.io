---
layout: terminal_centered
title: Echo Escape 1
permalink: /writeups/picoctf/pwn/medium/echoescape1
date: 2026-05-14
category: writeups
---

# Description  
**Author:** Yahaya Meddy  
**Description**  
The "secure" echo service welcomes you politely… but what if you don’t stay polite? Can you make it reveal the hidden flag? You can download the program file [here]() and source [code]().  

Hint 1: Why is the program using a buffer of size 32 but reading up to 128 bytes?  
Hint 2: Can you redirect the program’s execution flow?  

### Writeups  
From the programme, we can see that the buffer is only 32 bytes, but the read function reads up to 128 bytes. This allows us have a buffer overflow vulnerability. Using this we can find the offset of read() to ret. We can also find the address of the win function and perform a simple ret2win using the information.  

### Solve Script  
[Solve Script]()