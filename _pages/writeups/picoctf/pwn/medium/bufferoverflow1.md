---
layout: terminal_centered
title: Buffer Overflow 1
permalink: /writeups/picoctf/pwn/medium/bufferoverflow1
date: 2026-05-09
category: writeups
---

# Challenge Description  
**Author:** Sanjay C / Palash Oswal  
**Description** 
Control the return address. Now we're cooking! You can overflow the buffer and return to the flag function in the [program](/assets/downloads/picoctf/pwn/medium/buffer_overflow_1/vuln.c).  
You can view source [here](/assets/downloads/picoctf/pwn/medium/buffer_overflow_1/vuln).  

Hint 1: Make sure you consider big Endian vs small Endian.  
Hint 2: Changing the address of the return pointer can call different functions.  

### Writeup  
This is a simple buffer overflow, where after overflowing we ret2win (Return 2 Win -> Where we call the function that gives us the flag)  
After reading the program code, we can see that we enter main(), which calls vuln() and we want to buffer overflow such that we call win().  
We will first open up the programme in pwndbg.  

Firstly, let's find the address of win(). We can do this by using this command {% raw %} `x/gx win` {% endraw %}  
This give us the result {% raw %} `0x80491f6 <win>: 0x53e58955fb1e0ff3` {% endraw %}, telling us that the addr of win() is 0x804916.  

Secondly, we need to also find the distance of the return pointer to gets() function so that we can calculate exactly how many bytes we must buffer before inputting win()'s address.  
We can do this in 2 ways:

#### First Method  
The first method works by getting the function to completely overflow and telling you what the return pointer is pointing to.  
We can do this by using this command {% raw %} `cyclic 200` {% endraw %}, this prints out a string of length 200.  
We then simply input this into the function and let it segmentation fault.  
![Here lies a picture](/assets/downloads/picoctf/pwn/medium/buffer_overflow_1/seg_fault.png)  

We can then use this command {% raw %} `cyclic -l 0x6161616c` {% endraw %} to find the number of bytes we need to buffer.  
![Here lies a picture](/assets/downloads/picoctf/pwn/medium/buffer_overflow_1/offset.png)  

This tells us that we need to buffer 44 bytes.  

#### Second Method  
The second method does not require the challenge to output the return address to tell you how many bytes you need to buffer.  
Instead, we can do the same method as the first one, however, we set up a second breakpoint right after we enter our cyclic 200.  
We can then use these commands to check for the current return address, {% raw %} `x/wx $ebp+4` {% endraw %} which is the return address for 32-bit systems.  
![Here lies a picture](/assets/downloads/picoctf/pwn/medium/buffer_overflow_1/offset2.png)  

This also tells us that we need to buffer 44 bytes.  

### Payload  
The payload is very simple, using the information we gained from above, our payload is simply, 44 bytes of buffer and then the address of win().  

### Solve Script  
[Solve Script](/assets/downloads/picoctf/pwn/medium/buffer_overflow_1/exploit.py)  