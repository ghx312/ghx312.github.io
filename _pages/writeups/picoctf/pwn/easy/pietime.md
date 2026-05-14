---
layout: terminal_centered
title: PIE TIME
permalink: /writeups/picoctf/pwn/easy/pietime
date: 2026-05-14
category: writeups
---

# Description  
**Author:** Darkraicg492  
**Description**  
Can you try to get the flag? Beware we have PIE!  
The program's source code can be downloaded [here](/assets/downloads/picoctf/pwn/easy/pietime/vuln.c). The binary can be downloaded [here](/assets/downloads/picoctf/pwn/easy/pietime/vuln).  

Hint 1: Can you figure out what changed between the address you found locally and in the server output?  

### Writeup  
PIE, also known as position independant executables, is a type of protection that can be activated in the binary.  PIE randomises the binary's base address, this means that the relative distance between functions remain the same.  

This means that we can use the programme given to us locally, calculate the offset of the gets() to the rip, and apply that offset to the leak address that is provided to us in the nc version.  

Locally:  
main() addr: 0x555555555189  
win() addr: 0x5555555551f4  

Static offset = 0x5555555551f4 - 0x555555555189 = 0x6b  

Netcat:  
main() addr: 0x7f3d2a119189  
win() addr = 0x7f3d2a119189 + 0x6b = 0x7f3d2a1191f4  

Then we can simply execute a simple ret2win using buffer overflow.  

### Solve Script  
[Solve Script](/assets/downloads/picoctf/pwn/easy/pietime/exploit.py)