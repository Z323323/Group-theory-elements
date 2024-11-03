# Group theory elements and quadratic residues concepts

## Generators

<p>
  A unit (element which has an inverse) $G \in Z_{n}^{*}$ is called a generator or primitive root of $Z_{n}^{*}$ if for every $a \in Z_{n}^{*}$ we have $G^{k} = a$ for some $k$, i.e. if we start with $G$ and keep multiplying by $G$ eventually we will se every element [ for a power $k$ such as $G^{n} > G^{k}$ ]. Hence being a unit is not enough, infact for example $3 \mod 11$ is not a generator, while being a unit.<br>

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
  solution of $x^{3} - 1 = 0$. The reason of this can be searched following [ https://en.wikipedia.org/wiki/Lagrange_polynomial ] 
  and considering that it's easy to reproduce the roots of a polynomial of degree $n$ with a multiplication of simple binomials 
  of the form:

  $(x - root_{1})(x - root_{2})\dots(x - root_{n})$
  
  Polynomials division is a really complex process 
  (https://en.wikipedia.org/wiki/Polynomial_long_division), 
  but we can speed it up using web resources producing: $x^{3} - 1 = (x - 1)(x^{2} + x + 1)$.<br>
  $x - 1$'s solution is trivial, while $x^{2} + x + 1 = 0$ is a $2nd$ degree polynomial which can be solved 
  using the resolution formula [ https://github.com/xyzhyn/Quadratic-formula-derivation ]:

  $\displaystyle x = \frac{- 1 \pm \sqrt{(1)^{2} - 4 \cdot (1 \cdot 1)}}{2 \cdot 1}$<br>
  $\displaystyle x = \frac{- 1 \pm \sqrt{- 3}}{2}$
  
  $\displaystyle x_{1} = \frac{- 1 + i\sqrt{3}}{2}$<br>
  $\displaystyle x_{2} = \frac{- 1 - i\sqrt{3}}{2}$

  to be continued...
  
</p>

### Proof of generators theorem

<p>
Here I'll try to further explain [ https://crypto.stanford.edu/pbc/notes/numbertheory/gen.html ].<br>
By Fermat:
  
$x^{p - 1} - 1 = 0 (\mod p)$

We know that this equation has $p - 1$ solutions (roots) $(\mod p)$. Let $q^{k}$ be a prime power dividing $p - 1$. Here we know from the former section that $q^{k}$ could be easily $1$ or $2$. We can then rewrite the equation as:

$x^{p - 1} - 1 = (x^{q^{k}} - 1)g(x) = 0 (\mod p)$

where $g(x)$ is a $p - 1 - q^{k}$ polynomial since the reasoning about polynomials divisions. From the former section we know that $(x^{q^{k}} - 1)$ has at most $q^{k}$ roots and $g(x)$ has at most $p - 1 - q^{k}$ roots, and since their product has $p - 1$ **different** roots, we see that there are exactly $q^{k}$ **distinct** solutions to $x^{q^{k}} - 1 = 0 (\mod p)$.<br>

$x^{p - 1} - 1 = 0 (\mod p)$<br>
$\equiv$<br>
$x^{q_{1}^{k_{1}}} - 1 = 0 (\mod p)$<br>
$x^{q_{2}^{k_{2}}} - 1 = 0 (\mod p)$<br>
$\dots$<br>
$x^{q_{?}^{k_{?}}} - 1 = 0 (\mod p)$<br>
$->$<br>
$x^{p - 1} \equiv 1 (\mod p)$<br>
$\equiv$<br>
$x^{q_{1}^{k_{1}}} \equiv 1 \mod p$<br>
$x^{q_{2}^{k_{2}}} \equiv 1 \mod p$<br>
$\dots$<br>
$x^{q_{?}^{k_{?}}} \equiv 1 \mod p$<br>

Warning: this does not follow the CRT but the systems of congruences are verified.
Now, since every congruence is actually a part of the **distinct** solutions $(\mod p)$ and every congruence has $q_{?}^{k_{?}}$ solutions where every $q_{?}^{k_{?}}$ is a co-factor of $p - 1$, we can be sure that every co-factor aka non-coprime number of $p - 1$ will produce $1$ [ $x^{q_{?}^{k_{?}}} \equiv 1$ ] before $x^{p - 1}$ which means that, since they are co-factors of $p - 1$ and [ $x^{p - 1} \equiv 1 (\mod p)$ ] they will 'produce' $1$ from $1$ to $p - 1$, $n$ number of times equal to:

$n =$<br>
$\\{p - 1$ if $q_{?}^{k_{?}} = 1\\}$<br>
$\\{\frac{p - 1}{2}$ if $q_{?}^{k_{?}} = p - 1\\}$<br>
$\\{q_{?}^{k_{?}}$ in every other case}

which in turn means that they will never 'produce' the whole $Z_{p}^{\ast}$ at $x^{p - 1} - 1 = 0 (\mod p)$.

This means that $Z_{p}^{\ast} \backslash \\{\\{q_{1}^{k_{1}}\\} \cup \\{q_{2}^{k_{1}}\\} \dots \cup \\{q_{?}^{k_{1}}\\}\\}$ 'produce' $x^{p - 1} \equiv 1 (\mod p)$ and do not 'produce' $1$ before that power. But this not enough to prove this theorem by the way. We need to prove that $\phi(p - 1)$ is correct, and we need to prove that $Z_{p}^{\ast} \backslash \\{\\{q_{1}^{k_{1}}\\} \cup \\{q_{2}^{k_{1}}\\} \dots \cup \\{q_{?}^{k_{1}}\\}\\}$ can't produce the same number as result of the mult. by itself.
Now $q_{1}^{k_{1}} + q_{2}^{k_{2}} + \dots + q_{?}^{k_{?}}$ are exactly the number of coprimes to $p - 1$, but note that $q_{1}^{k_{1}} + q_{2}^{k_{2}} + \dots + q_{?}^{k_{?}}$ comprehends $1^{1}$ too, hence:

$|Z_{p}^{\ast}| - q_{1}^{k_{1}} - q_{2}^{k_{2}} \dots - q_{?}^{k_{?}} = (p - 1) - q_{1}^{k_{1}} - q_{2}^{k_{2}} \dots - q_{?}^{k_{?}}$<br>
$=$<br>
$(p - 2) + \\{(p - 1)\\} - 1^{1} - q_{1}^{k_{1}} - q_{2}^{k_{2}} \dots - q_{?}^{k_{?}}$

and since $|\\{(p - 1)\\}| = 1$

$(p - 2) + \\{(p - 1)\\} - 1^{1} - q_{1}^{k_{1}} - q_{2}^{k_{2}} \dots - q_{?}^{k_{?}} = \phi(p - 1)$

</p>
