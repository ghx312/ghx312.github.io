---
layout: terminal_centered
title: Qubits
permalink: /notes/qc/qubits
date: 2026-07-19
category: notes
---

# Introduction  
A qubit is the basic unit of information in quantum computing, while classical bits can be described as a 1 or 0, a qubit is simultaneously a combination of both.  
It is an integral part of the future of computing and cryptography.  

### Fundamental Laws of Qubits  
#### Born's Rule  
The probability of getting outcome X is given by square of the overlap between the actual state and vector representation of outcome X.  

When you measure a qubit $$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$$ in the standard basis:  
- The probability of yielding 0 is $$P(0) = \vert\vert\alpha\vert\vert^2$$  
- The probability of yielding 1 is $$P(1) = \vert\vert\beta\vert\vert^2$$  

#### No-Cloning Theorem  
It is mathematically impossible to create an identical copy of an arbitrary unknown quantum state. 

### Mathematical Notation  
#### Bra-ket Notation  
We represent quantum states using 'kets' $$\ket{\psi}$$. The standard computation basis vectors are defined as orthogonal column vectors:  
- 0 state: $$\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$  
- 1 state: $$\ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$  

We represent quantum conjugate states using 'bra' $$\bra{\psi}$$.  
Note that $$a^*$$ means the conjugate of $$a$$.  
- If $$\ket{\psi} = \begin{pmatrix} a \\ b \end{pmatrix}$$, then $$\bra{\psi} = \begin{pmatrix} a^* \ b^* \end{pmatrix}$$.  

#### Inner Product  
The inner product $$\braket{\phi|\psi}$$ multiplies a Bra and a Ket to yield a scalar. It measure the overlap between 2 quantum states:  
-$$\braket{\phi|\psi} = \begin{pmatrix} a^* \ b^* \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = a^*\alpha + b^*\beta$$  

#### Superposition State  
A general qubit state, $$\ket{\psi}$$ is a linear combination of these basis states:  
-$$\ket{\psi} = \alpha\ket{0} + \beta\ket{1} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$$  

#### The Normalization Law  
When a qubit is measured, it must collapse to either 0 or 1, hence the total probability must equal to 1:  
-$$\vert\vert\alpha\vert\vert^2 + \vert\vert\beta\vert\vert^2 = 1$$  

### Qubit States, Basis and Operations  
#### The Hadamard (Diagonal) Basis  
- State (Diagonal): $$\ket{+} = \frac{1}{\sqrt{2}}(\ket{0} + \ket{1})$$  
- State (Anti-Diagonal): $$\ket{-} = \frac{1}{\sqrt{2}}(\ket{0} - \ket{1})$$  
Both Hadamard Basis if measured using a standard basis detector, have a 50/50 exact change of collapsing into 0 or 1.  

#### Tensor Product  
To combine multiple qubits into a single system, we use the tensor product. For two qubits:  
-$$\ket{0} \otimes \ket{0} = \ket{00} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \otimes \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \cdot 1 \\ 1 \cdot 0 \\ 0 \cdot 1 \\ 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}$$  

General Formula for two-qubit tensor product:  
-$$a \otimes b = \ket{ab} = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix} \otimes \begin{pmatrix} b_1 \\ b_2 \end{pmatrix} = \begin{pmatrix} a_1 \cdot \begin{pmatrix} b_1 \\ b_2 \end{pmatrix} \\ a_2 \cdot \begin{pmatrix} b_1 \\ b_2 \end{pmatrix} \end{pmatrix} = \begin{pmatrix} a_1b_1 \\ a_1b_2 \\ a_2b_1 \\ a_2b_2 \end{pmatrix}$$  

The four basis states for a two-qubit system are $$\ket{00}$$, $$\ket{01}$$, $$\ket{10}$$, $$\ket{11}$$.  

Tensor products represent the combination of 2 individual qubit into 1 qubit. Reminder that all qubits are simply vectors and the tensor product simply converts 2 2-dimensional vectors into 1 4-dimensional vector.  

#### Bell States  
Bell States are important states in quantum computing and cryptography, the Bell State is the smallest unit of entanglement (Between 2 qubits) also known as an ebit.  
- $$\ket{\phi^+} = \frac{1}{\sqrt{2}}(\ket{00} + \ket{11}) = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix}$$, 50% Chance -> 00 state, 50% Chance -> 11 state  
- $$\ket{\phi^-} = \frac{1}{\sqrt{2}}(\ket{00} - \ket{11}) = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 0 \\ 0 \\ -1 \end{pmatrix}$$, 50% Chance -> 00 state, 50% Chance -> 11 state  
- $$\ket{\psi^+} = \frac{1}{\sqrt{2}}(\ket{01} + \ket{10}) = \frac{1}{\sqrt{2}} \begin{pmatrix} 0 \\ 1 \\ 1 \\ 0 \end{pmatrix}$$, 50% Chance -> 01 state, 50% Chance -> 10 state  
- $$\ket{\psi^-} = \frac{1}{\sqrt{2}}(\ket{01} - \ket{10}) = \frac{1}{\sqrt{2}} \begin{pmatrix} 0 \\ 1 \\ -1 \\ 0 \end{pmatrix}$$, 50% Chance -> 01 state, 50% Chance -> 10 state  