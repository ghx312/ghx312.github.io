---
layout: terminal_centered
title: CHSH Game
permalink: /notes/qc/nonlocalgames/chshgame
date: 2026-07-19
category: notes
---

# Introduction  
CHSH Game was created by John Clauser, Michael Horne, Abner Shimony, and Richard Holt. It is a non-local game which means that there are 2 players, Alice and Bob, who are cooperating in order to win a game and a referee who will obey the rules strictly.  

### Rules  
The rules of the CHSH Game is as follows:  
- Alice and Bob are allowed to cooperate and form a common strategy before the game begins  
- Alice and Bob are forbidden from communicating during the game  
- Alice's answer and question are, $$a$$ and $$x$$ respectively, while Bob's answer and question are, $$b$$ and $$y$$ respectively.  
- All questions and answers are bits: $$x, y, a, b, \in \{0,1\}$$  
- The referee chooses the questions $$(x, y)$$ uniformly at random  
- The answers $$(a, b)$$ win for the questions $$(x, y)$$ if $$a \oplus b = x \land y$$  

## Classical Strategy  
Firstly, let us note down the truth table for this game  
- In order for Alice and Bob to win when the questions are $$(0, 0) \rightarrow a = b$$  
- In order for Alice and Bob to win when the questions are $$(0, 1) \rightarrow a = b$$  
- In order for Alice and Bob to win when the questions are $$(1, 0) \rightarrow a = b$$  
- In order for Alice and Bob to win when the questions are $$(1, 1) \rightarrow a \neq b$$  

From this truth table, we can see that if both Alice and Bob choose to pick the same number always regardless of the given bit, they will win 3 out of 4 times. 
It can be shown that 75% is the best win rate any classical strategy can give for the CHSH Game.  

### Proof  

Let $$a(x)$$ and $$b(y)$$ be the responses Alice and Bob give respectively with the given parameters. For the first case, where $$(x, y) = (0, 0)$$ we can see that $$a(0) = b(0)$$ for Alice and Bob to win. For the second case, where $$(x, y) = (0, 1)$$, we can see that $$a(0) = b(1)$$ for Alice and Bob to win. For the third case, where $$(x, y) = (1, 0)$$, we can see that $$a(1) = b(0)$$ for Alice and Bob to win.  

From these first 3 cases, we can see that $$b(1) = a(0) = b(0) = a(1)$$. However, this implies that the strategy loses in the final case $$(x, y) = (1, 1)$$ as it requires $$a(1) \neq b(1)$$. Thus, there is no deterministic classical strategy that wins every time, or at least have a win rate of more than 75%.  

However, it makes us wonder if there is a better strategy with a higher win rate. This bring us to the quantum strategy.  

## Quantum Strategy  
### Pre-requisites  
In order to fully understand the quantum strategy, there is some pre-requisite knowledge to have. All of it can be found [here](/notes/qc/qubits).  

### Initialisation  
The quantum strategy starts of by letting both Alice and Bob share a pair of entangled qubits, $$\ket{\phi^+}$$. Denote Alice's qubit as qubit A, and Bob's qubit as qubit B. When Alice receives $$x$$, she will measure her qubit at angle $$\alpha(x)$$, where $$\alpha(x)$$ is a function that outputs an angle given the corresponding input. When Bob receives $$y$$, he will measure his qubit at an angle $$\beta(y)$$  

We can define Alice's measurement basis through the angle given by $$\alpha(x)$$ as $$\{\ket{\psi_{\alpha}}, \ket{\psi_{\alpha + \frac{\pi}{2}}}\}$$ and Bob's measurment basis through the angle given by $$\beta(x)$$ as $$\{\ket{\psi_{\beta}, \psi_{\beta + \frac{\pi}{2}}}\}$$.  

Let us calculate the overlap between the two different measuremnet basis.  

$$\braket{\psi_\alpha|\psi_\beta} = \cos\alpha\cos\beta + \sin\alpha\sin\beta = \cos(\alpha - \beta)$$  

This overlap represents how much the first measurement basis resembles the second measurement basis.  

Let us now construct the unitary matrix $$U_\theta$$ for Alice and Bob:  

$$U_\theta = \begin{pmatrix} \cos\theta \ \sin\theta \\ \cos(\theta + \frac{\pi}{2}) \ \sin(\theta + \frac{\pi}{2}) \end{pmatrix} = \begin{pmatrix} \cos\theta \ \sin\theta \\ -\sin\theta \ \cos\theta \end{pmatrix}$$  

This unitary matrix will allow Alice and Bob to “turn” the matrix by some degree theta as the current technology only allows
us to measure using the standard basis. So instead of measuring at angle $$\theta$$, we “turn” the qubit by and then measure using the standard measurement basis.  

We then find the tensor product of the 2 measurement basis from Alice and Bob, converting it into a 2 qubit system and
comparing it against the entangled qubit that both Alice and Bob currently hold. This gives us the overlap which will aid in
us calculating the probability of the qubit collapsing into a certain state which will help us in finding the optimal angle
differences. This equation over here represents the overlap for the state 00, as we are using $$\alpha$$ and $$\beta$$.  

$$\braket{\psi_\alpha \otimes \psi_\beta | \phi^+ } = \frac{\cos(\alpha)\cos(\beta) + \sin(\alpha)\sin(\beta)}{\sqrt{2}} = \frac{\cos(\alpha - \beta)}{\sqrt{2}}$$  

Through Born’s Rule, we know that the probability of an output happening is the overlap between the output’s state and the
current state squared, hence, we can already calculate the probability of any outcome in a 2 qubit system.  

$$P(a = 0, b = 0) = (\braket{\psi_\alpha \otimes \psi_\beta | \phi^+ })^2 = \frac{1}{2}\cos^2(\alpha - \beta)$$  

Now let us combine the 2 unitary matrices for Alice and Bob, this will help for future calculations we will be using this state instead of manually finding the overlap for all 4 states like in the above.  

$$U_\alpha \otimes U_\beta = (\ket{0}\bra{\psi_\alpha} + \ket{1}\bra{\psi_{\alpha + \frac{\pi}{2}}})(\ket{0}\bra{\psi_\beta} + \ket{1}\bra{\psi_{\beta + \frac{\pi}{2}}})$$  

$$= \ket{00}\bra{\psi_\alpha \otimes \psi_\beta} + \ket{01}\bra{\psi_\alpha \otimes \psi_{\beta + \frac{\pi}{2}}} + \ket{10}\bra{\psi_{\alpha + \frac{\pi}{2}} \otimes \psi_\beta} + \ket{11}\bra{\psi_{\alpha + \frac{\pi}{2}} \otimes \psi_{\beta + \frac{\pi}{2}}}$$  

## Derivation of Optimal Angles  
Let us first find the overlap of all 4 states using the tensor product between the 2 unitary matrix:  

$$(U_0 \otimes U_\frac{\pi}{8})\ket{\phi^+} = \ket{00}\braket{\psi_0 \otimes \psi_\frac{\pi}{8}|\phi^+} + \ket{01}\braket{\psi_0 \otimes \psi_\frac{5\pi}{8}|\phi^+} + \ket{10}\braket{\psi_\frac{\pi}{2} \otimes \psi_\frac{\pi}{8}|\phi^+} + \ket{11}\braket{\psi_\frac{\pi}{2} \otimes \psi_\frac{5\pi}{8}|\phi^+}$$  

$$= \frac{1}{\sqrt{2}}[\cos(-\frac{\pi}{8})\ket{00} + \cos(-\frac{5\pi}{8})\ket{01} + \cos(\frac{3\pi}{8})\ket{10} + \cos(-\frac{\pi}{8})\ket{11}]$$  

This gives us the overlap for every single possible outcome:  

$$\ket{00} \rightarrow \braket{\psi_\alpha \vert \psi_\beta}$$  

$$\ket{01} \rightarrow \braket{\psi_\alpha \vert \psi_{\beta + \frac{\pi}{2}}}$$  

$$\ket{10} \rightarrow \braket{\psi_{\alpha + \frac{\pi}{2}} \vert \psi_\beta}$$  

$$\ket{11} \rightarrow \braket{\psi_{\alpha + \frac{\pi}{2}} \vert \psi_{\beta + \frac{\pi}{2}}}$$  

These are their corresponding overlaps, through Born's rule, we can find out the probability of $$a = b$$ and $$a \neq b$$:  

$$\text{Pr}(a = b) = \frac{1}{2}|\braket{\psi_\alpha|\psi_\beta}|^2 + \frac{1}{2}|\braket{\psi_{\alpha + \frac{\pi}{2}}|\psi_{\beta + \frac{\pi}{2}}}|^2 = \cos^2(\alpha - \beta)$$  

$$\text{Pr}(a \neq b) = \frac{1}{2}|\braket{\psi_\alpha|\psi_{\beta + \frac{\pi}{2}}}|^2 + \frac{1}{2}|\braket{\psi_{\alpha + \frac{\pi}{2}}|\psi_\beta}|^2 = \sin^2(\alpha - \beta)$$  

As we know that from the truth table in the classical strategy tells us that we need $$\alpha = \beta$$ for 3 of the 4 possible question. Hence, the winning probability is:  

$$W = \frac{1}{4}[\cos^2(\alpha_0 - \beta_0) + \cos^2(\alpha_0 - \beta_1) + \cos^2(\alpha_1 - \beta_0) + \sin^2(\alpha_1 - \beta_1)]$$  

Rewriting the winning probability by using double angle formula and expressing the inner trigo terms as $$d_i$$.  

$$d_1 = \alpha_0 - \beta_0$$  

$$d_2 = \alpha_0 - \beta_1$$  

$$d_3 = \alpha_1 - \beta_0$$  

$$d_4 = \alpha_1 - \beta_1$$  

$$W = \frac{1}{2} + \frac{1}{8}[\cos2d_1 + \cos2d_2 + \cos2d_3 - \cos2d_4]$$ 

As we are trying to maximise our winning probability, we must maximise the inner term:  

$$S = \cos2d_1 + \cos2d_2 + \cos2d_3 - \cos2d_4$$  

In order to maximis $$S$$, we will take the partial derivative of all 4 variables, $$\alpha_0, \alpha_1, \beta_0$$ and $$\beta_1$$ and set them to 0, in order to find the maxima.  

$$\frac{\partial S}{\partial \alpha_0} = -2\sin2d_1 - 2\sin2d_2 = 0 \rightarrow \sin2d_1 = -\sin2d_2$$  

$$\frac{\partial S}{\partial \alpha_1} = -2\sin2d_3 + 2\sin2d_4 = 0 \rightarrow \sin2d_3 = \sin2d_4$$  

$$\frac{\partial S}{\partial \beta_0} = 2\sin2d_1 + 2\sin2d_3 = 0 \rightarrow \sin2d_1 = -\sin2d_3$$  

$$\frac{\partial S}{\partial \beta_1} = 2\sin2d_2 - 2\sin2d_4 = 0 \rightarrow \sin2d_2 = \sin2d_4$$  

From the partial derivatives we have obtained a system of equations:  

$$\sin2d_1 = -\sin2d_2$$  

$$\sin2d_3 = \sin2d_4$$  

$$\sin2d_1 = -\sin2d_3$$  

$$\sin2d_2 = \sin2d_4$$  

From this we can see that $$\sin2d_1 = -\sin2d_2 = -\sin2d_3 = -\sin2d_4$$ using the Tsirelson's Bound, we know that our equation $$S \leq 2\sqrt{2}$$. Hence, by solving the above system of equations and that $$S = 2\sqrt{2}$$, we can find that a valid set of solution is:  

$$-d_1 = d_2 = d_3 = \frac{\pi}{8}$$  

$$d_4 = \frac{3\pi}{8}$$  

Reminder than these are the optimal angles difference between Alice and Bob, Alice and Bob are free to choose any set of angles for their own angle functions, $$\alpha$$ and $$\beta$$ as long as it fulfils $$-d_1 = d_2 = d_3 = \frac{\pi}{8}$$ and $$d_4 = \frac{3\pi}{8}$$.

### Strategy Description  
Using the difference in basis angles that we found before, we let Alice and bob use that set of basis angles to get the most optimal winning strategy.  

Alice's actions:  
If Alice receives the question $$x = 0$$, she applies $$U_{\alpha(0) = 0}$$ to her qubit A.  
If Alice receives the question $$x = 1$$, she applies $$U_{\alpha(1) = \frac{\pi}{4}}$$ to her qubit A.  

After Alice applies this operation, she measures qubit A with a standard basis measurement, $$\{\ket{0}, \ket{1}\}$$, and sets her answer, $$a$$, to be the measured outcome.  

Bob's action:  
If Bob receives the question $$y = 0$$, he applies $$U_{\beta(0) = \frac{\pi}{8}}$$ to his qubit B.  
If Bob receives the question $$y = 1$$, he applies $$U_{\beta(1) = -\frac{\pi}{8}}$$ to his qubit B.  

After Bob applies this operation, he measures qubit B with a standard basis measurement, $$\{\ket{0}, \ket{1}\}$$, and sets his answer, $$b$$, to be the measured outcome.  

### Case-by-case Analysis  
##### Case 1  
Questions given: $$(x, y) = (0, 0)$$  
Win condition: $$a = b$$  

$$(U_0 \otimes U_\frac{\pi}{8})\ket{\phi^+} = \ket{00}\braket{\psi_0 \otimes \psi_\frac{\pi}{8}|\phi^+} + \ket{01}\braket{\psi_0 \otimes \psi_\frac{5\pi}{8}|\phi^+} + \ket{10}\braket{\psi_\frac{\pi}{2} \otimes \psi_\frac{\pi}{8}|\phi^+} + \ket{11}\braket{\psi_\frac{\pi}{2} \otimes \psi_\frac{5\pi}{8}|\phi^+}$$  

$$= \frac{1}{\sqrt{2}}[\cos(-\frac{\pi}{8})\ket{00} + \cos(-\frac{5\pi}{8})\ket{01} + \cos(\frac{3\pi}{8})\ket{10} + \cos(-\frac{\pi}{8})\ket{11}]$$  

$$\text{Pr}((a, b) = (0, 0)) = \frac{1}{2}\cos^2(-\frac{\pi}{8}) = \frac{2 + \sqrt{2}}{8}$$  

$$\text{Pr}((a, b) = (0, 1)) = \frac{1}{2}\cos^2(-\frac{5\pi}{8}) = \frac{2 - \sqrt{2}}{8}$$  

$$\text{Pr}((a, b) = (1, 0)) = \frac{1}{2}\cos^2(\frac{3\pi}{8}) = \frac{2 - \sqrt{2}}{8}$$  

$$\text{Pr}((a, b) = (1, 1)) = \frac{1}{2}\cos^2(-\frac{\pi}{8}) = \frac{2 + \sqrt{2}}{8}$$  

As the win condition stated is $$a = b$$, the probability of winning this round is: 

$$\text{Pr}(a = b) = \frac{2 + \sqrt{2}}{4}$$

##### Case 2  
Questions given: $$(x, y) = (0, 1)$$  
Win condition: $$a = b$$  

$$(U_0 \otimes U_{-\frac{\pi}{8}})\ket{\phi^+} = \ket{00}\braket{\psi_0 \otimes \psi_{-\frac{\pi}{8}}|\phi^+} + \ket{01}\braket{\psi_0 \otimes \psi_\frac{3\pi}{8}|\phi^+} + \ket{10}\braket{\psi_\frac{\pi}{2} \otimes \psi_{-\frac{\pi}{8}}|\phi^+} + \ket{11}\braket{\psi_\frac{\pi}{2} \otimes \psi_\frac{3\pi}{8}|\phi^+}$$  

$$= \frac{1}{\sqrt{2}}[\cos(\frac{\pi}{8})\ket{00} + \cos(-\frac{3\pi}{8})\ket{01} + \cos(\frac{5\pi}{8})\ket{10} + \cos(\frac{\pi}{8})\ket{11}]$$  

$$\text{Pr}((a, b) = (0, 0)) = \frac{1}{2}\cos^2(\frac{\pi}{8}) = \frac{2 + \sqrt{2}}{8}$$  

$$\text{Pr}((a, b) = (0, 1)) = \frac{1}{2}\cos^2(-\frac{3\pi}{8}) = \frac{2 - \sqrt{2}}{8}$$  

$$\text{Pr}((a, b) = (1, 0)) = \frac{1}{2}\cos^2(\frac{5\pi}{8}) = \frac{2 - \sqrt{2}}{8}$$  

$$\text{Pr}((a, b) = (1, 1)) = \frac{1}{2}\cos^2(\frac{\pi}{8}) = \frac{2 + \sqrt{2}}{8}$$  

As the win condition stated is $$a = b$$, the probability of winning this round is: 

$$\text{Pr}(a = b) = \frac{2 + \sqrt{2}}{4}$$

##### Case 3  
Questions given: $$(x, y) = (1, 0)$$  
Win condition: $$a = b$$  

$$(U_\frac{\pi}{4} \otimes U_\frac{\pi}{8})\ket{\phi^+} = \ket{00}\braket{\psi_\frac{\pi}{4} \otimes \psi_\frac{\pi}{8}|\phi^+} + \ket{01}\braket{\psi_\frac{\pi}{4} \otimes \psi_\frac{5\pi}{8}|\phi^+} + \ket{10}\braket{\psi_\frac{3\pi}{4} \otimes \psi_\frac{\pi}{8}|\phi^+} + \ket{11}\braket{\psi_\frac{3\pi}{4} \otimes \psi_\frac{5\pi}{8}|\phi^+}$$  

$$= \frac{1}{\sqrt{2}}[\cos(\frac{\pi}{8})\ket{00} + \cos(-\frac{3\pi}{8})\ket{01} + \cos(\frac{5\pi}{8})\ket{10} + \cos(\frac{\pi}{8})\ket{11}]$$  

$$\text{Pr}((a, b) = (0, 0)) = \frac{1}{2}\cos^2(\frac{\pi}{8}) = \frac{2 + \sqrt{2}}{8}$$  

$$\text{Pr}((a, b) = (0, 1)) = \frac{1}{2}\cos^2(-\frac{3\pi}{8}) = \frac{2 - \sqrt{2}}{8}$$  

$$\text{Pr}((a, b) = (1, 0)) = \frac{1}{2}\cos^2(\frac{5\pi}{8}) = \frac{2 - \sqrt{2}}{8}$$  

$$\text{Pr}((a, b) = (1, 1)) = \frac{1}{2}\cos^2(\frac{\pi}{8}) = \frac{2 + \sqrt{2}}{8}$$  

As the win condition stated is $$a = b$$, the probability of winning this round is:  

$$\text{Pr}(a = b) = \frac{2 + \sqrt{2}}{4}$$  

##### Case 4  
Questions given: $$(x, y) = (1, 1)$$  
Win condition: $$a \neq b$$  

$$(U_\frac{\pi}{4} \otimes U_{-\frac{\pi}{8}})\ket{\phi^+} = \ket{00}\braket{\psi_\frac{\pi}{4} \otimes \psi_{-\frac{\pi}{8}}|\phi^+} + \ket{01}\braket{\psi_\frac{\pi}{4} \otimes \psi_\frac{3\pi}{8}|\phi^+} + \ket{10}\braket{\psi_\frac{3\pi}{4} \otimes \psi_{-\frac{\pi}{8}}|\phi^+} + \ket{11}\braket{\psi_\frac{3\pi}{4} \otimes \psi_\frac{3\pi}{8}|\phi^+}$$  

$$= \frac{1}{\sqrt{2}}[\cos(\frac{3\pi}{8})\ket{00} + \cos(-\frac{\pi}{8})\ket{01} + \cos(\frac{7\pi}{8})\ket{10} + \cos(\frac{3\pi}{8})\ket{11}]$$  

$$\text{Pr}((a, b) = (0, 0)) = \frac{1}{2}\cos^2(\frac{3\pi}{8}) = \frac{2 - \sqrt{2}}{8}$$  

$$\text{Pr}((a, b) = (0, 1)) = \frac{1}{2}\cos^2(-\frac{\pi}{8}) = \frac{2 + \sqrt{2}}{8}$$  

$$\text{Pr}((a, b) = (1, 0)) = \frac{1}{2}\cos^2(\frac{7\pi}{8}) = \frac{2 + \sqrt{2}}{8}$$  

$$\text{Pr}((a, b) = (1, 1)) = \frac{1}{2}\cos^2(\frac{3\pi}{8}) = \frac{2 - \sqrt{2}}{8}$$  

As the win condition stated is $$a \neq b$$, the probability of winning this round is:  

$$\text{Pr}(a \neq b) = \frac{2 + \sqrt{2}}{4}$$  

### Summary  
From all the different possible sets of answers, we can see that Alice and Bob win about 85% of the time in every case. This
also happens to be the best quantum strategy.  
We can also verify this by using the formula for our win rate when determining the optimal angle difference between
measurement basis for Alice and Bob.  

$$W = \frac{1}{2} + \frac{1}{8}[\cos(-\frac{\pi}{4}) + \cos(\frac{\pi}{4}) + \cos((\frac{\pi}{4})) - \cos(\frac{3\pi}{4})] \approx 0.85$$  

[CHSH Game Simulation](https://colab.research.google.com/drive/1a24ivblwGOxDptdB4q78GI6E_a0JK1YO?usp=sharing)