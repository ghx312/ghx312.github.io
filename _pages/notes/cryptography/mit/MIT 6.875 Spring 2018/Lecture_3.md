---
layout: terminal_centered
title: Lecture 3
permalink: /notes/cryptography/mit/spring_2018/lecture_3/
date: 2026-04-05
category: notes
---

### Lecture 3

#### **Definitions**  
Negligible Function: A function $$f(k)$$ is negligible if $$\forall p(k)$$, $$\exists k_0$$, $$\forall k > k_0$$, $$f(k) < \frac{1}{p(k)}$$  
OWF: $$f:\{0,1\}^*$$ => $$\{0,1\}^*$$, $$\forall PPT A$$, $$P(A(f(x) = x^{'}|f(x^{'}) = f(x)) < \frac{1}{p(k)}$$  
WOWF: $$f:\{0,1\}^*$$ => $$\{0,1\}^{*}$$, $$\forall PPT A$$, $$P(A(f(x) = x^{'}|f(x^{'}) = f(x)) < 1 - \frac{1}{Q(k)}$$  
There will never be OWFs, only candidate OWFs.

#### **Groups Properties**  
Closure: $$Z_N$$ is a set of numbers, where a certain operation is applied to 2 random numbers in the group, the output falls in the group  
Identity: The number when the operation of the group is applied to all numbers, all outputs are the same as the input (Identity element) (Multiplicative Groups \= 1\) (Additive Groups \= 0\)  
Inverses: The number in the group has an inverse that, when the group’s operation is applied to both numbers, the answer is 0\. (Inverse element)  
Associative: It does not matter how the numbers in the groups are grouped in an equation, as long as the sequence remains unchanged.  
($$A \oplus B$$)$$\oplus C = A \oplus$$($$B \oplus C$$) (Associative)  
Commutative: The Order in which the input is sequenced does not matter as long as the inputs are the same. (E.g. 1 + 2 = 2 + 1)  
$$G(Z_N, \text{Operation}), \text{where } Order(G) = |G|, \text{where } |G| = \text{Number of elements in} Z_N$$

#### **Legendre's Theorem**  
All outputs are within the group (Basically mod N)  
$$\forall a \in Z_N$$ ,$$a^{|G|} = e$$ (e \= Multiplicative inverse)  
$$\forall a \in Z_N$$, $$a \cdot {|G|} = e$$ (e \= Addition inverse)  

#### **Order(a)**  
$$Order(a)$$ = $$min\{i > 0|a^i = e\}$$ (e \= Multiplicative Inverse)  
If $$Order(a) = |G|$$, a is a generator  
Or  
Euler’s Totient Function $$\phi()$$  

#### **Generator**  
$$a \in G$$, $$\{a\} = \{a^1$$, $$a^2,\dots,a^{|G|}\}|\{a^1$$, $$a^2,\dots,a^{|G|}\} = Z_N$$ (Multiplicative Groups)  
$a \in G$, $\{a\} = \{a$, $2a$, $3a,\dots, a \cdot |G|\}|\{a$, $2a$, $3a,\dots,a \cdot {|G|}\} = Z_N$ (Additive Groups)
A generator is a number when raised to an increasing integer (For multiplicative groups) or added it itself (For additive groups), returns every element within the set.  
{Primitive Roots}={Generators} Primitive Roots exist if the modulo is, 1, 2, 4, $p^k$, $2p^k$  
$2p^k$ is for odd primes p  
A group is cyclic if it has a generator

**DLOG**  
$DLOG_g(a) = t$, $1 \leq t \leq |G|$, s.t $a = g^t$  
$DLOG_g(a) = t$, $1 \leq t \leq |G|$, s.t $a = g \cdot t$
Basically, an algorithm that solves the discrete log

Discrete Logarithm Problem (Informally)
Given G, $g = a$, $a \in G$. Find $DLOG_g(a)$
Given ($Z_p$, $+$), where p is prime, find $DLOG_g(a)$  
$g^t = a \pmod{p}$

Easy Problems:  
Can be solved in linear, quadratic, and cubic  
$a + b \pmod{n}$
$a \cdot b \pmod{n}$
$GCD(a$, $b)$
$a^{-1} \pmod{p}$ only when $GCD(a$, $p) = 1$ (Use Euclid's Extended Algorithm) 
$a \cdot x + p \cdot y = GCD(a$, $p) = 1$, find x, $x = a^{-1}$  
$a^b \pmod{n}$

**Multiplicative Modular Math**
$G = (Z_{N}^{*} = \{1 \leq z < N|GCD(z, n) = 1\}, \times)$
$|Z_{N}^{*}| = \phi(n)$, $|Z_{8}^{*}| = 4$, $|Z_{7}^{*}| = 6$
$|Z_{p}^{*}| = p - 1$, for p prime
$\phi(p \cdot q) = (p - 1)(q - 1)$ where p and q are coprime  
$|Z_{p_k}^{*}| = p^{(k - 1)}(p - 1)$, for p prime (General Formula)  
$\phi(p^k \cdot q^l) = \phi(p^k) \cdot \phi(q^l) = p^{(k-1)}(p-1) \cdot q^{(l-1)}(q-1)$ where p and q are coprime

Cyclic:  
$Z_p^{*}$, $Order(a)|(p - 1)$, $a^d = 1 \pmod{p}$  
Let's say there is a set for all exponents d where $a^d = 1 \pmod{p}$
If there is 1 value, a in the set, there are many values in the set where the set is
$d_1 = \{1$, $a$, $a^2$, $a^3,\dots,a^{d-1}\}$

Discrete Logarithm Problem (Formally)
$G(Z_p^{*}$, $\times)$
A prime, p  
A generator, $g \in G$  
An element, $h \in G$
Find $x$ s.t
$g^x \equiv h \pmod{p}$

**Prime Number Theorem**
$n = \{1$, $2,\dots,n\}$
$\frac{\#Number\_of\_n\_bit\_primes}{\#Number\_of\_n\_bit\_numbers} \approx \frac{1}{nln(2)}$

Primality Testing \[Agrawal-Kayal-Saxena (AKS) Algorithm\]
Best for testing primes

How to test if a number is a generator
$\phi(n) = p - 1 = \prod q_1^{k_n}$
$g^{\frac{\phi(n)}{q_i}} \pmod{n}$
In simple terms, separate the totient of p into its prime factors, then check using the algorithm below, if none of the answer are 1, g is a generator

**Strong Primes**
$p = \vartheta q + 1$, where q is prime, $\vartheta$ is an integer
or  
$p - 1 = \vartheta q$
In simple terms, this ensures that $p - 1$ is not a number that only consists of small factors, making it easy to find the $\phi(p)$. This helps to keep p is a safe prime, not vulnerable to totient formula attacks

**Discrete Algorithm Problems**
$F = \{F_{n^{'}}$ $D_{n^{'}}\}_{n \in N}$
$F_n = \{f:D_n$->$R_n\}$ (A function that gives the corresponding output from the input)

The goal
→ Sample a $f_y \in F_N$ in $poly(n)$ time (Finding an OWF)  
→ Sample an element in $D_n$ in $poly(n)$ time (Finding an element)  
→ $f_y$ in $poly(n)$ (Computing the function)  
$EXP_{p,g}(x) = g^x \pmod{p}$, where p is an n-bit prime, g is a generator of Zp\*  
$D_n = \{0,1,2,\dots,p-2\}$ (Domain of D, or valid inputs of D)  
$Z_{p}^{*} = R_n$ (Outputs of all valid inputs)
$len(D_n) = len(R_n)$ (There is a unique output for every valid input)

In simple terms, there are a family of problems known as $F_n$, where there are $D_n$ inputs and $R_n$ outputs, and an example of one of the members of this family is $DLOG()$

Solving for x:
$a = g^x = g^{x_1 \cdot m + x_2}$, $m \approx \sqrt{p}$
$a \cdot g^{-x_2} = (g^{m})^{x_1}$

Algorithm to find $\sqrt{p}$ in polynomial time/Solve DLP:  
Compute all values of $g^{-x_2}$ for $x_2 \in \{0,1,2,3,4,5,\dots,m-1\}$
Make a table for all values of $x_2$
$\{a \cdot g^{-x_2}\} = \{\forall x_2\}$ (Length is p)
$\{(g^m)^{x_1}\} = \{\forall x_1\}$ (Length is p)
Sort the tables and go through each of them until
$a \cdot g^{-x_2} = (g^m)^{x_1}$
$x = x_1 + x_2$
Time taken: $\sqrt{p}$  
Also known as the Meet-in-the-Middle Approach or [Baby-Step Giant-Step](https://colab.research.google.com/drive/1bGRV8OVXUC0II34-JJmrioFjNp7eEorl?usp=sharing)

**Index Calculus Method**:
Time take: $2^{O(\sqrt{(log(N)log(log(N))})}$ (Sub-Exponential Time)
Guided Example:
`5^x = 8 (mod 37)`

Step 1: Choose Factor Base
Choose a set of small primes 
`B = {2, 3, 5}`

Step 2: Correct relations
Randomly pick $k$ for $g^k \pmod{p}$ such that every prime factors of the result is in B or the result is B-Smooth. There can be more than 1 results, however, all of their prime factors must remain within B.

$g^k = p^{e_1}_{1}p^{e_2}_{2}\dots \pmod{p}$ 

By taking $log_g()$ on both sides, we also switch the modulo to p - 1 to take into account for Fermat's Little Theorem as $g^{p - 1} \equiv 1 \pmod{p}$ 

$k = e_1log_g(p_1) + e_2log_g(p_2) \dots \pmod{p - 1}$

5^1 = 5 mod 37 => 1 = log$_5$(5) mod 36
5^3 = 20 mod 37 => 3 = 2log$_5$(2) + log$_5$(5) mod 36
5^11 = 2 mod 37 => 11 = log$_5$(2) mod 36
5^22 = 3 mod 37 => 22 = log$_5$(3) mod 36

Step 3: Solving Linear Systems
After we obtain the system of equations, we can solve the linear equations

$\begin{bmatrix} 2 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{bmatrix} \begin{bmatrix} log_{5}2 \\ log_{5}3 \\ log_{5}5\end{bmatrix} = \begin{bmatrix} 3 \\ 11 \\ 12 \\ 1\end{bmatrix} \pmod{36}$

Factor Base Logs:
$log_{5}2 \equiv 11 \pmod{36}$
$log_{5}3 \equiv 22 \pmod{36}$
$log_{5}5 \equiv 1 \pmod{36}$

Step 4: Target Decompositions
Try random $m$ until $5^m \cdot 8 \pmod{37}$ is B-Smooth

Let $m = 0$
$5^0 \cdot 8 = 2^3 \pmod{37}$ 
$0 + x = 3log_{5}2 \pmod{36}$
$x \equiv 3 \times 11 \pmod{36}$
***
