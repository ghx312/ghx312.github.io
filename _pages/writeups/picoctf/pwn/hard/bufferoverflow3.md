---
layout: terminal_centered
title: Buffer Overflow 3
permalink: /writeups/picoctf/pwn/hard/bufferoverflow3
date: 2026-05-11
category: writeups
---

# Challenge Description  
**Author:** Sanjay C / Palash Oswal  
**Description**  
Do you think you can bypass the protection and get the flag?  
It looks like Dr. Oswal added a stack canary to this [program](/assets/downloads/picoctf/pwn/hard/buffer_overflow_3/vuln) to protect against buffer overflows. You can view source [here](/assets/downloads/picoctf/pwn/hard/buffer_overflow_3/vuln.c).  

Hint 1: Maybe there's a smart way to brute-force the canary?  

### Writeups  
For this challenge, there is an unknown canary given to us that is 4 bytes long, the buffer is also has a length of 64.  

The challenge is also different where it allows us to input the amount of bytes we would like to submit. However, a vulnerability is not having a limit on the number we can provide. This allows us to provide more bytes than the given buffer of 64.  

Hence, we can input in 200 as the number of bytes we would like to submit, and we can input in {% raw %} `cyclic 200` {% endraw %}, this of course destroys the canary.  
Looking at the DISASM, we can see the current global canary and we can see the offset of canary from gets()
![Here lies a picture](/assets/downloads/picoctf/pwn/hard/buffer_overflow_3/canary_disasm.png)  
![Here lies another picture](/assets/downloads/picoctf/pwn/hard/buffer_overflow_3/canary_offset.png)  

For this challenge is it important to note that canaries will only trigger and exit if the canary is not intact, this means that instead of simply guessing all of the canary at the same time which is 256 to the power of 4. We can simply guess the first byte and stop overflowing, as if we buffer 64 bytes + 1 byte of the canary, as long as that one byte is correct, the canary will remain intact. Then we bruteforce by guessing the first byte, second, third and fourth. This allows us to find out what the canary is.  

Then we can simply find the offset to the return pointer and override it to return towards the win() function.

### Solve Script
[Solve Script](/assets/downloads/picoctf/pwn/hard/buffer_overflow_3/exploit.py)