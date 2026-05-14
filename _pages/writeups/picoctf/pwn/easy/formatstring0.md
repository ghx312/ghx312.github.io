---
layout: terminal_centered
title: Format String 0
permalink: /writeups/picoctf/pwn/easy/formatstring0
date: 2026-05-14
category: writeups
---

# Description  
**Author:** Cheng Zhang  
**Description**  
Can you use your knowledge of format strings to make the customers happy?  
Download the binary [here](/assets/downloads/picoctf/pwn/easy/formatstring0/format-string-0).  
Download the source [here](/assets/downloads/picoctf/pwn/easy/formatstring0/format-string-0.c).  

Hint 1: This is an introduction of format string vulnerabilities. Look up "format specifiers" if you have never seen them before.  
Hint 2: Just try out the different options  

### Writeup  
For this challenge there are actually 2 different solutions.  
Let's go through the first intended solution.  

#### Intended Solution  
The intended solution was for us to use a format string vulnerability as it parses the user's input into printf() without specifying a format.  
From, the code we can see that we are forced to use one of the 3 options from the given menu to answer the question, however, we also have to pass a check where they check the length of our input and only when it is longer than 64 than we get to pass the first question.  

For the first question, we are supposed to use Gr%114d_Cheese which contains %114d which formats the user input such that there is a number that has a padding length of 114, the number is due to the d part meaning decimal.  

This allows us to pass both checks as Gr%114d_Cheese is in the menu and it passes the length check.  

For the second question, the only constraint was that we needed to select an option from the given menu. However, the flag is located in a segmentation fault handler. This means that we need to segmentation fault in order to get the flag.  

Hence we need to use Cla%sic_Che%s%steak as it has the %s format. %s pops the first value of the stack and reads it as an address and goes there, as not all values on the stack are valid addresses, we will eventually segfault and trigger the flag.  

#### Unintended Solution  
This challenge can actually be solved in another way using buffer overflow and ret2win. Buffer overflow vulnerability is not dependant on the gets() function only, it simply occurs when there is a function that allows the user to write more than intended/writing more than the memory allocated for writing. In this case, this challenge uses scanf("%s", choice1) which does not limit the user input.  

Therefore, by BOFing, we can find the offset from scanf("%s", choice1) to ret and then input the address of the segmentation fault handler to print the flag.  This is also the solution that is shown by the solve script provided below.  

### Solve Script  
[Solve Script](/assets/downloads/picoctf/pwn/easy/formatstring0/exploit.py)