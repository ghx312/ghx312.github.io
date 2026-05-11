---
layout: terminal_centered
title: Classic BOF
permalink: /notes/pwn/bof/classicbof
date: 2026-05-11
category: notes
---

## What is BOF?  
BOF also known as buffer overflow is when the binary accepts more data than the buffer can contain.  
For example:  
{% raw %}
`void vuln(){`  
    `buf[64]`  
    `gets(buf)`  
`}`  
{% endraw %}

The binary creates a buffer of 64 bytes, then accepts input from the user. If the users input more than 64 bytes, the buffer is unable to contain them all, and the remaining bytes will spill over into the adjacent memory addresses. This oftern causes a segmentation fault which crashes the programme, however, mastering this skill will allows you to get the binary to execute functions that aren't even called by the author.  

This example above uses {% raw %} `gets()` {% endraw %} which is a dangerous function as it will keep writing information given by the author until it hits a newline. This makes it one of the most obvious signs of a BOF vulnerability.  

## ret2win
ret2win, also known as return to win, is a byproduct of the buffer overflow vulnerability. Usually when a function is called, the function is ran and returned to the original function. However, if a BOF vulnerability occurs within the called functions, we can override the return pointer and get it to run a seperate function. Usually this function would be the win() function where the flag would print. However, for real life scenarios it could be pointing towards a function within a class tha changes the adminstrative rights for a session.  
Example:  
{% raw %}
`void win(){`  
    `printf(flag);`  
`}`  

`void vuln(){`  
    `buf[64]`  
    `gets(buf)`  
`}`  

`int main(){`  
    `vuln();`  
`}`  
{% endraw %}

In this case, when we run the programme, the programme will first call main() which calls vuln(). Vuln then initialises a 64 byte buffer and gets() input from the user.  
If there user inputs more than 64 bytes and overrides the return pointer to point towards the head of the win() function, the win() function will run and print out the flag.  
This is basically what ret2win is, using BOF to control the direction of the programme.  

## Canary  
The canary is a piece of data in a memory address, the purpose of a canary is to detect a buffer overflow. The author would create a canary, receive input from the user, then check if the canary is still intact, meaning that the data at a certain memory address has not been tampered with. As buffer overflow causes the the immediate memory address after the buffer to be changed, this means that if the checking of the canary is before the return, the canary would be destroyed and the programme would exit.  

{% raw %}
`void win(){`  
    `printf(flag);`  
`}`  

`void vuln(){`  
    `canary[4] = beef;`  
    `buf[64];`  
    `gets(buf);`  
    `if canary != beef:`  
        `exit(1);`  
`}`  

`int main(){`  
    `vuln();`  
`}`  
{% endraw %}

This is an example of a canary where if the adversary simply buffer overflows, it would destroy the canary and trigger an early exit, stopping the adversary from leaking the flag.  