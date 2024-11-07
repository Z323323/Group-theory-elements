# Group theory elements and quadratic residues concepts

## Generators

<p>
  A unit (element which has an inverse) $G \in Z_{p}^{*}$ is called a generator or primitive root of $Z_{p}^{*}$ if for every $a \in Z_{p}^{*}$ we have $G^{k} = a$ for $k$ such that $p > k$, i.e. if we start with $G$ and keep multiplying by $G$ we will se every element once we get $G^{p - 1}$. Hence being a unit is not enough, infact for example $3 \mod 11$ is not a generator, while being a unit.<br>

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
  $x^{3} - 1 \equiv 0 \mod p$
  
  We know $x = 1 \mod p$ is a solution, hence  we can use $x - 1$ to divide $x^{3} - 1$ since it is a 
  co-factor of $x^{3} - 1 = 0$. The reason of this can be searched following [ https://en.wikipedia.org/wiki/Lagrange_polynomial ] 
  and considering that it's easy to reproduce the roots of a polynomial of degree $n$ (which has $n$ roots) with a multiplication of simple binomials 
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

  This means that since $(x^{2} + x + 1)$ is always a polynomial which is part of the final solution (since 
  $2$ is always a divisor of $p - 1$ and since every non trivial prime number is always $> 2$), the 
  intermediate solutions of $x^{p - 1} \equiv 1 \mod p$ will always carry imaginary numbers (until someone 
  proves this statement is wrong), and for some strange reason (I'll ask god why is that) the solutions to 
  $x^{p - 1} \equiv 1 \mod p$ do not, i.e. you always know that the solution is $1$, but this is only 
  because of $\mod p$, otherwise (I'm almost sure that) even $x^{p - 1} - 1 = 0$ has solutions in the 
  complex field. This in turn means that until someone proves a similar 'theory of everything' about 
  multiplicative prime groups (like Fermat's Theorem but for every power [ which I don't think is possible 
  ]) we will never know what happens between $1s$. I guess the only way to calculate this is using the 
  complex field, but since the DLP *seems* to hold until now (2024) I'm assuming such formula hasn't been 
  discovered.<br>
  This whole reasoning is to prepare yourself to the next section which proves the 'generators theorem' 
  using logic assumptions which fall back into the imaginary numbers, i.e. the proof uses imaginary numbers 
  to prove a rule which works for real numbers. Hence, if you face these:

  $\Phi^{q_{1}^{k_{1}}} - 1 = 0 (\mod p)$<br>
  $\Psi^{q_{2}^{k_{2}}} - 1 = 0 (\mod p)$<br>
  $\dots$<br>
  $\Omega^{q_{?}^{k_{?}}} - 1 = 0 (\mod p)$<br>

  note that most of them will have imaginary solutions, which means that if you try to check these on your 
  computer this system won't work. Also the logic works because each
  $q_{1}^{k_{?}}/q_{2}^{k_{?}}/\dots/q_{?}^{k_{?}}$ actually means nothing taken singularly, i.e. the system 
  of congruences holds only if we consider every combination of numbers which polynomials degrees summed 
  produce $p - 1$, so I guess that even here some sort of implicit combination of degrees must hold, and the 
  same goes for every degree, this is why this subject is a hell of a mess.
  produce <br>
  <br>
  to be continued (maybe)...
  
</p>

### Proof of generators theorem

<p>
[ https://crypto.stanford.edu/pbc/notes/numbertheory/gen.html ].<br>
Here I derived a similar while different proof.<br>
By Fermat:
  
$x^{p - 1} - 1 = 0 (\mod p)$

We know that this equation has $p - 1$ solutions (roots) $(\mod p)$. Let $q^{k}$ be a prime power dividing $p - 1$. Here we know from the former section that $q^{k}$ could be easily $1^{1}$ or $2^{?}$. We can then rewrite the equation as:

$x^{p - 1} - 1 = (x^{q^{k}} - 1)g(x) = 0 (\mod p)$

where $g(x)$ is a $p - 1 - q^{k}$ polynomial since the reasoning about polynomials divisions. From the former section we know that $(x^{q^{k}} - 1)$ has at most $q^{k}$ roots and $g(x)$ has at most $p - 1 - q^{k}$ roots, and since their product has $p - 1$ **different** roots, we see that there are exactly $q^{k}$ **distinct** solutions to $x^{q^{k}} - 1 = 0 (\mod p)$.<br>
Thus:

$(\Phi/\Psi/\dots/\Omega)^{p - 1} - 1 = 0 (\mod p)$<br>
$\equiv$<br>
$\Phi^{q_{1}^{k_{1}}} - 1 = 0 (\mod p)$<br>
$\Psi^{q_{2}^{k_{2}}} - 1 = 0 (\mod p)$<br>
$\dots$<br>
$\Omega^{q_{?}^{k_{?}}} - 1 = 0 (\mod p)$<br>
$->$<br>
$(\Phi/\Psi/\dots/\Omega)^{p - 1} \equiv 1 (\mod p)$<br>
$\equiv$<br>
$\Gamma^{2^S} \equiv 1 \mod p$<br>
$\Phi^{q_{1}^{k_{1}}} \equiv 1 \mod p$<br>
$\Psi^{q_{2}^{k_{2}}} \equiv 1 \mod p$<br>
$\dots$<br>
$\Omega^{q_{?}^{k_{?}}} \equiv 1 \mod p$<br>

Now this system is wrong because if we had:<br>

$(x - root_{1})^{q_{1}^{k_{1}}}(x - root_{2}){q_{2}^{k_{2}}} \dots (x - root_{n})^{q_{n}^{k_{n}}}$

$(x - root_{1})^{q_{1}^{k_{1}}}(x - root_{2}){q_{2}^{k_{2}}} \dots (x - root_{n})^{q_{n}^{k_{n}}}$

$(x_{root_{1}} - 1)^{1} \mod p$<br>
$(x_{root_{2}} - 1)^{1} \mod p$<br>
$\dots$<br>
$(x_{root_{2^S}} - 1)^{1} \mod p$<br>
$(x - 1)^{q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}} \equiv 1 \mod p$<br>

which produces

$(x_{root_{1}} - 1)(x_{root_{2}} - 1) \dots (x_{root_{S + 1}} - 1)(x - 1)^{q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}}$

hence this system correctly maps all the roots of $x^{p - 1} - 1 = 0 (\mod p)$



Now the problem is that this system maps $x^{p - 1} - 1 = 0 (\mod p)$ which is not what we want, because this is the solution we already know, i.e. all the numbers from $1$ to $p - 1$, so to obtain a system which maps the non-generators, we need to set something which implies that the $1$ has already been obtained (i.e. a system which only contains roots but which has a lower degree). The straightforward way to do this is to divide the whole roots-polynomial by (x - 1) which is always part of every polynomial. But before doing that since:

$(\Phi/\Psi/\dots/\Omega)^{p - 1} \equiv 1 (\mod p)$<br>
$\equiv$<br>
$\Gamma^{2^S} \equiv 1 \mod p$<br>
$\Phi^{q_{1}^{k_{1}}} \equiv 1 \mod p$<br>
$\Psi^{q_{2}^{k_{2}}} \equiv 1 \mod p$<br>
$\dots$<br>
$\Omega^{q_{?}^{k_{?}}} \equiv 1 \mod p$<br>


$\displaystyle \frac{(x_{root_{1}} - 1)(x_{root_{2}} - 1) \dots (x_{root_{S + 1}} - 1)(x - 1)^{q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}}}{x - 1} =$
$\displaystyle \frac{(x_{root_{1}} - 1)^{q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}}(x_{root_{2}} - 1)^{q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}} \dots (x_{root_{S + 1}} - 1)^{q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}}}{x - 1}$

which is either equal to:

$(x - 1)^{2^{S}(q_{1}^{k_{?} - 1}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})}$ or $(x - 1)^{2^{S}(q_{1}^{k_{?}}q_{2}^{k_{?} - 1} \dots q_{?}^{k_{?}})}$ or $(x - 1)^{2^{S}(q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?} - 1})}$

or (if we solve the numerator before the division):

$(x - 1)^{2^{S - 1}(q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})}$

and since these are the roots, the results produced originate is the number of non-generators. Now, to get the number of generators:

$p - 1 = 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
$->$<br>
$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?}}q_{2}^{k_{? - 1}} \dots q_{?}^{k_{?}}$<br>
or<br>
$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{? - 1}}$<br>

hence:

$(n_{cofactors}) \cdot 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?}}q_{2}^{k_{? - 1}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{? - 1}} = 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - nonGenerators = generators$

and since:

$\displaystyle z(?) + \mu(?) + \lambda(?) + n(?) + \dots$

$\displaystyle y = \frac{? + ? + ? + ? + \dots}{n_{addends}}$

$\displaystyle z(?) + \mu(?) + \lambda(?) + n(?) + \dots = (z + \mu + \lambda + n \dots)y$

this

$- 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$- 2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$- 2^{S}q_{1}^{k_{?}}q_{2}^{k_{? - 1}} \dots q_{?}^{k_{?}}$<br>
or<br>
$- 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{? - 1}}$<br>

equals to

$(- 2^{S - 1} - q_{1}^{k_{?} - 1} - q_{2}^{k_{?} - 1} - \dots - q_{?}^{k_{?} - 1})(n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})$

hence these

$+ 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}$<br>
$+ 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}$<br>
$+ 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}$<br>
$+ 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}$<br>

equal

$(2^{S} + q_{1}^{k_{?}} + q_{2}^{k_{?}} + \dots + q_{?}^{k_{?}})(n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})$

but keep in mind that operating this subtraction we are actually considering $2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}$, $n_{cofactors} - 1$ more times than we should (i.e. we should subtract all of $- 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$, etc. from $2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}$ only $1$ time, not $n_{cofactors}$ times, but since this is required to solve this theorem, what we are effectively finding is the number of generators of $2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}$, multiplied $n_{cofactors} - 1$ times) then: 

$(n_{cofactors}) \cdot 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?}}q_{2}^{k_{? - 1}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{? - 1}} = (n_{cofactors - 1})generators(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}})$

equals to

$(2^{S} + q_{1}^{k_{?}} + q_{2}^{k_{?}} + \dots + q_{?}^{k_{?}})(n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}) + (- 2^{S - 1} - q_{1}^{k_{?} - 1} - q_{2}^{k_{?} - 1} - \dots - q_{?}^{k_{?} - 1})(n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}) = generators$

$(n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})(2^{S} + q_{1}^{k_{?}} + q_{2}^{k_{?}} + \dots + q_{?}^{k_{?}} - 2^{S - 1} - q_{1}^{k_{?} - 1} - q_{2}^{k_{?} - 1} - \dots - q_{?}^{k_{?} - 1}) = generators$

and since [ https://github.com/xyzhyn/Totient-extension-to-non-primes ]:

$(n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})\phi(p - 1) = (n_{cofactors} - 1)generators(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})$





$(x \cdot a) - (x \cdot b) = xa - xb = x(a - b)$<br>
$->$<br>
$(2^{S} - 2^{S - 1})q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$(q_{1}^{k_{?}} - q_{1}^{k_{?} - 1})2^{S}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$(q_{2}^{k_{?}} - q_{2}^{k_{? - 1}})2^{S}q_{1}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$(q_{?}^{k_{?}} - q_{?}^{k_{? - 1}})2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots$<br>

and by [ https://github.com/xyzhyn/Totient-extension-to-non-primes ]:

$\phi(2^{S})q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$\phi(q_{1}^{k_{?}})2^{S}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$\phi(q_{2}^{k_{?}})2^{S}q_{1}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$\phi(q_{?}^{k_{?}})2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots$<br>

Let's think about this result first:

$\displaystyle z(?) + \mu(?) + \lambda(?) + n(?) + \dots$

$\displaystyle y = \frac{? + ? + ? + ? + \dots}{n_{addends}}$

$\displaystyle z(?) + \mu(?) + \lambda(?) + n(?) + \dots = (z + \mu + \lambda + n \dots)y$

Now, since all the former solutions coexist, we need to sum them, obtaining:

$[(\phi(2^{S}) + \phi(q_{1}^{k_{?}}) + \phi(q_{2}^{k_{?}}) + \dots + \phi(q_{?}^{k_{?}})](n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})$<br>

Now this result is not actually the total number of generators, since for every coprime co-factor number of generators we summed $2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}$, hence now we will need to subtract it $(n_{cofactors} - 1)$ number of times (the $- 1$ is because it needs to be added [we need to subtract all other terms from it] one time), hence:

$(n_{cofactors})generators = (n_{cofactors})(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}) - [(\phi(2^{S}) + \phi(q_{1}^{k_{?}}) + \phi(q_{2}^{k_{?}}) + \dots + \phi(q_{?}^{k_{?}})](n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})$<br>

$(n_{cofactors})generators = (n_{cofactors})(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}) + [(\phi(2^{S}) + \phi(q_{1}^{k_{?}}) + \phi(q_{2}^{k_{?}}) + \dots + \phi(q_{?}^{k_{?}})](n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})$<br>



which solutions are

$(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}) - 1$

and

$(2^{S - 1}q_{1}^{k_{? - 1}}q_{2}^{k_{? - 1}} \dots q_{?}^{k_{? - 1}}) - 1$

$(x_{root_{1}} - 1)(x_{root_{2}} - 1) \dots (x_{root_{2^S}} - 1)(x - 1)^{q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}}$

equals

$(x - 1)^{2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}}$

$\displaystyle \frac{(x_{root_{1}} - 1)(x_{root_{2}} - 1) \dots (x_{root_{2^S}} - 1)(x - 1)^{q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}}}{x - 1} = (x - 1)^{2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 1}$

and finally

$(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}) - (2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 1) = \phi(p - 1)$

Here ' $(\Phi/\Psi/\dots/\Omega)$ ' means 'all of them', but when I write $(\Phi/\Psi/\dots/\Omega)^{q_{1}^{k_{?}}/q_{2}^{k_{?}}/\dots/q_{?}^{k_{?}}}$ below, they are meant to be separated, i.e. $\Phi^{q_{1}^{k_{?}}}$ etc. and the same goes for $q_{1}^{k_{?}}/q_{2}^{k_{?}}/\dots/q_{?}^{k_{?}}$, they are always associated to a base in particular.<br>
Warning: this does not follow the CRT but the systems of congruences are verified.
Now, since every congruence is actually a part of the **distinct** solutions $(\mod p)$ and every congruence has $q_{1}^{k_{?}}/q_{2}^{k_{?}}/\dots/q_{?}^{k_{?}}$ solutions where every $q_{1}^{k_{?}}/q_{2}^{k_{?}}/\dots/q_{?}^{k_{?}}$ is a co-factor of $p - 1$, we can be sure that every co-factor aka non-coprime number of $p - 1$ will produce $1$ [ $(\Phi/\Psi/\dots/\Omega)^{q_{1}^{k_{?}}/q_{2}^{k_{?}}/\dots/q_{?}^{k_{?}}} \equiv 1$ ] before $(\Phi/\Psi/\dots/\Omega)^{p - 1}$ which means that they will 'produce' $1$ from $1$ to $p - 1$, $n$ number of times equal to (only in the complex field):

$n = \\{q_{1}^{k_{?}}/q_{2}^{k_{?}}/\dots/q_{?}^{k_{?}}\\}$

which in turn means that they will never 'produce' the whole $Z_{p}^{\ast}$ at $(\Phi/\Psi/\dots/\Omega)^{p - 1} - 1 = 0 (\mod p)$.<br>
[ This one above is one of the hardest steps; remember that every $(\Phi/\Psi/\dots/\Omega)^{q_{1}^{k_{?}}/q_{2}^{k_{?}}/\dots/q_{?}^{k_{?}}} - 1 = 0 (\mod p)$ has $q_{1}^{k_{?}}/q_{2}^{k_{?}}/\dots/q_{?}^{k_{?}}$ roots ].

This means that $Z_{p}^{\ast} \backslash \\{\\{q_{1}^{k_{1}}\\} \cup \\{q_{2}^{k_{1}}\\} \dots \cup \\{q_{?}^{k_{1}}\\}\\}$ 'produce' $x^{p - 1} \equiv 1 (\mod p)$ and do not 'produce' $1$ before that power. But this not enough to prove this theorem by the way. We need to prove that $\phi(p - 1)$ is correct, and we need to prove that $Z_{p}^{\ast} \backslash \\{\\{q_{1}^{k_{1}}\\} \cup \\{q_{2}^{k_{1}}\\} \dots \cup \\{q_{?}^{k_{1}}\\}\\}$ can't produce the same number as result of the mult. by itself.
Now $q_{1}^{k_{1}} + q_{2}^{k_{2}} + \dots + q_{?}^{k_{?}}$ are exactly the number of coprimes to $p - 1$, but note that if we insert $1^{1}$ inside them (which is fair since the reasoning about polynomials division) we will end up having $q_{1}^{k_{1} - 1} + q_{2}^{k_{2} - 1} + \dots + q_{?}^{k_{? - 1}}$ hence:

$|Z_{p}^{\ast}| - 1 - q_{1}^{k_{1} - 1} - q_{2}^{k_{2} - 1} \dots - q_{?}^{k_{? - 1}} = (p - 1) - 1 q_{1}^{k_{1 - 1}} - q_{2}^{k_{2 - 1}} \dots - q_{?}^{k_{? - 1}}$<br>

Now we can notice that $p - 1$ for the same reasoning made up here $q_{1}^{k_{1}}  q_{2}^{k_{2}} \dots - q_{?}^{k_{?}}$, thus:

$p - 2 =  - q_{?}^{k_{?} - 1} - q_{1}^{k_{1} - 1} - q_{2}^{k_{2} - 1} \dots - q_{?}^{k_{?}}

$(p - 2) + \\{(p - 1)\\} - 1^{1} - q_{1}^{k_{1}} - q_{2}^{k_{2}} \dots - q_{?}^{k_{?}}$

and since $|\\{(p - 1)\\}| = 1$

$(p - 2) + \\{(p - 1)\\} - 1^{1} - q_{1}^{k_{1}} - q_{2}^{k_{2}} \dots - q_{?}^{k_{?}} = \phi(p - 1)$

This proves that $\phi(p - 1)$ elements do not produce '1' before $x^{p - 1} - 1 = 0 (\mod p)$. Now since $\\{(p - 1)\\} - 1^{1}$ shows clearly that they are not part of the solution, [ it's obvious by the way, even though $\phi(p - 1)$ still contains $\\{1\\}$ (yea math is comical, and magical) and the reason for this is that $\phi(p - 1)$ is only a reference number which works by construction but we should look at it like it is just a number at this point ] we know that every number left in the set $Z_{p}^{\ast} \backslash \\{\\{q_{1}^{k_{1}}\\} \cup \\{q_{2}^{k_{1}}\\} \dots \cup \\{q_{?}^{k_{1}}\\}\\}$ is coprime with $p - 1$ and it's not $1$ or $p - 1$. Now to finally prove this theorem, let's pull out the almighty 'cancellation law' [ https://github.com/xyzhyn/Fermat-Little-Theorem-proof ]; since:

$(x)(x) \equiv (x)(1) \mod p$<br>
-><br>
$x \equiv 1 \mod p$

is not possible because $x < p$ and $x \neq 1$ since $\\{1\\}$ is not part of the result set, the theorem is proved. In particular this behaviour works for every $a \in Z_{p}^{*} \backslash \\{1\\}$, not only generators.
</p>

## Cyclic groups
<p>
  When $Z_{n}^{*}$ has a generator, we call $Z_{n}^{*}$ a cyclic group. If $G$ is a generator we write $Z_{n}^{*} = \langle G \rangle$.<br> At this point it's quite easy to figure out that $Z_{p}^{*}$ is always a cyclic group.<br>
</p>

## Finite subgroups
<p>
  A subgroup of $Z_{n}^{*}$ is a non-empty subset $H$ of $Z_{n}^{*}$ such that if $a, b \in H$, then $ab \in H$.<br> It's pretty simple to figure out that this definition is quite open/not-restricted. 
</p>

### Ex.
<p>
  Any $a \in Z_{n}^{*}$ can be used to generate cyclic subgroups (this is the interesting thing about subgroups):

  $\langle a \rangle = \\{a, a^2, \dots, a^d = 1\\}$ for some $d$

  Any group is always a subgroup of itself (wow). $\\{1\\}$ is always a subgroup of any group (wow). 
</p>

## Lagrange's Theorem
<p>
  Let $H$ be a subgroup of $Z_{n}^{*}$ of size $m$. Then $m|\phi(n)$.
</p>

### Proof
<p>
  If $n$ is a non-prime number, then the former proof (generators) shows clearly that   
</p>
