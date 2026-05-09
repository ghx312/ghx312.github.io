---
layout: terminal_centered
title: Buffer Overflow 0
permalink: /writeups/picoctf/pwn/medium/bufferoverflow0
date: 2026-05-10
category: writeups
---

# Challenge Description  
**Author:** Alex Fulton / Palash Oswal  
**Description**  
Let's start off simple, can you overflow the correct buffer? The program is available [here](/assets/downloads/picoctf/pwn/medium/buffer_overflow_0/vuln). You can view source [here](/assets/downloads/picoctf/pwn/medium/buffer_overflow_0/vuln.c).  

Hint 1: How can you trigger the flag to print?  
Hint 2: If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.  
Hint 3: Run man gets and read the BUGS section. How many characters can the program really read?  

### Writeup  
From the code, we can see that as long as we get the binary to segmentation fault, the flag will be printed.  
In order to trigger the segmentation fault, we can use the buf2 within the vuln() function, by having our initial buf be over the length of buf2, we are able to segementation fault, printing the flag.  
Within the code, buf2 is given 16 bytes of memory, however, we have to input more than 28 is due to the extra pointers and instructions we have to overide in the stack to segmentation fault.  
 
### Solve Script  
[Solve Script](/assets/downloads/picoctf/pwn/medium/buffer_overflow_0/exploit.py)  
