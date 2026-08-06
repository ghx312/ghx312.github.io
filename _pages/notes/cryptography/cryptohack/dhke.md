---
layout: terminal_centered
title: CryptoHack - DHKE
permalink: /notes/cryptography/cryptohack/dhke/
date: 2026-07-22
category: notes
---

## Introduction to Public Key Cryptography  
### Modular Exponentiation  
#### Trapdoor Functions  
Trapdoor Functions are problems that cryptosystems use to ensure that they are secure by using math problems that are one-way.  
Meaning that it is hard to inverse a certain operation, for example the 2 problems that we will be using in RSA is the Integer Factorization Problem and also the Discrete Logarithm Problem. 

What consitutes a trapdoor function? A trapdoor function is one that cannot be easily inverted without the necessary information, usually these problems do not have a solution in polynomial time, such that for sufficiently large values used the computation required is grows faster than the values used. This helps to keep your data safe.  

##### Integer Factorization Problem  
Given a large composite number $$N$$, find its prime decomposition, or to express it in a form where all of its multiplicants are primes of some positive integer power.  
In RSA, the version of this problem that we are dealing with are given $$N = p \times q$$, where p and q are large distinct unknown primes. Given N find p and q.  

##### Discrete Logarithm Problem  
Given $$g^x \equiv h \pmod{N}$$, and the values $$x, h, N$$ find g.  

#### Code  
In order to do modular exponentiation in Python, we can use the inbuild function {% raw %}`pow(m, e, n)`{% endraw %}, where $$m$$ is your base, $$e$$ is your exponent and $$n$$ is your modulus.  

### Public Keys  
#### Encryption in RSA  
In order to encrypt messages in RSA, you need your public exponent usually denoted by $$e = 65537$$ or $$e = 0x1001$$ which is $$65537$$ in Hex. You also need you public modulus, $$N$$ where $$N = p \times q$$, where $$p$$ and $$q$$ are your private factors.  

We encrypt messages by letting our message be the base and modular exponentiating it by our public exponent and reducing it by our public modulus.  

$$m^e \equiv c \pmod{N}$$  

where $$c$$ is the encrypted message or the resultant ciphertext.  

### Euler's Totient  
Euler's Totient function is a function that gives you the number of integers that are positive, lesser than the input parameter and coprime to the input parameter. The function's formula is given by:  

$$N = p_1^{e_1} \times p_2^{e_2} \times \dots \times p_i^{e_i}$$  

where $$p_i$$ are the prime factors of $$N$$.  

$$\phi(N) = N(1 - \frac{1}{p_1})(1 - \frac{1}{p_2})\dots(1 - \frac{1}{p_i})$$  

However, if we are able to express N's prime decomposition as:  

$$N = p_1 \times p_2 \times \dots \times p_i$$  

Then we can simplify the Euler's Totient function's formula to:  

$$\phi(N) = (p_1 - 1)(p_2 - 1)\dots(p_i - 1)$$  

In RSA, we will be using the second formula where the formula we are usually using will be in this exact form:  

$$\phi(N) = (p - 1)(q - 1)$$  

### Private Keys  
The private key in RSA is given by calculating the private exponent, usually denoted by $$d$$, which fulfils the condition below:  

$$d \times e \equiv 1 \pmod{\phi(N)}$$  

We can calculate this using a generalized form of Fermat's Little Theorem:  

$$e^{\phi(N) - 2} \equiv e^{-1} \pmod{\phi(N)}$$  

#### Code  
In python in order to find the multiplicative inverse, we can also use the pow function, the code is given as {% raw %}`pow(e, -1, Totient_N)`{% endraw %}.  

### RSA Decryption  
In RSA in order to decrypt, we modularly exponentiate the ciphertext by the private key, $$d$$.  

$$c^d \equiv m^{e + d} \equiv m^{\phi(N) + 1} \equiv m \pmod{N}$$  

This is true due to Euler's Totient Theorem which states that:  

$$a^{\phi(N)} \equiv 1 \pmod{N}, \text{GCD}(N, a) = 1$$  

#### Code  
In python in order to decrypt we would use this piece of code {% raw %}`pow(c, d, n)`{% endraw %}  

### RSA Signatures  
RSA Signing is useful as it helps the messager and receiver to ensure that their messages are truely from each other, this involved the use of Hash Functions.  

#### Hash Functions  
Hash Functions are one-way functions where $$F(x) = y$$ but it is hard find the inverse of $$F(x)$$ such that $$F^{-1}(y) = x$$.  
A property of the hash function is also that it is deterministic, which means that although every single input will lead to a seemingly random string of text, if you were to input the same message twice, you would get the same string of text every single time.  

#### Signatures  
Alice and Bob wants to talk to each other using the RSA cryptosystem that we have learnt previously, however, Mallory can perform what is known as a Man-in-the-Middle attack, there they intercept messages from both sides and edit them before sending it out. When Bob receives a message from Alice, he would not know if the message is from Mallory or Alice as they both can encrypt and send him messages. Hence, we can ultilise the hash function from above to give us a unique hash from our message.  

$$H(m) = s$$  

Alice can then "sign" the hash by encrypting it:  

$$S \equiv s^e \pmod{N}$$  

Alice then sends both the hash and the ciphertext to Bob. When Bob decrypts both the hash and ciphertext, he is unable to invert the hash to see if the message that produced that hash is the same as the decrypted ciphertext. However, he can hash the decrypted ciphertext to check if it is the same as the hash. If they are the same, this means that the message was indeed from Alice, however, if they are different, this means that Mallory has edited the ciphertext before sending it to Bob.  

#### Code  
We can import the SHA256 hash function from the hashlib library, remember to let the messasge be in bytes, as the hash function only works in bytes.  
{% raw %}`message = b"crypto{Immut4ble_m3ssag1ng}"`{% endraw %}  
{% raw %}`hash = hashlib.sha256(message).hexdigest()`{% endraw %}  

This will produce the hash of our message, we will the import the {% raw %}`bytes_to_long`{% endraw %} function from the {% raw %}`Crypto.Util.number`{% endraw %} library in order to turn our hash into integers so that we can encrypt it using RSA.  

{% raw %}`int_hash = bytes_to_long(hash)`{% endraw %}  

We will then encrypt this hash as per normal using RSA.  

### Factoring  
Factoring is a big part of RSA as if we are able to factor the public modulus $$N$$, we can recover the 2 private prime factors $$p$$ and $$q$$, allowing us to compute $$\phi(N)$$ and recovering the private exponent. Hence, there exist many number factoring algorithms, some exploit certain properties of the primes used in creating $$N$$, some are just for general factoring. However, there does not exist a classical algorithm that factors numbers in polynomial time, this means that RSA is safe if a minimum of 2048-bit public modulus is used, which is the standard safety protocol.  

In this challenge, you are required to factor the number $$510143758735509025530880200653196460532653147$$, which is a fairly small number compared to normal RSA challenges.
There are multiple methods to factor this number, I personally use [factor.db](https://factordb.com/) which is a rainbow table that stores a database full of numbers in their prime decomposition form, this doesn't work all the time as it requires users to submit the prime decomposition of the numbers themselves, however, for most numbers this should be sufficent. I also use [YAFU](https://github.com/bbuhrow/yafu) which stands for Yet Another Factoring Unit, it is a all purpose number factorer and it helps you to factor numbers on an industrial scale, however, I do not recommend running this for too long as it is very power intensive. There also a multitude of methods to factor numbers, however, these methods are enough for this challenge. 

### Monoprime  
Monoprime's description gives us a clue `Why is everyone so obsessed with multiplying two primes for RSA. Why not just use one?`, as we know that $$N = p \times q$$ if only 1 prime was used, that would mean that $$N = p^2$$. $$N$$ is a perferct square, we simply have to take the square root of $$N$$ to recover the prime factors. We can then calculate $$\phi(N)$$ and find the private key.  

#### Code  
In order to find exact roots of large numbers, I recommend using the `math` library and specifically the `math.sqrt(number)` function as it is able to process large numbers with high accuracy.  

### Manyprime  
Manyprime's decription gives us a clue `Using one prime factor was definitely a bad idea so I'll try using over 30 instead.` This tells us that $$N$$ was made with many primes, however the size of $$N$$ is still the same, this tells me that those 30 primes are relatively small to the ones that we usually deal with. We can use [YAFU](https://github.com/bbuhrow/yafu) to factorise this and calculate $$\phi(N)$$.

### Salty  
Salty's decryption gives us a clue `Smallest exponent should be fastest, right?`, reading from the code `e = 1`, we can see that no modular exponentiation was performed, this means that the ciphertext is actually just the original message.  

### Modulus Inutilis  
Modulus Inutilis' descryption actually does not helps us that much. `My primes should be more than large enough now!` this statement is true as they are using the recommended size of 1024-bit primes, which is the industry standard. However, the vulnerability actually lies in the public exponent $$e = 3$$, as 3 is a small number there is a chance that the ciphertext did not require modular reduction, allowing us to find the exact cube root of the ciphertext to recover the message.  

###  Working with Fields  
The challenge is relatively easy and has nothing to do wither Fields, but here are the information you need to understand them.  

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
Fields are made of 2 abelian groups, with the first abelian group using the + binary operator and the second using $$\times$$ binary operator. Let us denote a field of elements as $$\mathbb{F}_p = \{0, 1, 2, \dots, p - 1\}$$, where $$p$$ is prime.  

Under the addition operator, the entire set of element is a valid abelian group  

Under the multiplication operator, the entire set of elements (Except for 0) is a valid abelian group  

The distributive law states that $$a \times (b + c) = (a \times b) + (a \times c)$$  

Modular Arithmetic is actually a field by itself (Provided that the modulo is prime)  

### Generators  
An element, $$g$$, of the multiplicative part of the Field, $$\mathbb{F}_p^\times$$, is called a generator if its subgroup $$H = \langle g \rangle = \{g^0, g^1, g^2, \dots g^{p - 2}\}$$ contains all elements of $$\mathbb{F}_p^\times$$. Equivalently, if the $$g$$ is a generator iff $$\operatorname{ORDER}(g) = p - 1$$, where all $$p - 1$$ elements of $$H$$ are distinct. (The order of a group is simply now many elements it contains)

#### Generator Tests  
In order to test if an element in $$\mathbb{F}_p$$ is a generator, we can first do prime decomposition on $$p - 1$$.  

$$p - 1 = \prod q_i^{k_i}$$  

An element $$g$$ is a generator if:  

$$g^{\frac{p - 1}{q_i}} \not\equiv 1 \pmod{p}$$  

for all $$q_i$$.  

### Computing Public Values  
The Diffie-Hellman Protocol uses the Discrete Logarithmic Problem as it is assumed to be "hard" for carefully chosen groups. We must first choose a modulo prime, $$p$$ to work with. It is important to choose a prime, $$p$$, such that it is in the form of $$p = 2q + 1$$ where $$q$$ is a large prime. This protects the Diffie-Hellamn Protocol from the [Pohlig-Hellman algorithm](INSERTLINKTOPOHLIGHELLMANALGORITHMPAGE).  

The user then picks a secret key, $$a$$, such that $$0 < a < p - 1$$ and calculates.  

$$A \equiv g^a \pmod{p}$$  

where $$A$$ is our public key, and $$a$$ is our private key.  

### Computing Shared Values  
Your partner will follow the same steps in [Computing Public Values](http://ghx312.github.io/notes/cryptography/cryptohack/dhke/#computing-public-values), where their public and private keys are $$B$$ and $$b$$ respectively.  

They will then transfer their public-key through the insecure channel towards you. This will be useful when calculating the shared secret.  

The shared secret is given by:  

$$S = B^a \pmod{p}$$  

where $$S$$ is the shared secret.  

Your partner will also calculate the shared secret:  

$$S = A^b \pmod{p}$$  

As modular exponentiation is commutative (meaning that $$x^{ab} \equiv x^{ba} \pmod{N}$$), the secret key obtained by both you and your partner will be identical.  

$$S \equiv B^a \equiv A^b \equiv g^{ab} \equiv g^{ba} \pmod{p}$$  

### Deriving Symmetric Keys  
After deriving your shared symmetric secret keys, we still require a symmetric encryption system to utilise these keys. In the challenge, we are told that Alice and Bob are using AES, we are given the required values to calculate and derive the shared symmetric secret keys.  

In order to understand how to decrypt go to [Symmetric Encryption](/notes/cryptography/cryptohack/symmetric_encryption/)  

### Pohlig-Hellman
Pohlig-Hellman is an attack on the discrete logarithm problem in subgroup's whose order is a smooth integer (Smooth meaning easily factorable).  



