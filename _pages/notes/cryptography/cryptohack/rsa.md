---
layout: terminal_centered
title: CryptoHack - RSA
permalink: /notes/cryptography/cryptohack/rsa/
date: 2026-04-07
category: notes
---

# Introduction  
There are all the notes for RSA, I hope it will be helpful. Use the side bar to navigate through the different topics. ;)  

## Prerequisites  
There are some prequisite topics that are required for an understanding of RSA.  
- Modular Arithmetic  
- Greatest Common Divisior  
- Euclid's Algorithm + Extended Euclid's Algorithm  
- Fermat's Little Theorem  

There are some other topics that are required to understand the different attacks for RSA but these are the bare minimum for now.  

### Modular Arithmetic  
Modular Arithmetic is taken the remainder of a number after dividing by the modulo.  
E.g. $$7 \pmod{3} \equiv 1$$  
Where $$7 \div 3 = 2R1$$  

Notation:  
We use the $$\equiv$$ to say that 2 numbers are the same under a certain modulo.  
We also indicate the modulo used using $$\pmod{p}$$, where p is our modulo.  

Characteristics of Modular Arithmetic:  
$$a + x \equiv b + x \pmod{p}$$  
$$a - x \equiv b - x \pmod{p}$$  
$$a \times x \equiv b \times x \pmod{p}$$  
$$a + b \pmod{p} \equiv (a \pmod{p} + b \pmod{p}) \pmod{p}$$  
$$ a \times x \equiv b \times x \rightarrow a \equiv b \pmod{\frac{p}{gcd(p, x)}}$$  
$$ a \times x \equiv b \times x \rightarrow a \equiv b \pmod{p}, gcd(p, x) = 1$$  

### Greatest Common Divisor  
GCD is the greatest common divisor denoted by GCD(a, b) = x where x is the remainder.  
E.g. GCD(15, 25) = 5 as 5 is the greatest common divisor.  
We can find the greatest common divisor of any 2 numbers using Euclid's Algorithm.  
If GCD(a, b) = 1, it means that they are coprime where they do not share any common factors.  

### Euclid's Algorithm  
Euclid's Algorithm is used for finding the greatest common divisor.  
GCD(a, b):  
$$a = k_1b + c_1$$  
$$b = k_2c_1 + c_2$$  
$$\dots$$  
$$c_n = k_{n + 1}c_{n + 1} + 0$$  
Where the previous remainder is the greatest common divisor of a and b.  