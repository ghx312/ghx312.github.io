---
layout: terminal_centered
title: CryptoHack - RSA
permalink: /notes/cryptography/cryptohack/rsa/
date: 2026-07-21
category: notes
---

## Introduction to RSA  
RSA, also known as Rivest–Shamir–Adleman, is an asymmetric cryptographic system that utilises the Integer Factorization Problem and the Discrete Logarithmic Problem. It is one of the most well known cryptographic system used to date. However, due to the technological advancements both in classical and quantum strategies, RSA has been slowly disregarded as a safe encryption system.  

RSA is a great cryptosystem to start with when studying the world of cryptography.  

This page covers all information covered in the CryptoHack course, however, there exist more information about RSA that is covered in my [general notes](notes/cryptography/general/rsa)

### Greatest Common Divisor  
The Greates Common Divisor of 2 numbers, is the largerst integer that divides both numbers. I can also be said to be the greatest shared factor between them. 

There are multiple methods to finding the GCD of 2 numbers, however, the one that I will be covering here today is Eucild's Algorithm.  

#### Eucild's Algorithm  
Eucild's Algorithm starts by taking the larger of the 2 number, let's denote that as $$x_1$$, and expressing it as a linear relationship in terms of the smaller number, $$x_2$$. 

We can express $$x_1 = kx_2 + c_1$$, where $$k \in \mathbb{Z}^+$$ and $$0 \leq c_1 < x_2$$. We then repeat this process for $$x_2$$ and $$c_1$$, where we express $$x_2 = kc_1 + c_2$$, where $$k \in \mathbb{Z}^+$$ and $$0 \leq c_2 < c_1$$.  

So the full algorithm would be something like this:  

$$x_1 = kx_2 + c_1$$  

$$x_2 = kc_1 + c_2$$  

$$\dots$$  

$$c_{i - 2} = kc_{i - 1} + c_{i}$$  

The algorithm stops when $$c_i = 0$$, the previous non-zero remainder is the greatest common divisor of the numbers $$x_1$$ and $$x_2$$.  

Here is an example of using Euclid's Algorithm to find the gratest common divisor of 13 and 5.  

$$13 = 2(5) + 3$$  

$$5 = 1(3) + 2$$  

$$3 = 1(2) + 1$$  

$$2 = 2(1) + 0$$  

$$\text{GCD}(13, 5) = 1$$  

### Extended GCD  
The Extended GCD covers the Extended Euclid's Algorithm.  

#### Extended Euclid's Algorithm  
The Extended Euclid's Algorithm is an algorithm to find the integers $$a, b$$ such that $$ax_1 + bx_2 = \text{GCD}(x_1, x_2)$$.  

We can do this by reversing the original Euclid's Algorithm, isolating GCD and expressing the remainding terms as a linear equations of its previous terms. Here is an example with the numbers, 13 and 5.  

$$1 = 3 - 1(2)$$  

$$1 = 2(3) - 5$$  

$$1 = 2(13) - 4(5)$$  

We have found our $$a$$ and $$b$$ being, 2 and -4.  

### Modular Arithmetic 1  
Modular Arithmetic is a topic under Discrete Math that is commonly used in cryptography.  
Modular Arithmetic can be described as in taking the remainder of a number after being divided by another. For example:  

$$13 \equiv 3 \pmod{10}$$  

Where 3 is the remainder of 13 after dividing by 10, when 2 numbers have the same remainder after being divided by $$x$$, we can say that the 2 numbers are congruent (or the $$\equiv$$ sign) mod x.  

So we can also have $$23 \equiv 13 \pmod{10}$$ as they both have a remainder of 3 after being divided by 10.  

When a number's remainder is 0 after being divided by 10, this means that it is divisble by 10, we can use this vertical bar to denote divisbility, where $$10 \vert 20$$ which means that 10 divides 20, this can also be expressed as $$20 \equiv 0 \pmod{10}$$.  

#### Code  
In Python, the modulo sign is denoted by the precent sign %, where a % b means to take the remainder of a after being divided by b.  

{% raw %}`remainder = 13 % 5`{% endraw %}

### Modular Arithmetic 2  
Modular Arithmetic 2 covers the topic of Fields $$\mathbb{F}_p$$ and identity elements for the addition and multiplication operator.  

#### Groups  
Groups are a set of elements that fulfil a set of mathematical rules. In modular arithmetic, we will be working closely with groups (More specifically fields). Let us denote the group of elements that we are working with as, $$G = \{a_1, a_2, \dots, a_n\}$$, let us also denote the binary operator that we will be using as $$*$$.  

Closure: Closure is the rule that any 2 elements in a group, $$\forall a, b \in G$$, using the given binary operator must result in another element in the group, $$a * b \in G$$.  

Associativity: Associativity is the rule that it does not matter which order you apply the operator.  
Formally: $$a * (b * c) = (a * b) * c$$  

Identity Elements: Inverses elements are elements in which when acted upon the original element using the given binary operator returns the identity element.  

For example, in addition the inverse element is the negative of the original element, as $$x - x = e = 0$$. In multiplication, the inverse element is the reciprocal of the original element, as $$x \times \frac{1}{x} = e = 1$$ 

#### Abelian Groups  
Abelian Groups are also groups, however, they also fulfil one more rule of commutativity.  

Communtativity: Commutativity is the rule that the order of the elements does not matter when applying the operator.
Formally: $$a * b = b * a$$  

Groups that have this rule are also known as Abelian groups. All abelian groups are groups but not all groups are abelian groups (An example of a non-abelian group would be matrix multiplication)  

#### Field  
Fields are made 2 abelian groups, with the first abelian group using the + binary operator and the second using $$\times$$ binary operator. Let us denote a field of elements as $$\mathbb{F}_p = \{0, 1, 2, \dots, p - 1\}$$, where $$p$$ is prime.  

Under the addition operator, the entire set of element is a valid abelian group  

Under the multiplication operator, the entire set of elements (Except for 0) is a valid abelian group  

The distributive law states that $$a \times (b + c) = (a \times b) + (a \times c)$$  

Modular Arithmetic is actually a field by itself (Provided that the modulo is prime)  

#### Fermat's Little Theorem  
Fermat's Little Theorem states that:  

$$a^{p - 1} \equiv 1 \pmod{p}$$  

Where $$p$$ is a prime number and $$0 < a < p$$  

### Modular Inverting  
Modular Inverting requires us to derive the other general forms of Fermat's Little Theorem. Here are are the different derivations:  

$$a^p \equiv a \pmod{p}$$  

$$a^{p - 2} \equiv a^{-1} \pmod{p}$$  

We can use the second formula to find the multiplicative inverse of $$a$$ modulo $$p$$.  

### Quadratic Residues  
Quadratic Residues are elements in $$\mathbb{F}_p^*$$ such that there are 2 solutions in $$\mathbb{F}_p^*$$ when $$a^2 \equiv x \pmod{p}$$ where x is the element. If $$x$$ has 2 solutions in $$\mathbb{F}_p^*$$, it is known as a Quadratic Residue and its corresponding solutions are given by $$a$$ and $$-a$$. However, if $$x$$ does not have 2 solutions, it is known as a Quadratic Non-Residue.  

In order to find if there exist a quadratic residue for an element in $$\mathbb{F}_p$$, if $$p$$ is small, we can iterate through the whole group to check if a valid solution exists. However, this method is incredibly slow for larger numbers.  

### Legendre Symbol  
The Legendre Symbol is given by $$(a/p) \equiv a^{\frac{p - 1}{2}} \pmod{p}$$:  

$$(a/p) = 1$$ if a is a quadratic residue and $$a \not\equiv 0 \pmod{p}$$  
$$(a/p) = -1$$ if a is a quadratic non-residue $$\pmod{p}$$  
$$(a/p) = 0$$ if $$a \equiv 0 \pmod{p}$$  

Quadratic Residue * Quadratic Residue = Quadratic Residue  
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue  
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue  

This allows us to quickly determine if a number is a quadratic residue, however, it does not help us in determining the solutions for a possible quadratic residue.  

Using the hint that $$p \equiv 3 \pmod{4}$$, we can find a method to quickly derive the solutions to the quadratic residue.  

As we know that all possible quadratic residues fulfil this equation:  

$$a^{\frac{p - 1}{2}} \equiv 1 \pmod{p}$$

We can then multiply $$a$$ to both sides giving us this equation.  

$$a^\frac{p - 1}{2} \times a \equiv a^{\frac{p + 1}{2}} \pmod{p}$$  

We can then simply take the square root of this to give us the quadratic roots of a.  

$$\sqrt{a^\frac{p  + 1}{2}} \equiv a^\frac{p + 1}{4} \equiv  \sqrt{a} \pmod{p}$$  

We can use this resultant equation to easily find the quadratic roots of a quadratic residue mod p  
However, it is important to take note that this method will only work if the prime, $$p \equiv 3 \pmod{4}$$  

### Modular Square Root  
However, what is the modulus isn't a prime that fulfils the condition that allows us to use the strategy above, where $$p \not\equiv 3 \pmod{4}$$  
Hence, we have to use the Tonelli-Shanks Algoritm.  

#### Tonelli-Shanks Algorithm  
This algorithm work iff $$a$$ is a quadratic residue, which can be checked using the Legrendre Symbol.  

Let us express $$p - 1 = q \times 2^s$$, we also find $$z$$ such that $$(z/p) = -1$$  

We then initialise the following varaibles:  

$$c = z^q \pmod{p}$$  

$$r = a^\frac{p + 1}{2} \pmod{p}$$  

$$t = a^q \pmod{p}$$  

$$m = s$$  

Using these variables, we iterate through the following loop, where we stop when $$t = 1$$ and smallest integer $$i, (0 < i < m)$$ such that $$t^{2^i} = 1$$  

$$b = c^{2m + i - 1} \pmod{p}$$  

$$r = r \times b \pmod{p}$$  

$$t = t \times b^2 \pmod{p}$$  

$$c = b^2 \pmod{p}$$  

$$m = i$$  

When the loop ends, $$r$$ will be the square root of $$a \pmod{p}$$  

If $$s = 1$$, the algorithm simply condenses to:  

$$r = a^\frac{p - 1}{4}$$  

### Chinese Remainder Theorem  
The Chinese Remainder Theorem allows us to combine linear systems of equation with different modulus, but with the same remainder.  

Given a set of linear modular equations such that:  

$$x \equiv y_1 \pmod{n_1}$$  

$$x \equiv y_2 \pmod{n_2}$$  

$$x \equiv y_3 \pmod{n_3}$$  

$$\dots$$  

$$x \equiv y_i \pmod{n_i}$$

Given that all modulus are coprime or $$\text{GCD}(n_1, n_2, n_3, \dots, n_i) = 1$$  

$$N = \prod_{k = 1}^{i} n_k$$  

Set $$N_i = \frac{N}{n_i}$$, let $$d_i$$ be the multiplicative inverse of $$N_i \pmod{n_i}$$  

We will be able to combine the equation into its final form, being:  

$$x \equiv \sum_{k = 1}^{i} y_k \times N_k \times d_k \pmod{N}$$  