# Group theory elements and quadratic residues concepts

## Generators

<p>
  A unit (element which has an inverse) $G \in Z_{n}^{*}$ is called a generator or primitive root of $Z_{n}^{*}$ if for every $a \in Z_{n}^{*}$ we have $G^{k} = a$ for some $k$, i.e. if we start with $G$ and keep multiplying by $G$ eventually we will se every element. This is why $G$ has to be a unit, if it wasn't it could only generate multiples of $G$, as already shown in https://github.com/xyzhyn/Number-theory-background (Fermat's primality test section). Being a unit is not enough by the way, since for example $3 \mod 11$ is not a generator, while being a unit.<br>

  The theorem states: let $p$ be a prime, then $Z_{p}^{\ast}$ contains exactly $\phi(p - 1)$ generators. In general, for every divisor $d | p - 1$, $Z_{p}^{\ast}$ contains $\phi(d)$ elements of order $d$.<br>
  
  
</p>

### Proof

<p>
 Let $p$ prime; from Euler's Theorem:

 $x^{\phi(p - 1)} \equiv 1 (\mod p - 1)$<br>
 
 and from the CRT and Euler's Theorem:

 $x^{\phi(p - 1)} \equiv 1 (\mod p - 1)$<br>
 $\equiv$<br>
 $x^{\phi(\tau_{1}^{?})} \equiv 1 (\mod \tau_{1}^{?})$<br>
 $x^{\phi(\tau_{2}^{?})} \equiv 1 (\mod \tau_{2}^{?})$<br>
 $\dots$<br>
 $x^{\phi(\tau_{?}^{?})} \equiv 1 (\mod \tau_{?}^{?})$<br>
 
 Which means that the solutions are $\phi(p - 1)$. Note that the 'evil detail' is that the Euler's Theorem 
 holds only if $x$ and $p - 1$ are coprime, and the same goes for every 
 $x^{\phi(\tau_{?}^{?})} \equiv 1 (\mod \tau_{?}^{?})$. Since the solutions to every congruence are 
 $\phi(\tau_{?}^{?})$ and the solutions to the initial congruence are them multiplied, by the 
 multiplicativity of the Totient the number of solutions, i.e. the numbers $< p - 1$ which raised to $\phi(p - 1)$ 'produce' 1 are exactly $\phi(p - 1)$. This means that (since it's clear that $p - 1$ is not a 
 generator) there are $\phi(p - 1)$ generators $< p$. Now, why then can't we consider the same reasoning with 
 the Fermat's Little Theorem and state that there are $x^{p-1}$ generators? Because it doesn't ensure that 
 $x^{p - 1}$ with $0 < x < p$ will produce distinct results from $x^{2}$ to $x^{p - 1}$, while: 

 $x^{\phi(\tau_{1}^{?})} \equiv 1 (\mod \tau_{1}^{?})$<br>
 $x^{\phi(\tau_{2}^{?})} \equiv 1 (\mod \tau_{2}^{?})$<br>
 $\dots$<br>
 $x^{\phi(\tau_{?}^{?})} \equiv 1 (\mod \tau_{?}^{?})$<br>

 produce

 $x^{\phi(p - 1)} \equiv 1 (\mod p - 1)$<br>

 *distinct* (and therefore unique) solutions (as already proved in the CRT article), and this means that those solutions are effectively generators. The reason why they are *distinct* is because the same solutions are 'collapsed' into a single solution in $x^{\phi(p - 1)} \equiv 1 (\mod p - 1)$, while the different solutions always produce different (unique) results $(\mod p - 1)$.

</p>
