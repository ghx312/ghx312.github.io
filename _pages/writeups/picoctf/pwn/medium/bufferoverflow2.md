---
layout: terminal_centered
title: Buffer Overflow 2
permalink: /writeups/picoctf/pwn/medium/bufferoverflow2
date: 2026-05-11
category: writeups
---

# Challenge Description
**Author:** Sanjay C / Palash Oswal  
**Description**  
Control the return address and arguments  
This time you'll need to control the arguments to the function you return to! Can you get the flag from this [program](/assets/downloads/picoctf/pwn/medium/buffer_overflow_2/vuln)?  
You can view source [here](/assets/downloads/picoctf/pwn/medium/buffer_overflow_2/vuln.c).  

Hint 1: Try using GDB to print out the stack once you write to it.  

### Writeup
This challenge is about the same as [Buffer Overflow 1](/writeups/picoctf/pwn/medium/bufferoverflow1), the only difference is that we need to input the right arguments for the win function.  

Firstly, let's find out what is the offset to the return.  
We can do this by overflowing the buffer and checking the memory of the return address before it segmentation faults.  
Using these 2 commands {% raw %} `cyclic 200` {% endraw %} and {% raw %} `break *vuln+29` {% endraw %}, we can use the string provided by {% raw %} `cyclic 200` {% endraw %} and input it into the function. Then the break point allows us to check the address the return function is pointing to.  

![Here lies a picture](/assets/downloads/picoctf/pwn/medium/buffer_overflow_2/ptr_addr.png)  

We can then use {% raw %} `cyclic -l 0x62616164` {% endraw %} to find out that the offset is 112.  

Now that we know the offset we can ret2win, by using {% raw %} `x/wx win` {% endraw %}, we can find the memory address of win() and return to it.  
This gives us a payload of {% raw %} `b"A" * 112 + p32(0x8049296)` {% endraw %}, this allows us to return to main, however, we are still unable to get the flag.  
This is due to the checking for arguments, as we provided no arguments, we will fail the check and simply return.  

Hence, we need to find the offset for the arguments and also the arguements themselves.  

### Arguments  
We can see that the address of our arguments are at {% raw %} `ebp+8` {% endraw %} and {% raw %} `ebp+0xc` {% endraw %} as we can see the check uses these 2 addresses at {% raw %} `dword ptr [ebp + 8], 0xcafef00d` {% endraw %} and {% raw %} `dword ptr [ebp + 0xc], 0xf00df00d` {% endraw %}.  

Using this payload, {% raw %} `b"A" * 112 + p32(0x8049296) + b"aaaabaaacaaadaaaeaaa"` {% endraw %}, we are able to find offset for both arguments relative to the return pointer.  

![Here lies a picture](/assets/downloads/picoctf/pwn/medium/buffer_overflow_2/args_offset.png)  

Hence, we can use this final payload:  
{% raw %} `payload = b"A" * 112 + p32(0x8049296) + b"B" * 4 + p32(0xCAFEF00D) + p32(0xF00DF00D)` {% endraw %}  

### Solve Scipt  
[Solve Script](/assets/downloads/picoctf/pwn/medium/buffer_overflow_2/exploit.py)  