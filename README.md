# Group theory elements and quadratic residues concepts

## Generators

<p>
  A unit (element which has an inverse) $G \in Z_{n}^{*}$ is called a generator or primitive root of $Z_{n}^{*}$ if for every $a \in Z_{n}^{*}$ we have $G^{k} = a$ for some $k$, i.e. if we start with $G$ and keep multiplying by $G$ eventually we will se every element. This is why $G$ has to be a unit, if it wasn't it could only generate multiples of $G$, as already shown in https://github.com/xyzhyn/Number-theory-background (Fermat's primality test section), even though every element is a unit if we consider $Z_{n}^{*}$ where $n$ is prime. Being a unit is not enough by the way, since for example $3 \mod 11$ is not a generator, while being a unit.<br>

  The theorem states: let $p$ be a prime, then $Z_{p}^{\ast}$ contains exactly $\phi(p - 1)$ generators.
</p>

### Polynomials of degree $n$ have at most $n$ roots (solutions) over $Z_{p}$

<p>
  [ https://crypto.stanford.edu/pbc/notes/numbertheory/poly.html ].
</p>

### Further reasoning on the former

<p>
  $p$ prime:<br>
  $x \equiv 1 \mod p$<br>
  $x - 1 \equiv 0 \mod p$<br>
  $x = 1 \mod p$<br>
  
  Let's see what actually happens increasing the degree:<br>
  $x^{2} \equiv 1 \mod p$<br>
  $x^{2} - 1 \equiv 0 \mod p$<br>
  $x = 1 \mod p$ or $x = -1 \mod p$<br>

  Now the game starts getting interesting.<br>
  $x^{3} \equiv 1 \mod p$<br>
  $x^{3} - 1 \equiv 0 \mod p$<br>
  We know $x = 1 \mod p$ is a solution, hence  we can use $x - 1$ to divide $x^{3} - 1$ since it is a 
  solution of $x^{3} - 1 = 0$. The reason of this can be searched following this 
  https://en.wikipedia.org/wiki/Lagrange_polynomial. Polynomials division is a really complex process 
  (https://en.wikipedia.org/wiki/Polynomial_long_division), 
  but we can speed it up using web resources producing: $x^{3} - 1 = (x - 1)(x^{2} + x + 1)$.<br>
  $x - 1$'s solution is trivial, while $x^{2} + x + 1 = 0$ is a $2nd$ degree polynomial which can be solved 
  using the resolution formula [ https://github.com/xyzhyn/Quadratic-formula-derivation ]:

  $\displaystyle x = \frac{1 \pm \sqrt{(-1)^{2} - 4 \cdot (1 \cdot 1)}}{2 \cdot 1}$
  
  $\displaystyle x_{1} = \frac{1 + i\sqrt{3}}{2}$<br>
  $\displaystyle x_{2} = \frac{1 - i\sqrt{3}}{2}$

  to be continued...
  
  
  
</p>

### Proof of generators theorem

<p>

</p>
