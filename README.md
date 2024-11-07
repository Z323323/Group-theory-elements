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

### Proof of generators theorem

<p>
[ https://crypto.stanford.edu/pbc/notes/numbertheory/gen.html ].<br>
Here I derived a similar while different proof.<br>
By Fermat:
  
$x^{p - 1} - 1 = 0 (\mod p)$

We know that this equation has $p - 1$ solutions (roots) $(\mod p)$. Let $q^{k}$ be a prime power dividing $p - 1$. We can then rewrite the equation as:

$x^{p - 1} - 1 = (x^{q^{k}} - 1)g(x) = 0 (\mod p)$

where $g(x)$ is a $p - 1 - q^{k}$ polynomial. From the former section we know that $(x^{q^{k}} - 1)$ has at most $q^{k}$ roots and $g(x)$ has at most $p - 1 - q^{k}$ roots, and since their product has $p - 1$ **different** roots, we see that there are exactly $q^{k}$ **distinct** solutions to $x^{q^{k}} - 1 = 0 (\mod p)$. This result is particularly important because we know how many roots (solutions) each $x^{?} \equiv 1 \mod p$ has, with certainty.<br>
Thus, to find the number of generators, we can state that since $x^{p - 1} - 1 = 0 (\mod p)$ has $p - 1$ different solutions, then $p - 1$ minus the solutions of $x^{p - 2} - 1 = 0 (\mod p)$ is the number of generators. This is because $x^{p - 2} - 1 = 0 (\mod p)$ [ $x^{p - 2} \equiv 1 \mod p$ ] solutions contain every $x^{z} - 1 = 0 (\mod p)$ solutions with $0 < z < p - 1$ (since the reasoning above about polynomials multiplication). Hence $x^{p - 2} - 1 = 0 (\mod p)$ contains $p - 2$ solutions and these solutions are all the numbers that produce $1 \mod p$ before being raised to $p - 1$. In oder words $x^{p - 2} - 1 = 0 (\mod p)$ maps all the solutions of $x^{z} - 1 = 0 (\mod p)$ with $0 < z < p - 1$ and all these solutions are the numbers which produce $1$ being raised to $z$ power; thus $x^{p - 2} - 1 = 0 (\mod p)$ solutions are the $nonGenerators$, and $p - 1 - nonGenerators$ are the number of $generators$.<br>
Now, the first thing to do is to obtain $x^{p - 2} = 0 \mod p$. We know that $p - 1 = 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$, thus to decrease this power/degree we need to divide by $x - 1$:

$\displaystyle \frac{(x - 1)^{2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}}}{x - 1}$

But this is either equal to:

$(x - 1)^{2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}}$ or $(x - 1)^{2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}}$ or $(x - 1)^{2^{S}q_{1}^{k_{?}}q_{2}^{k_{?} - 1} \dots q_{?}^{k_{?}}}$ or $(x - 1)^{2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?} - 1}}$

To understand this behaviour, you should mind that for ex. $5 \times 6$ is either $5$ sets of $6$ elements or $6$ sets of $5$ elements. Now, to get the number of $generators$, we will need to consider each one of the former solutions, thus:

$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
or<br>
$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?}}q_{2}^{k_{? - 1}} \dots q_{?}^{k_{?}}$<br>
or<br>
$2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}} - 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{? - 1}}$<br>

Now keep in mind that operating these subtractions we are actually considering $2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$, $n_{cofactors} - 1$ more times than we should (i.e. we should subtract all of $- 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$, etc. from $2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$ only $1$ time, not $n_{cofactors}$ times, but since this is required to solve this theorem, what we are effectively finding is the number of generators of $2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$, multiplied $n_{cofactors} - 1$ times). Now we need to get a sum of all these terms in order to find the $generators$, hence these: 

$- 2^{S - 1}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
$- 2^{S}q_{1}^{k_{?} - 1}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}$<br>
$- 2^{S}q_{1}^{k_{?}}q_{2}^{k_{? - 1}} \dots q_{?}^{k_{?}}$<br>
$- 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{? - 1}}$<br>

equal to

$(- 2^{S - 1} - q_{1}^{k_{?} - 1} - q_{2}^{k_{?} - 1} - \dots - q_{?}^{k_{?} - 1})(n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})$

and therefore these

$+ 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}$<br>
$+ 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}$<br>
$+ 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}$<br>
$+ 2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}}$<br>

equal

$(2^{S} + q_{1}^{k_{?}} + q_{2}^{k_{?}} + \dots + q_{?}^{k_{?}})(n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})$

Now we can finally operate the subtraction, noting that since all the negative terms have been encapsulated into that multiplication, now we will need to consider it an addition. Also you will need to remember and keep in mind the former reasoning about $(n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})$. Now we can finally proceed:

$generators(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})(n_{cofactors} - 1)  = (2^{S} + q_{1}^{k_{?}} + q_{2}^{k_{?}} + \dots + q_{?}^{k_{?}})(n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}}) + (- 2^{S - 1} - q_{1}^{k_{?} - 1} - q_{2}^{k_{?} - 1} - \dots - q_{?}^{k_{?} - 1})(n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})$

$(x \cdot a) + (x \cdot b) = xa + xb = x(a + b)$<br>
$->$<br>
$generators(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})(n_{cofactors} - 1) = (n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})(2^{S} + q_{1}^{k_{?}} + q_{2}^{k_{?}} + \dots + q_{?}^{k_{?}} - 2^{S - 1} - q_{1}^{k_{?} - 1} - q_{2}^{k_{?} - 1} - \dots - q_{?}^{k_{?} - 1})$

and since [ https://github.com/xyzhyn/Totient-extension-to-non-primes ]:

$generators(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})(n_{cofactors} - 1) = (n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})\phi(2^{S})\phi(q_{1}^{k_{?}})\phi(q_{2}^{k_{?}}) \dots \phi(q_{?}^{k_{?}})$

$generators(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})(n_{cofactors} - 1) = (n_{cofactors} - 1)(2^{S}q_{1}^{k_{?}}q_{2}^{k_{?}} \dots q_{?}^{k_{?}})\phi(p - 1)$

$generators = \phi(p - 1)$
</p>

#### Little extra found along the battles

Since the 'cancellation law' [ https://github.com/xyzhyn/Fermat-Little-Theorem-proof ]:

$(x)(x) \equiv (x)(1) \mod p$<br>
-><br>
$x \equiv 1 \mod p$

is not possible if $x < p$ and $x \neq 1$.
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
