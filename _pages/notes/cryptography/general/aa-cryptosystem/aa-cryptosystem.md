---
layout: terminal_centered
title: Introduction to RSA
permalink: /notes/cryptography/general/aa-cryptosystem/introduction/
date: 2026-07-03
category: notes
---

# Introduction  
I recently stumbled upon a new cryptosystem called the AA $$_\beta$$ - Cryptosystem made like more than a decade ago. I decided to take a week off and learn about it, and here are all my notes and all you need to know about the cryptosystem.  

### Initialisation
Alice chooses 3 ephemeral secret keys that are integers, $$a_1$$, $$a_2$$ and $$a_3$$ which are 2$$n$$-bits long.  
The 3 ephemeral secret keys must fulfil this relation:  
-$$a_1 + a_2 \equiv 0 \pmod{a_1 - a_2}$$  
-$$a_2 + a_3 \equiv v \pmod{a_1 - a_2}$$  
where $$v$$ is 0.8125$$n$$-bits long  

Let $$p$$ and $$q$$ be two distince prime numebrs of $$n$$-bit length.  

Alice's public keys are given by:  
-$$e_{A1} = a_1 + a_2 = pq$$  
-$$e_{A2} = a_1 + a_3$$  

Alice's private keys are given by:  
-$$d_{A1} = a_1 - a_2 = p$$  
-$$d_{A2} = v$$  

Bob will generate two ephemeral sessions keys, $$k_1$$ and $$k_2$$. They are each $$\frac{n}{6}$$-bits long.  
The message that Bob will relay to Alice is a $$\frac{4n}{5}$$-bit integer, $$m$$.  

### Encryption  
Bob will produce the following ciphertext:  
-$$C = k_1e_{A1} + k_2e_{A2} + m$$  

### Decryption  
$$(C \pmod{d_{A1}}) \pmod{d_{A2}} = m$$  
Step 1: $$(C \pmod{d_{A1}}) = k_2v + m$$, as $$k_2v + m < d_{A1}$$  

Proof that $$e_{A2} \pmod{d_{A1}} \equiv v$$  
Assume that $$e_{A2} \pmod{d_{A1}} \not\equiv v$$  
1.Definition of $$e_{A2} = a_1 + a_3$$  
2.Definition of v: $$a_2 + a_3 \equiv v \pmod{a_1 - a_2}$$  
3.$$a_1 + a_3 \not\equiv v \pmod{a_1 - a_2}$$  
4.$$a_1 + a_3 + (a_1 - a_2) \not\equiv v + (a_1 - a_2) \pmod{a_1 - a_2}$$  
5.$$a_1 + a_3 \not\equiv a_2 + a_3 + a_1 - a_2 \pmod{a_1 - a_2}$$  
6.Statement 5. claims that $$a_1 + a_3 \not\equiv a_1 + a_3 \pmod{a_1 - a_2}$$, however, $$a_1 + a_3 \equiv a_1 + a_3 \pmod{a_1 - a_2}$$  
7.We have come to a contradiction, hence, $$e_{A2} \pmod{d_{A1}} \equiv v$$  

Step 2: $$(k_2v + m \pmod{d_{A2}}) = m$$, as $$m < d_{A2}$$  

### Public Information  
These are the information known to the public, or a potential Eve.  
-$$e_{A1} = a_1 + a_2 = pq$$  
-$$e_{A2} = a_1 + a_3$$  
-$$C = k_1 e_{A1} + k_2 e_{A2} + m$$

***

# Underlying Security Principles  
### Diophantine Equation Hard Problem  
The Diophantine Equation Hard Problem is to determine a sequence of intergers which are the preferred solutions to a linear Diophantine Equations in the form of $$U = \sum_{i = 1}^{n} V_ix_i$$, where all $$V_i$$ are known.  

For an unbounded $$x_i$$ there are infinitely many integer solutions, however, when working with this cryptosystem, it allows us to reduce the search space of the preferred solutions to $$x_i \in [2^{63}, 2^{64} - 1]$$. This is still a huge search space, and there is currently no known algorithm or exploit to reduce this search space.  

When trying to exploit this cryptosystem, I would not exploit this search space. I would instead try to use LLL in order to exploit the linear relationship of the unknown $$x_i$$ in the Diophantine Equations.  

There are 2 possible DEHP Problems that we can solve in order to break this cryptosystem.  

#### AAβ-DEHP-1  
Determine the preferred integer either $$k_1$$ or $$k_2$$ such that $$m = C - k_1e_{A1} \pmod{e_A2}$$ or $$m = C - k_2e_{A2} \pmod{e_{A1}}$$  

This problem is basically impossible to solve as it requires you to already know about the original message.  

#### AAβ-DEHP-2  
Determine the preferred integers, $$a_1$$, $$a_2$$ and $$a_3$$ belonging to the public keys $$e_{A1}$$ and $$e_{A2}$$  

This is possible to be solved, however, it is incredibly hard as we are only given 2 equations with 3 unknowns and also requires it to be the preferred solutions.  

### Integer Factorization Problem  
The integer factorization problem states that it is computationally hard to find the prime decomposition of any number. 

Given $$n$$ where $$n = p \times q$$, find $$p$$ and $$q$$, where $$p$$ and $$q$$ are distinct, large primes.

The best algorithm that we have for this problem is the GNFS which runs in sub-exponential time which is slower than the polynomial time that we want.  