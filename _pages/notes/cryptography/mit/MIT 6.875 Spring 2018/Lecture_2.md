---
layout: terminal_centered
title: Lecture 2
permalink: /notes/cryptography/mit/spring_2018/lecture_2/
date: 2026-04-05
category: notes
---

## Lecture 2

### **Shannon’s Key Length Theorem:**  
Shannon’s Key Length Theorem states that the length of the key must be longer than or equal to the length of the message in order for an algorithm to achieve Perfect Secrecy, and that there are more or equal number of keys than messages.  
$$|k| \geq |m|$$, $$|K| \geq |M|$$  

#### **Proof**  
Assume $$|M| \geq |K|$$  
Let c be such that $$P(C = c) > 0$$  
Let $$M_c = \{m$$ such that $$\exists k$$ for which $$m = D(k,c)\}$$ (Set of m that can be decrypted)  
Then $$|K| > |M_c|$$ (Since there is at least 1 key for each message) and $$|M| \geq |K|$$ (Assumption for proof)  
So, there exists some $$m^{'} \in M$$ for which there is no k, such that $$D(k^{'}, c) = m^{'}$$  
Hence, $$P(C = c|M = m^{,}) = 0$$, since $$P(C = c) > 0$$ hence, $$P(C = c|M = m) > 0$$  
Since, $$P(C = c|M = m^{'}) = 0 \neq P(C = c|M = m)$$, this violates the Perfect Indistinguishability, which in turn violates Perfect Secrecy, hence, $$|K| \geq |M|$$  
(Proof by Contradiction)

***

### **Pros and Cons of the One-Time Pad**
Pros:  
According to Shannon’s Theorem, it is the best possible encryption algorithm

Cons:  
The size of the key is huge, as it is the same as the message bits (XOR)  
The receiver needs to know which key goes with which ciphertext   
(Perfect Indistinguishability)  

### **Probabilistic Polynomial Time (PPT):**  
A PPT is the assumed algorithm that the adversary uses to “crack” the encryption system  
It runs in $$O(c \cdot n^k)$$, where n is the input size of the message in bits and c, k are just constants.  
This algorithm assumes that the adversary runs an algorithm that is random and in polynomial time of the length of the message. We want this to be smaller than some function to prove that an encryption system is secure.  
Perfect secrecy is not a reasonable standard to achieve; hence, Perfect Indistinguishability is also not realistic to achieve. Therefore, we need to revise our definition of a secure encryption system.

### **Revised Encryption Definition**  
G($$1^k$$) - Randomised algorithm that produces the SK (Secret key) of k length ($$k = l$$)  
E(SK, m) = c - Algorithm that encrypts the m (Plaintext)  
D(SK, c) = m, - Algorithm that decrypts the c (Ciphertext)  
Correctness: When the ciphertext is run through the Decryption function with the SK, you will obtain the original message.  
Computational Security: With respect to the PPT of Adversary EVE (New)  

So, now instead of standardising Perfect Security, we only have to be secure to some $$\frac{1}{poly(n)}$$  

### **Convention**
We say that a function $$p(k)$$ is negligible if for every polynomial P, there exists a $$k_0$$
such that $$\forall k > k_0$$, $$\varepsilon(k) < \frac{1}{p(k)}$$

In simple terms, k is the security parameter, P is all possible polynomials, $$\varepsilon(k)$$ is the vulnerability function; as long as there is a $$k_0$$ for all possible polynomials that $$\varepsilon(k) < \frac{1}{p(k)}$$, the system is secure. $$k_0$$ is like a point where all of $$k > k_0$$, all of k is secure.
This shows that the security increases exponentially relative to the vulnerability making it negligible.
The opposite is true, where if there is one P where there are no $$k_0$$ (Point of change), k is no longer secure as now there is a $$\varepsilon(k) > \frac{1}{p(k)}$$. The vulnerability is now exponentially larger than the security.
Any $$k < k_0$$, is not secure as it is not exponentially larger than the vulnerability function.

***

#### **Computational Indistinguishability (IND)**  
Encryption system (G.E.D) satisfies computational indistinguishability if:  
$$\forall$$ polynomial time sampleable message space M (Its just M)  
$$\forall$$ PPT algorithm EVE  
$$\forall$$ Non-negligible functions $$k_0$$ such that all $$k > k_0$$  
$$P[EVE(m_1, m_2, c) = b] < \frac{1}{2} + \varepsilon(k)$$  

In simple terms, if you pick $$m_1, m_2, E(SK, m_1) = c_1$$ and $$E(SK, m_2) = c_2$$, you will not be able to tell if $$c_1 = E(SK, m_1)$$ or $$c_1 = E(SK, m_2)$$  
The probability that you, as a bystander, guess m from c correctly using EVE (Which is the PPT algorithm), is less than $$\frac{1}{2} + \varepsilon(k)$$ as there are 2 options, $$m_1, m_2$$, hence 50/50 for each option through blind guessing, plus the vulnerability exploited using $$\varepsilon(k)$$  
It's the same thing as before, just that k is large enough that the convention has been reached.  

The reason that the probability of EVE not being able to find what the original m is, despite knowing G.E.D and the ciphertext, is that the $$\varepsilon(k)$$ runs in a limited time, so unless time is infinite, EVE will never be able to guarantee finding the original m.  

#### **Perfect Indistinguishability vs Computational Indistinguishability**
Perfect indistinguishability cannot be cracked even with infinite time, while computational indistinguishability is crackable with infinite time; however, due to the time constraints and power of the adversary, they do not possess the time to crack this.  

#### **Computational Indistinguishability (Many messages)**  
Encryption system (G.E.D) satisfies computational indistinguishability if:  
$$\forall$$ polynomial time sampleable message space M (It's just M)  
$$\forall$$ PPT algorithm EVE  
$$\forall$$ Non-negligible functions $\varepsilon$, $\exists k_0$ such that all $$k > k_0$$  
$$P[EVE(m_0, m_1, c) = b)] < \frac{1}{2} + \varepsilon(k)$$  
But this time $$m_0 = \{m_{0}^{1}, m_{0}^{2}, \dots ,m_{0}^{P(k)}\}$$, and $$m_1 = \{m_{1}^{1}, m_{1}^{2}, \dots ,m_{1}^{P(k)}\}$$ where $$c_1 = E(SK, m_1^b)$$  
$$c = \{c_1, c_2,\dots,c_{P(k)}\}$$  
It is the same logic, however, this time it is repeated over many messages, since all ciphertexts are different and messages, there is only 1 key that relates each message to each ciphertext, making it impossible to know which ciphertext is to which pair of messages, let alone knowing the message by itself.

### **Randomised Encryption**  
$$C_1 = E(s, m, r)$$
r represents a random state where it chooses a random ciphertext from the list of all possible ciphertexts. When the same plaintext is run with the same key, there must be an exponential list of ciphertexts that are not equal to each other, r then use the state that the chosen data was in to select a corresponding ciphertext. r must be from a data set with high entropy to prevent cryptoanalysis vulnerabilities.  

### **Semantic Security (SS)**  
$$\forall$$ PPT EVE, $$\exists$$ PPT EVE$$^{'}$$  
$$\forall$$ Polynomial time sampleable distribution M  
$$\forall$$ functions f:M => {0,1}  
$$\forall$$ non-negligible functions: $$\varepsilon > 0, \exists k_0$$ such that $$k > k_0$$  
$$|P_M[EVE^{'}(1^k) = f(M)] - P_M[EVE(1^k, c) = f(M)|E(SK, M) = c]| < \varepsilon(k)$$  

$$f(M)$$ is the function that outputs information about the plaintext for all plaintexts, $$f()$$ is true.  
(E.g. $$f(M)$$ \= “Is the first bit 1 or 0”)  
$$P_M[EVE^{'}(1^k) = f(M)]$$ is just the probability that EVE guess the plaintext generated by f(M) knowing the security parameters only  
$$P_M[EVE(1^k, c) = f(M)|E(SK,M) = c]$$ is just the probability that EVE guess the plaintext generated by f(M) knowing the security parameters and the ciphertext which came from $$E(SK, M )=c$$

The absolute values are there is show that the difference them, knowing the function f(M) with or without the ciphertext, is negligible as it is less than the vulnerability $$\varepsilon(k)$$.

In simple terms, the adversary gains no advantage in gaining information about the plaintext with or without the ciphertext.  

#### **Computational Indistinguishability and Semantic Security**
(G.E.D) satisfies Computational Indistinguishability only if it satisfies Semantic Security  

***

#### **One-Way Functions (OWF)**  
One-Way Functions satisfy Computational Indistinguishability  
x => f(x) is trivial  
f(x) => x is a hard problem  

#### **Easy to Evaluate**  
$$\exists$$PPT Algorithm A, such that $$\forall x, A(x) = f(x)$$,

#### **Hard to Invert**  
$$\forall$$PPT Algorithm Inverter, $$\forall$$ non-negligible $$\varepsilon()$$, $$\exists k_0$$, $$\forall k > k_0$$  
$$P(\text{Inverter}(1^k$$, $$f(x)) = x^{'}|f(x^{'}) = f(x)) < \varepsilon(k)$$  

In simple terms, there will always be a PPT algorithm that can easily calculate
f(x), for any x. However, the chances that the inverse PPT algorithm works (The Decryption System by Adversary) is less than the vulnerability, making it negligible for large enough k.

### **Factoring Integers**
OWF: Given an integer N, find its prime factors  
$$p, q$$ => $$N = f(p \cdot q)$$, is an easy problem as $$p \cdot q = N$$ is easy to calculate  
$$N = p \cdot q$$ is a hard problem depending on the p, q chosen.  

Factoring Integers can be an OWF only when certain p, q are selected, mainly primes that are of equal length and $p \neq q$. The best inverse algorithm for these specific integers is sub-exponential time. (General Number Field Sieve)  

### **Weak One-Way Function (WOWF)**
Easy to Evaluate: $$\exists A$$, $$A(x) = f(x)$$  
Weakly hard to invert:  
$$\exists \varepsilon (k) \geq \frac{1}{p(k)}$$, such that $$\forall A$$, $$\exists k_0$$, $$\forall k > k_0$$ => $$P(A(1^k$$, $$f(x) \neq x^{'})|f(x)=f(x^{'})) > \varepsilon(k)$$  
In simple terms, a WOWF works the same as a OWF, however, only on a significant fraction of inputs. For the other fraction of inputs, it is no longer a OWF and getting the inverse function is trivial. There is a 1/Q number of inputs where it is computationally difficult to get the inverse.  
WOWF: $$\varepsilon(k) > \frac{1}{p(k)}$$, $$\varepsilon(k) < 1 - \frac{1}{p(k)}$$

#### **Weak OWF $$\equiv$$ Strong OWF**
Theorem: OWF exist even if only WOWF exists  
SOWF: $$\varepsilon(k) < \frac{1}{p(k)}$$  
Suppose f is a WOWF for hardcore 1/Q. Instances, then the following F is an SOWF  
Definition:  
$$F(x_1,\dots,x_N) = f(x_1)||f(x_2)||\cdots||f(x_N)$$ for $$|x_i| = k$$, $$N=2kQ(k)$$  
$$Q(k)$$ is the polynomial function that describes the difficulty of inverting with the security parameters k.  
$$\frac{1}{Q(k)}$$ is the chance of a hard-to-inverse input being chosen randomly from the set of all inputs.  
$$1 - \frac{1}{Q(k)}$$ is the chance of an easy-to-invert input being chosen randomly from the set of all inputs.  
$$2k$$ is a precalculated bound.  
This function takes N numbers of $$f(x)$$ which contain both weak and hardcore inputs, and concatenates them into $$F(x_i)$$ this forces the adversary to invert all N numbers of x.  
$$|x_i| = k$$ is just the length of each randomly selected x

If an adversary works by inverting each coordinate, f(x) individually, we get an immediate bound on the success probability:  
$$(1 - \frac{1}{Q(k)})^{kQ(k)}$$ => $$[(1 - \frac{1}{Q(k)})^{Q(k)}]^{k}$$ => $$\frac{1}{e^k}$$  
As, $$(1 - \frac{1}{Q(k)})^{Q(k)}$$, $$k \rightarrow \infty$$, $$Q(k) \rightarrow \infty$$, $$(1 - \frac{1}{Q(k)})^{Q(k)} \rightarrow \frac{1}{e}$$, $$n=Q(k)$$, $$\lim_{n \to \infty} (1 - \frac{1}{n})^n = \frac{1}{e}$$   
Hence, $$P(EVE(F(x_i)) = x_{i}^{'}|f(x_{i}^{'}) = f(x_i)) \leq \frac{1}{e^k}$$  
In simple terms, P\[Adversary Succeeding\] the maximum is $$\frac{1}{e^k}$$  
(This is not formal proof, just intuition)  

### **Formal Proof**  
A reduction F not strong => f not weak  
Assume F is not strong, which means that $$\exists \varepsilon(k) > \frac{1}{p(k)}$$, let there be $$A^{'}$$ s.t for inf. many $$k^{'}$$, $$P(A^{'}(F(x_1,\dots,x_N)) \text{inverts}) > \varepsilon(k^{'})$$  

Define A(y):  
For each position i = 1… N, Repeat for more than $$2k(\varepsilon/N)^{-1}$$ trials:  
1) Choose random $$x_1$$, $$x_{i-1}$$, $$x_{i+1}$$, $$x_N$$  
2) Compute $$z = f(x_1)|...|f(x_{i-1})||y||f(x_{i+1})|...|f(x_N)$$  
3) Run $$A^{'}(z)$$ if it fails, continue; else set $$A^{'}(z) = x_1,\dots, x_N$$, such that $$f(x_{i}^{'}) = f(x_i)$$, output $$x_{i}^{'}$$, $$f(x_{i}^{'}) = y$$  

This function basically takes i and iterates through numbers from 1 to N and makes the function $$A^{'}(z)$$ solve it, if it does not work, reset and continue through the iteration. If it works, make $$A(y)$$ the inverter function for just 1 coordinate of that whole chain of successful inputs of $$A^{'}(z)$$. This shows that $$A(y) > \frac{1}{Q(k)}$$, this makes A a more efficient algorithm than before.  

In simple terms, the function $$A(y)$$ is the inverse of $$f(x)$$, while $$A^{'}(z)$$ is the inverter of $$F(x)$$, since we assumed that $$F(x)$$ is not strong, it must have a non-negligible vulnerability, $$\varepsilon(k) > \frac{1}{p(k)}$$. Hence, we can use $$A^{'}(z)$$ to invert a list of inputs, including the fraction of hard-core inputs. Then we can derive $$A(y)$$ from $$A^{'}(z)$$, by picking values of x which are part of the hard-core inputs and putting them as y, since, the definition of WOWF does not allow us to have the inverse of computationally hard numbers (Hard-core inputs), we have proof by contradiction that $$F(x)$$ is strong or $$f(x)$$ is weak. (In this case, the conclusion is that $$F(x)$$ is strong)  

***