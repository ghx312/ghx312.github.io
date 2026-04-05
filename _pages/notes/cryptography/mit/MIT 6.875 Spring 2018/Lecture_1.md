---
layout: terminal_centered
title: Lecture 1
permalink: /notes/cryptography/mit/spring_2018/lecture_1/
date: 2026-04-04
category: notes
---

### Lecture 1

#### **Adversary: (Unbounded Computationally, Eavesdropper)**  
The adversary is the identity of the person who is trying to figure out your message.  

It is essential to identify your adversary so that you can determine the computational power and time they have to break your encryption algorithm. (Usually, the assumption that your adversary has unbounded power, meaning that they have unlimited computational power and space)  

There are 2 types of adversaries:  
Adversary EVE, where the adversary can only listen in on all the information  
EVE(), is a function that gives an output based off the PPT, c and m’s given  
Adversary Active (Mallory), where the adversary can forge or alter messages

##### **What does the adversary know?**  
Kerrcoff’s Law: The adversary knows G.E.D (Has full knowledge of the algorithm)  
Ciphertext only: The adversary can only know c, which is passed through insecure channels/public channels

##### **What does the adversary not know?**  
The adversary does not know the state that G() was run in (The random state that was used to get SK), they do not know SK for E() and SK for D()

##### **Why does the adversary know?**  
It is safer to assume that the adversary knows and allows you to prove that your encryption algorithm is secure in the worst-case scenario. In real life, if an algorithm is safe, it would be widely implemented, thereby greatly reducing the likelihood that the adversary does not know G.E.D.

##### **What do we want from an encryption algorithm?**  
The adversary should not be able to compute the plaintext from ciphertexts  
The adversary should not be able to compute any partial information about the plaintext from the ciphertext. (Perfect Secrecy)  
The adversary should not be able to compute relations between ciphertexts.  
(Perfect indistinguishability, also the vulnerability that led to the downfall of the Enigma machine)

##### **Reduction/Reduced Algorithm**  
Reduction is the act of condensing an algorithm to its mathematical problem, whether it be a computationally hard problem of factoring large integers or discrete logarithms 

The reduced algorithm is the underlying mathematical problem that needs to be solved to “crack” the algorithm.

***

#### **Basics: Functions of an encryption algorithm**  
G($$1^k$$) - Randomised algorithm that produces the SK (Secret key) of k length ($$k = l$$)  
E(SK, m) = c, Algorithm that encrypts the m (Plaintext)  
D(SK, c) = m, Algorithm that decrypts the c (Ciphertext)   
Correctness: When the ciphertext is run through the Decryption function with the SK, you will obtain the original message  
Security: The ciphertext reveals nothing useful to the adversary  
K \= {Set of all Keys}, C \= {Set of all Ciphertexts}, M \= {Set of all Plaintexts}

#### **Perfect Secrecy (Shannon’s Secrecy Definition)**  
C is all possible ciphertexts, M is all possible messages   
$$\forall$$ probability distribution over M  
$$\forall$$ c in C, m in M  
$$P(M = m) = P(M = m|C = c)$$ or $$P(M = m) = P(M = m|E(sk, m) = c)$$
If an algorithm has perfect secrecy, the chance that the adversary guesses the non-zero probability of m is equal to the chance that the adversary guesses the non-zero probability of m when they know c.

In simple terms, the ciphertext, c, does not give out any information on what the plaintext, m, is.

#### **Perfect Indistinguishability**  
$$\forall m, m^{'} \in M$$  
$$\forall c \in C$$  
$$P(C = c|M = m) = P(C = c|M = m^{'})$$  
If an algorithm has perfect indistinguishability, it means that there is an equal chance between all messages that the ciphertext, when decoded, can be.

In simple terms, when the adversary has the ciphertext, there is an equal chance that the ciphertext is $$m_1$$, and $$m_2$$   
E.g. $$c = \text{oadbwyeifabo}$$, $$m_1 = \text{hello}$$, $$m_2 =  \text{你好}$$, $$P(M = m_1) = P(M = m_2)$$  
It does not matter which language, datatype or length of the message or ciphertext, c has an equal chance of being any of m. It does not allow the adversary to deduce any information about the contents of the message. 

If an algorithm satisfies Perfect Indistinguishability, it also satisfies Perfect Secrecy, vice versa. (In practice, OTP is the only useful algorithm that achieves this)

***  

#### **One-Time Pad (Encryption System)**  
$$m_1, c, SK \in \{0,1\}^{l}$$ is the security parameter  
(Security parameter is the possible type of input, key and output for this encryption system, in this case it is 0 and 1, which is binary, where l is the length of the message)  
G($$1^l$$) chooses SK at random $$\{0,1\}^l$$  
E(SK, m) = $$SK \oplus m = c$$  
D(SK, c) = $$SK \oplus c = m$$  

This encryption scheme achieves Perfect Secrecy as there is only 1 key to a message that matches a predetermined ciphertext, vice versa, making all messages and ciphertexts equally likely, achieving Perfect Secrecy

##### **Proof:**  
Fix $$m, c \in \{0,1\}^l$$  
$$P(C = c) = P_{SK}(SK \oplus m = c) = P_{SK}(SK = m \oplus c) = \frac{1}{2^l}$$  
Thus, $$c, m_1, m_2$$  
$$P_{SK}(C = c|M = m_1) = P_{SK}(C = c|M = m_2)$$ (Perfect Indistinguishability)  
Since One-Time Pad G.E.D achieves Perfect Indistinguishability => Perfect Secrecy  

In simple terms, m and c can only be 1 or 0, for the length of the message. The probability that any c is equivalent to a predetermined c is $$\frac{1}{2^l}$$ as there are 2 possible states for each digit of SK and SK has a length of l.  
Since $$SK \oplus m = c$$, there is only 1 possible SK when XORed with a predetermined m gives c, hence the probability that any SK when XORed with a predetermined m gives c is the same as $$\frac{1}{2^l}$$.
Following XOR logic, we can determine that $$P_{SK} (SK = m \oplus c) = \frac{1}{2^l}$$ as there is only 1 possible option of SK when predetermined $$m \oplus c$$  
Thus, $$P_{SK} (m_1 \oplus SK = c) = P_{SK} (m_2 \oplus SK = c)$$, as $$P(SK \oplus c = m)$$ are equal for all possible SK.  
Since One-Time Pad G.E.D achieves Perfect Indistinguishability => Perfect Secrecy  

##### **Why a One-Time Pad can only be used once (Without changing SK):**  
Consider the case that 2 messages of length l, each encrypted using the same SK.  
Let $$m = m_1 || m_2$$, $$m^{'} = m_{1}^{'} || m_{2}^{'}$$, $$c = c_1 || c_1$$ where $$m_1 = m_2$$ and $$m_{1}^{'} \neq m_{2}^{'}$$ , since the ciphertext is made up of $$c_1 || c_1$$, due to XOR logic, we know that the first half and second half of the plaintext is the same.  
We know that $$m_{1}^{'} \neq m_{2}^{'}$$, we can deduce that $$P_{SK}(m^{'} \oplus SK = c) = 0$$ as there is no SK that can XOR 2 different messages into the same ciphertext, while we know that $$P_{SK} (m \oplus SK = c) > 0$$, as there is a SK that can XOR 2 same messages into the same ciphertext.  
As Perfect Indistinguishability requires $$P(C = c|M = m) = P(C = c|M = m)$$, and we know that $$P_{SK} (m \oplus SK = c) \neq P_{SK} (m^{'} \oplus SK = c)$$, this shows that if One-Time Pad is used twice (without changing SK), it will not have Perfect Indistinguishability.  

***