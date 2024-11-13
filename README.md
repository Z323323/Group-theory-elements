# Group theory elements and quadratic residues concepts

## Analysis of the Totient function for powers of primes

A deep understanding of the Totient function is required in order to really understand what the actual hell is happening. First: let's see how the Totient of the power of a prime divides that number.

$\displaystyle \frac{p^q}{\phi(p^{q})} = \frac{p^{q}}{p^{q} - p^{q - 1}} = \frac{p^{q}}{p^{q - 1}(p - 1)} = \frac{p}{p - 1} = 1 + \frac{1}{p - 1}$

And now look at this, this holds for any prime $p$:

$\displaystyle \frac{p}{\phi(p)} = \frac{p}{p - 1} = 1 + \frac{1}{p - 1}$

Now we can state that if

$\displaystyle \frac{p^q}{\phi(p^{q})} = 1 + \frac{1}{p - 1}$

then

$\displaystyle \phi(p^{q})(1 + \frac{1}{p - 1}) = p^{q}$

and also

$\displaystyle (\phi(p^{q})2^{S})(1 + \frac{1}{p - 1}) = p^{q}2^{S}$

Now if we consider $p^{q}2^{S}$ as $p - 1$ where $p$ is a prime number which has a $p - 1$ of that kind:

$\displaystyle p - 1 = \phi(p^{q}) 2^{S} ( 1 + \frac{1}{p - 1})$

$\displaystyle p - 1 = \displaystyle \phi(p^{q})2^{S} + \frac{\phi(p^{q})2^S}{p - 1} = \phi(p^{q})2^{S} + \frac{\phi(p^{q})}{p^{q}}$

Now we can recognise that if

$\displaystyle p - 1 = \phi(p^{q})2^{S} + \frac{\phi(p^{q})}{p^{q}}$

then

$\displaystyle p = \phi(p^{q})2^{S} + \frac{\phi(p^{q})}{p^{q}} + \frac{p^q}{\phi(p^{q})} = \phi(p^{q})2^{S} + 1$

Hence we can state that 

$p = \phi(p^{q})2^{S} + 1$

and

$p - 1 = \phi(p^{q})2^{S}$

This means that the Totient function doesn't give a shit about the degree of $p$, and at the same time it represents the order of the subgroups of $Z_{p}^{*}$. Now, since we know that the order of the subgroups is not affected by the degree of $p$ we can count how many times the Totient repeat itself given a degree $p - 1$.

$\displaystyle (1 + \frac{1}{p - 1})(p - 1) = p - 1 + 1 = p$

Then by Fermat:

$a^{p - 1} \equiv 1 \mod p$

and therefore




## Generators

<p>
  A unit (element which has an inverse) $G \in Z_{p}^{*}$ is called a generator or primitive root of $Z_{p}^{*}$ if for every $a \in Z_{p}^{*}$ we have $G^{k} = a$ for $k$ such that $p > k > 0$, i.e. if we start with $G$ and keep multiplying by $G$ we will se every element once we get $G^{p - 1}$. Hence being a unit is not enough, infact for example $3 \mod 11$ is not a generator, while being a unit.<br>

  The theorem states: let $p$ be a prime, then $Z_{p}^{\ast}$ contains exactly $\phi(p - 1)$ generators.

  Now if $n$ is a non-prime integer $> 1$ we would have $\phi(n)$ generators for $Z_{n}^{\ast}$, otherwise if $p$ is prime then $\phi(\phi(p)) = \phi(p - 1)$ and $\phi(\phi(p))$ is a more general rule for cyclic groups. Since I'm always reasoning about groups composed by elements such as every $e \in Z_{n}^{\ast}, 0 < e < n$ we can conclude that every $Z_{p}^{*}$ has $\phi(p - 1)$ generators, since it's always cyclic, and $Z_{n}^{\ast}$ with $n$ non-prime has $\phi(n)$ generators since it's always non-cyclic.

  $Z_{n}^{\ast}$, implies $n = 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$ with or without $2^{S}$. By the Euler's Theorem and the CRT:

  $x^{\phi(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})} \equiv 1 \mod 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
  $\equiv$<br>
  $x^{\phi(2^{S})} \equiv 1 \mod 2^{S}$<br>
  $x^{\phi(q_{1}^{k_{?}})} \equiv 1 \mod q_{1}^{k_{?}}$<br>
  $x^{\phi(q_{2}^{k_{?}})} \equiv 1 \mod q_{2}^{k_{?}}$<br>
  $\dots$<br>
  $x^{\phi(q_{?}^{k_{?}})} \equiv 1 \mod q_{?}^{k_{?}}$<br>

  Now let's take for example $x^{\phi(q_{1}^{k_{?}})} \equiv 1 \mod q_{1}^{k_{?}}$ and re-apply this construction, by the Euler's Theorem, Fermat's Theorem and CRT:

  $x^{\phi(q_{1}^{k_{?}})} \equiv 1 \mod q_{1}^{k_{?}}$<br>
  $\equiv$<br>
  $x_{1}^{q_{1} - 1} \equiv 1 \mod q_{1}$<br>
  $\dots$<br>
  $x_{k_{?}}^{q_{1} - 1} \equiv 1 \mod q_{1}$

  $x_{1}^{q_{1}} \equiv x_{1} \mod q_{1}$<br>
  $\dots$<br>
  $x_{k_{?}}^{q_{1}} \equiv x_{k_{?}} \mod q_{1}$<br>
  $\equiv$<br>
  $x^{(q_{1})^{k_{?}}} \equiv x^{(q_{1})^{k_{?}}} \mod q_{1}^{k_{?}}$<br>

  but 

  $x^{(q_{1})^{k_{?}}} \mod q_{1}^{k_{?}}$

  was

ok sono quasi sicuro che visto che $(q_{1} - 1)(q_{1} - 1)\dots$ assicura un resto di 1 allora x^q^k ha resto 1, ma non ha tanto senso, forse devo provare a dimostrarlo.

  $(q_{1} - 1)(q_{1} - 1) = q_{1}^2 -2q_{1} + 1$<br>
  $(q_{1} - 1)(q_{1} - 1)(q_{1} - 1) = (q_{1}^2 - 2q_{1} + 1)(q_{1} - 1) = q_{1}^3 - q_{1}^2 -2q_{1}^2 + 2q_{1} + q_{1} - 1 = q_{1}^3 - 3q_{1}^2 + 3q_{1} - 1$<br>
  $(q_{1} - 1)(q_{1} - 1)(q_{1} - 1)(q_{1} - 1) = (q_{1}^3 - 3q_{1}^2 + 3q_{1} - 1)(q_{1} - 1) = q_{1}^4 - q_{1}^3 - 3q_{1}^3 + 3q_{1}^2 + 3q_{1}^2 - 3q_{1} - q_{1} + 1 = q_{1}^4 - 4q_{1}^3 + 6q_{1}^2 - 4q_{1} + 1$

  


  
  and by the corollary of the Fermat's Little Theorem:

  $x^{\phi(q_{1}^{k_{?}})} \equiv 1 \mod q_{1}^{k_{?}}$<br>
  $\equiv$<br>
  $x_{1}^{n(q_{1} - 1)} \equiv 1 \mod q_{1}$<br>
  $\dots$<br>
  $x_{k_{?}}^{n(q_{1} - 1)} \equiv 1 \mod q_{1}$

  
  Now let's take for example $x^{\phi(2^{S})} \equiv 1 \mod 2^{S}$ and re-apply this construction:

  $x^{\phi(2^{S})} \equiv 1 \mod 2^{S}$<br>
  $\equiv$<br>
  $x_{1}^{2} \equiv 1 \mod 2$<br>
  $\dots$<br>
  $x_{S}^{2} \equiv 1 \mod 2$



  
</p>

## Cyclic groups
<p>
  When $Z_{n}^{*}$ has a generator, we call $Z_{n}^{*}$ a cyclic group. If $G$ is a generator we write $Z_{n}^{*} = \langle G \rangle$.
</p>

## Cyclic subgroups
<p>
  A subgroup of $Z_{n}^{*}$ is a non-empty subset $H$ of $Z_{n}^{*}$ such that if $a, b \in H$, then $ab \in H$.<br> It's pretty simple to figure out that this definition is quite open/not-restricted, infact we don't give a shit about subgroups, we are only interested in cyclic subgroups.<br>
  A cyclic subgroup of $Z_{n}^{*}$ is a non-empty subset $H$ of $Z_{n}^{*}$ such that every $e \in H$ are generated taking one random element $r \in Z_{n}$, and all the elements generated by $r^{k} \mod n$ with $k > 1$ until $r^{k} \equiv 1 \mod n$.
</p>

### Ex.
<p>
  Any $a \in Z_{n}^{*}$ can be used to generate cyclic subgroups:

  $\langle a \rangle = \\{a, a^2, \dots, a^d = 1\\}$ for some $d$

  Any group is always a subgroup of itself (wow). $\\{1\\}$ is always a subgroup of any group (wow). 
</p>

## Lagrange's Theorem 

<p>
  Let $H$ be a subgroup of $Z_{n}^{*}$ of size $m$. Then $m|\phi(n)$.

  By Fermat:
  
  $x^{p - 1} - 1 = 0 (\mod p)$

  We know that this equation has $p - 1$ solutions (roots) $(\mod p)$. Let $q^{k}$ be a prime power dividing $p - 1$. We can then rewrite the equation as:

  $x^{p - 1} - 1 = (x^{q^{k}} - 1)g(x) = 0 (\mod p)$

  where $g(x)$ is a $p - 1 - q^{k}$ polynomial. From [ Qua ci andrà il link alla dimostrazione del teorema fondamentale dell'algebra ] we know that $(x^{q^{k}} - 1)$ has at most $q^{k}$ roots and $g(x)$ has at most $p - 1 - q^{k}$ 
  roots, and since their product has $p - 1$ **different** roots, we see that there are exactly $q^{k}$ **distinct** solutions to $x^{q^{k}} - 1 = 0 (\mod p)$.<br>
Now, since every $p - 1$ where $p$ is prime, is representable as $p - 1 = 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$, we know that any congruence of these kind of forms:

  $x^{2^{S}} \equiv 1 \mod p$<br>
  $x^{q_{1}^{k_{?}}} \equiv 1 \mod p$<br>
  $x^{q_{2}^{k_{?}}} \equiv 1 \mod p$<br>
  $\dots$<br>
  $x^{q_{?}^{k_{?}}} \equiv 1 \mod p$

  'produces' $2^{S}, q_{1}^{k_{?}}, q_{2}^{k_{?}}, \dots, q_{?}^{k_{?}}$ **distinct** solutions, hence a subgroup of order equal to $2^{S}, q_{1}^{k_{?}}, q_{2}^{k_{?}}, \dots, q_{?}^{k_{?}}$.
  Now we can take this congruence:

  $x^{(2^{S})q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}} = x^{p - 1} \equiv 1 \mod p$<br>
  
and

  $x^{2^{S}(\phi(q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}))} \equiv 1 \mod 2^S$

From the corollary of Fermat's Little Theorem we know that $x^{k(2^{S})} \equiv 1 \mod 2^{S}$, and since the reasoning about 'contained solutions', the $2^{S}$ order subgroup will be contained $q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$ times at $x^{p - 1} \equiv 1 \mod p$. Which means that it's order divides $\phi(n)$. The same goes for all the other co-factors. Now let's suppose that we had $x^{z} \equiv 1 \mod p$ where $z < p - 1$ doesn't divide $p - 1$. By Fermat $x^{p - 1} \equiv 1 \mod p$ must hold, hence by the corollary, since $x^{k(z)} \equiv 1 \mod p$ it must be $k(z) = p - 1$. But $z$ is not a co-factor of $p - 1$, hence $k = \frac{p - 1}{z} \notin N$, and therefore it can't be the order of a subgroup, which proves the theorem.<br>
The reason why $x^{z} \equiv 1 \mod p$ with $z$ coprime with $p - 1$ is that the former construction made by Ben Lynn, is true, but only if we consider complex numbers, hence it's not true for $z \in N$.<br>

</p>

### Proof of generators theorem

<p>
From the former proof, we know that since every $q$ which divides $p - 1$ is not a generator (since they form subgroups and not the whole $Z_{p}^{\ast})$ then it must be that all the coprimes are generators, since all elements of $Z_{p}^{\ast}$ 'produce' $1$ at $x^{p - 1} \mod p$ by Fermat. This is enough actually to state that the number of generators are $\phi(p - 1)$ for $Z_{p}^{\ast}$ and $\phi(n)$ for $Z_{n}^{\ast}$, but if you want to follow the calculation:

$\displaystyle \frac{2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}}{2 / q_{1} / q_{2} / \dots / q_{?}}$

Where "/" = "either or", produces:

$2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$ or $2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$ or $2^{S}q_{1}^{k_{?}}q_{2}^{k_{?} - 1} \dots q_{?}^{k_{?}}$ or $2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?} - 1}$

All these are $nonGenerators$ calculated factor-by-factor, now to get the number of $generators$, we will need to consider each one of the former solutions, thus:<br>
[ https://github.com/xyzhyn/Totient-extension-to-non-primes ]

[ $(x \cdot a) - (x \cdot b) = x(a - b)$ ]

$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} = \phi(2^{S})q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} = 2^{S}\phi(q_{1}^{k_{?}})q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?}}q_{2}^{k_{? - 1}} \dots q_{?}^{k_{?}} = 2^{S}q_{1}^{k_{?}}\phi(q_{2}^{k_{?}}) \dots q_{?}^{k_{?}}$<br>
$\dots$<br>
or<br>
$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{? - 1}} = 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots \phi(q_{?}^{k_{?}})$<br>

Now keep in mind that operating these subtractions we are actually considering $2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$, $n_{cofactors} - 1$ more times than we should (i.e. we should subtract all of $- 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$, etc. from $2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$ only $1$ time, not $n_{cofactors}$ times, but since this is required to solve this theorem, what we are effectively finding is the number of generators $+ 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$, multiplied $n_{cofactors} - 1$ times). Now we need to get a sum of all these terms in order to find the $generators$, hence these: 

$\phi(2^{S})q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
$2^{S}\phi(q_{1}^{k_{?}})q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
$2^{S}q_{1}^{k_{?}}\phi(q_{2}^{k_{?}}) \dots q_{?}^{k_{?}}$<br>
$\dots$<br>
$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots \phi(q_{?}^{k_{?}})$<br>

equal

$\phi(2^{S})\phi(q_{1}^{k_{?}})\phi(q_{2}^{k_{?}}) \dots \phi(q_{?}^{k_{?}}) + (n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})$

and finally

$generators + (2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})(n_{cofactors} - 1)  = \phi(2^{S})\phi(q_{1}^{k_{?}})\phi(q_{2}^{k_{?}}) \dots \phi(q_{?}^{k_{?}}) + (n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})$

$generators = \phi(p - 1)$

</p>

#### Little extra found along the battles

Since the 'cancellation law' [ https://github.com/xyzhyn/Fermat-Little-Theorem-proof ]:

$(x)(x) \equiv (x)(1) \mod p$<br>
-><br>
$x \equiv 1 \mod p$

is not possible if $x < p - 1$ and $x \neq 1$.


  $nonGenerators = 2^{S - 1}q_{1}^{k_{?} - 1}q_{2}^{k_{?} - 1} \dots q_{?}^{k_{?} - 1}$

  indeed

  $2^{S - 1}q_{1}^{k_{?} - 1}q_{2}^{k_{?} - 1} \dots q_{?}^{k_{?} - 1} + \phi(p - 1) =$

  $2^{S - 1}q_{1}^{k_{?} - 1}q_{2}^{k_{?} - 1} \dots q_{?}^{k_{?} - 1} + (2^{S} - 2^{S - 1})(q_{1}^{k_{?}} - q_{1}^{k_{?} - 1})(q_{2}^{k_{?}} - q_{2}^{k_{?} - 1}) \dots (q_{?}^{k_{?}} - q_{?}^{k_{?} - 1}) =$
  
  -----<br>

  $(2^{S} - 2^{S - 1})(q_{1}^{k_{?}} - q_{1}^{k_{?} - 1})(q_{2}^{k_{?}} - q_{2}^{k_{?} - 1}) \dots (q_{?}^{k_{?}} - q_{?}^{k_{?} - 1}) =$

  $(2^{S}q_{1}^{k_{?}} - 2^{S}q_{1}^{k_{?} - 1} - 2^{S - 1}q_{1}^{k_{?}} + 2^{S - 1}q_{1}^{k_{?} - 1})(q_{2}^{k_{?}} - q_{2}^{k_{?} - 1}) \dots (q_{?}^{k_{?}} - q_{?}^{k_{?} - 1})$

  -----<br>

  $(q_{2}^{k_{?}} - q_{2}^{k_{?} - 1}) \dots (q_{?}^{k_{?}} - q_{?}^{k_{?} - 1}) = q_{2}^{k_{?}}q_{?}^{k_{?}} - q_{2}^{k_{?}}q_{?}^{k_{?} - 1} - q_{2}^{k_{?} - 1}q_{?}^{k_{?}} + q_{2}^{k_{?} - 1}q_{?}^{k_{?} - 1}$

  -----<br>

  $(2^{S}q_{1}^{k_{?}} - 2^{S}q_{1}^{k_{?} - 1} - 2^{S - 1}q_{1}^{k_{?}} + 2^{S - 1}q_{1}^{k_{?} - 1})(q_{2}^{k_{?}}q_{?}^{k_{?}} - q_{2}^{k_{?}}q_{?}^{k_{?} - 1} - q_{2}^{k_{?} - 1}q_{?}^{k_{?}} + q_{2}^{k_{?} - 1}q_{?}^{k_{?} - 1})=$
  
  $2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}q_{?}^{k_{?} - 1} - 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?} - 1}q_{?}^{k_{?}} + 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?} - 1}q_{?}^{k_{?} - 1} \dots$
  
  $- 2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?}}q_{?}^{k_{?}} + 2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?}}q_{?}^{k_{?} - 1} + 2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?} - 1}q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?} - 1}q_{?}^{k_{?} - 1} \dots$
  
  $- 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}}q_{?}^{k_{?}} + 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}}q_{?}^{k_{?} - 1} + 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?} - 1}q_{?}^{k_{?}} - 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?} - 1}q_{?}^{k_{?} - 1} \dots$
  
  $+ 2^{S - 1}q_{1}^{k_{?} - 1}q_{2}^{k_{?}}q_{?}^{k_{?}} - 2^{S - 1}q_{1}^{k_{?} - 1}q_{2}^{k_{?}}q_{?}^{k_{?} - 1} - 2^{S - 1}q_{1}^{k_{?} - 1}q_{2}^{k_{?} - 1}q_{?}^{k_{?}} + 2^{S - 1}q_{1}^{k_{?} - 1}q_{2}^{k_{?} - 1}q_{?}^{k_{?} - 1}$

  

  $

  

  
</p>
