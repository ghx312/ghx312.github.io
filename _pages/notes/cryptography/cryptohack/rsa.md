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
- Multiplicative Inverses
- Euler's Totient Function  
- Euler's Totient Theorem  

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

Example:  
$$13 = 2(5) + 3$$  
$$5 = 1(3) + 2$$  
$$3 = 1(2) + 1$$  
$$2 = 2(1) + 0$$  
GCD(13, 5) = 1  

### Extended Euclid Algorithm  
$$\exists u, v \rightarrow a \times u + b \times v = GCD(a, b)$$  
We can find u and v by reversing Euclid's original algorithm.  
Here is an example using the previous example from Euclid's Algorithm.  

Example:  
$$1 = 3 - 1(2)$$  
$$1 = 2(3) - 5$$  
$$1 = 2(13) - 4(5)$$  
$$13 \times 2 + 5 \times -4 = 1$$  
$$u = 2, v = -4$$  

### Fermat's Little Theorem  
If p is prime, $$a < p$$  
Fermat Theorem states that:  
$$a^p \equiv a \pmod{p}$$  
$$a^{p - 1} \equiv 1 \pmod{p}$$  
$$a^{p - 2} \equiv a^{-1} \pmod{p}$$  

### Multiplicative Inverses  
A finite field $$F_p$$ contains all possible elements modulo p.  
$$F_p = \{0, 1, 2, 3, 4, 5,..., p - 1\}$$
Where $$F_p$$ contains all elements from 0 to p - 1 which are all the possible numbers modulo p.  
$$\forall g \in F_p, \exists d \in F_p | g \times p \equiv 1 \pmod{p}$$  

### Euler's Totient Function  
Euler's Totient Function is denoted as $$\phi()$$  
Where $$\phi(N) = \text{Number of x in F_p | GCD(N, x) = 1}$$  
For example:  
$$\phi(8) = 4$$ as only the numbers 1, 3, 5, 7 are coprime to 8.  
$$\phi(p) = (p - 1)$$ if p is prime.  

Euler's Totient Function is multiplicative, this means that $$\phi(p) \times \phi(q) = \phi(p \times q)$$ if both p and q are prime and $$p \neq q$$  
Therefore, $$\phi(pq) = (p - 1)(q - 1)$$  

### Euler's Totient Theorem  
Euler's Totient Theorem states that:
$$a^{\phi(p)} \equiv 1 \pmod{p}$$, where a and p are coprime.  

## How does RSA work?  
We will go through this in a few parts:  
- Initialisation  
- Encryption  
- Decryption  
- Why does it work?  

### Initialisation  
Let's say we have 2 people Alice and Bob who would like talk to each other, however, Eve is in their way and also want to read the conversation.  

In order to prevent this, Alice is going to use the RSA encryption system.  
Alice first starts by choosing 2 prime numbers, p and q. She then computes $$p \times q = N$$  
These 2 primes numbers are kept hidden as they are required for decryption.  
Alice then chooses a public exponent, $$e$$, which is usally 65537.  
Alice then sends N and e to Bob.  
Eve intercepts the information and tracks it down.  

So now these are the information that Alice, Bob and Eve have:  
Alice: p, q, N, e  
Bob: N, e  
Eve: N, e  

### Encryption  
Bob now has a message he would like to send to Alice, we denote this as m.  
Bob encrypts his message by calculating the ciphertext through this.  
$$m^{e} \equiv c \pmod{N}$$, where m is his message and c is the ciphertext.  

Bob then sends his ciphertext to Alice, however, Eve is able to intercept it and read it.  

So now these are the information that Alice, Bob and Eve have:  
Alice: p, q, N, e, c  
Bob: N, e, m, c  
Eve: N, e, c  

c looks like gibberish to Alice and Eve, however, as Alice has p and q, she is able to reverse the encryption and decrypt it.  

### Decryption  
Alice first calculates totient N using this formula.  
$$\phi(N) = (p - 1)(q - 1)$$  
She is then able to calcuate d by using Euler's Totient Theorem and Euclid's Algorithm.  
$$e \times d \equiv 1 \pmod{\phi(N)}$$  
She then decrypts the ciphertext by calculating:  
$$c^{d} = m \pmod{N}$$  

As Eve does not possess knowledge about the 2 hidden primes, p and q. She is unable to decrypt the ciphertext.  

### Why does it work?  
It works as Eve does not posses knowledge about the 2 hidden primes.  
However, some may argue that Eve could recover the primes by factoring N.  
Hence to combat this, we must use big prime numbers, a safe limit is 2048-bit primes.  

# Vulnerabilities    
I will classify these vulnerabilities under 2 categories, implementation vulnerabilities and normal vulnerabilities.  

Implementation Vulnerabilities are vulnerabilities that occurs due to implementation error by the creator.  

Normal Vulnerabilities are vulnerabilities that are innate to RSA itself.  

## Implementation Vulnerabilities  
Let's start with something relatively simple, when N is prime.  
