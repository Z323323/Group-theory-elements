# Group theory elements and quadratic residues concepts

## Generators

<p>
  A unit (element which has an inverse) $G \in Z_{n}^{*}$ is called a generator or primitive root of $Z_{n}^{*}$ if for every $a \in Z_{n}^{*}$ we have $G^{k} = a$ for some $k$, i.e. if we start with $G$ and keep multiplying by $G$ eventually we will se every element. This is why $G$ has to be unit, if it wasn't it could only generate multiples of $G$, as already shown in https://github.com/xyzhyn/Number-theory-background (Fermat's primality test section). Being a unit is not enough by the way, since for example $3 \mod 11$ is not a generator, while being a unit.<br>

  The theorem states: let $p$ be a prime, then $Z_{p}^{\ast}$ contains exactly $\phi(p - 1)$ generators. In general, for every divisor $d | p - 1$, $Z_{p}^{\ast}$ contains $\phi(d)$ elements of order $d$ (the sum of every $\phi(d)$ ).<br>
  Ok now let's understand why this arcane magic holds.
</p>

### Proof

<p>
  From Fermat's Little Theorem:

  $x^{p - 1} (\mod p) - 1 = 0$

  has $p - 1$ distinct solutions ($p$ is prime obv.), i.e. every element of $Z_{p}^{\ast}$ is a solution. Let $q^{k}$ be a prime power dividing $p - 1$. We can factorize $x^{p - 1} (\mod p) - 1 = 0$ as:

  $x^{p - 1} - 1 = (x^{q^{k}} - 1)g(x) = 0 (\mod p)$

  where

  $g(x) = P(x)^{p - 1 - q^{k}}$

  and $P(x)$ is some polynomial of the degree shown above. $x^{q^{k}} - 1$ has at most $q{k}$ roots:

  $x^{q^{k}} \equiv 1 \mod p$

  and $g(x)$ has at most $p - 1 - q^{k}$ roots, and since their product has $p - 1$ different roots, there are exactly $q^{k}$ solutions to:

  $x^{q^{k}} (\mod p) - 1 = 0$
</p>
