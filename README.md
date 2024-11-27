# Group theory elements

I recommend the use of Zn.py to figure out things.

## Multiplicative groups, (cyclic) subgroups and generators
<p>
  Here I want to make a slight modification to the normal definition of subgroups in the group theory. Becuse we are totally not interested in subgroups but cyclic subgroups. Since the definition of subgroup is useless, and the definition of cyclic subgroup already assumes what the Lagrange's Theorem proves (and we need to prove it), I'm going to set the definition of subgroups as the normal definition of cyclic subgroup but without the assumption of cyclicness.<br>
  
  We define a subgroup of $Z_{n}^{\ast}$ as a non-empty subset $H$ of $Z_{n}^{*}$ such that, taken any element $e \in Z_{n}^{\ast}$, all elements $z \in H$ are delimited by $e^{1}$ and the first $1$ 'produced' by $e^{o} \mod n, 0 \lt o \lt n \in N$, i.e the whole subgroup $H$ is:

  $\langle e \rangle = \\{e, e^{2}, e^{3}, \dots, e^{o} = 1\\}$

  I called the $degree$ ' $o$ ' because $o$ defines the $order$ of the subgroup, i.e. the number of its elements. Also $\langle e \rangle$ is a convention to indicate that $e$ 'generates' the whole (sub)group, indeed all the elements which generate the same set/group/subgroup are called $generators$ for that set/group/subgroup.<br>
  Now, another clarification is necessary. Sometimes when papers refer to $Z_{n}^{*}$, they refer to a group of this kind: $\\{1, 2, 3, \dots, n - 1\\}$ but without all the numbers which are not coprime with $n$. From another article which I'm still writing:
<strong>

  $3 \times z_{187 coprime} \mod (3 \times 187)$

  From this example we can easily imagine the left part as series of $3$ elements added, and the right part too. This means that since $z_{187 coprime}$ and $187$ are coprimes, their modulo will never 'produce' $0$, and this means that any result produced (which will be $0 < z < 187$) will be multiplied by $3$. This is why having a term which is not coprime with the modulo will never 'produce' $1$ as remainder, but only multiples of that term, and this is why the Euler's Theorem holds only for $a$ and $n$ coprimes and also why every non-coprime $z$ with $0 < z < n$ can't have a multiplicative modular inverse.<br>
  <br>
  [ This reasoning works in general proving this fact ].<br>
</strong>

 Now, placing this reasoning into this context, having only coprimes of $n$ in $Z_{n}^{*}$ has sense, since the modulo operation for non-coprimes does not produce $1$ but only multiples of the co-factor(s) of $e$ and $n$, or 0. Hence we could not care about those subsets since they don't match our definition of subgroup. Now it's really important to understand that this is not always the case, indeed if we always reason this way $Z_{n}^{\ast}$ would become $Z_{\phi(n)}^{\ast}$.<br>
 Now having made this important clarification we can safely assume that the number of subgroups is always $\phi(n)$, i.e. all generators (of the subgroups) which are coprime with $n$. Also, for everything I just said, the set mapped by all the subgroups will be $Z_{\phi(n)}^{\ast}$, hence non-coprimes of $n$ will never appear in the subgroups. This is a direct consequence of the text in bold; if we remove $3$ from the above example (left part), $z_{187 coprime}$ will be both coprime with $3$ and $187$. Now if we imagine $z_{561 coprime} > 3 \times 187$ we can represent it as series of $3$ elements. It's clear that since it's not a multiple of $3$, after the removal operated by the modulo, we would end up having a number $< 3 \times 187$ which is coprime with both $3$ and $187$. The same reasoning goes for powers of such number.
</p>

## Lagrange's Theorem

<p>
I wrote the definition of subgroups as I did because this theorem is vital in order to prove the cyclicness of subgroups of $Z_{n}^{*}$ and the generators theorem. All these precautions have been made because there must not be any definition which already assumes what this theorem proves.<br>
<br>
  Let $H$ be a subgroup of $Z_{n}^{*}$ of order $o$. Then $o|\phi(n)$.
</p>

### Proof

<p>
  
  Let $H = \\{z_{1}, \dots, z_{o}\\}$. Let $a$ be some element which belongs to $Z_{\phi(n)}^{*}$ with $a \notin H$ and consider the set $Ha = \\{z_{1}a, \dots, z_{o}a \\}$. Every element of this new set must be **distinct** since 

  $z_{1}a \equiv z_{2}a \mod n$

  implies 
  
  $n | a(z_{1} - z_{2})$
  
  and since $n$ can't divide $a$ since $a$ is coprime with $n$ ($a$ is an element of a subgroup hence it must be coprime with $n$ since the definition of subgroups I wrote):
  
  $z_{1} \equiv z_{2} \mod n$

  but this can't be true since $z_{1}, z_{2} < n$ and $z_{1} \neq z_{2}$, hence $z_{1}a \neq z_{2}a$ proving they are **distinct** pairwise.<br>
  Also no element of $Ha$ lies in $H$, since it would imply

  $za \in H$<br>
  $->$<br>
  $za \equiv z \mod n$<br>
  $n | z(a - 1)$<br>
  $->$<br>
  $a \equiv 1 \mod n$

  Therefore $a$ should be equal to $1$, but this can't be, because $1 \in H$ by the definition of subgroup and $a \notin H$, hence no element of $Ha$ lies in $H$.
  This would mean that

  $\displaystyle |H| = \frac{\phi(n)}{2}$

  Otherwise if we didn't consider any $a$:

  $\displaystyle |H| = \phi(n)$

  which obviously divides $\phi(n)$.<br>
  Now, let's say that there is still some other element left in $Z_{\phi(n)}^{*}$. Iterating the previous procedure/reasoning with $a, b$ and $H, Ha, Hb$ where 

  $Hb = \\{z_{1}b, \dots, z_{o}b \\}$

  we would obtain

  $\displaystyle |H| = \frac{\phi(n)}{3}$

  and iterating up to $H, Ha, Hb, \dots H_{\phi(n)}$:

  $\displaystyle |H| = \frac{\phi(n)}{\phi(n)} = 1$

  which still divides $\phi(n)$ therefore proving the theorem.<br>
  <br>
  Papers normally refer to $Ha, Hb, \dots H_{\phi(n)}$ as the left cosets. This proof proves the importance of such concept besides the theorem, since as I already mentioned, this theorem allows to prove the cyclicness (next section), which believe me, it would be one hell of a ride to prove without this theorem. Also this theorem proves that any subgroup's element are **distinct** which is non-trivial at all. I could repeat myself but this theorem is simply too much powerful.
  
</p>

## Proof of cyclicness of subgroups

<p>
  Calling $o$ the order of any subgroup of $Z_{n}^{*}$, we have by Lagrange's Theorem 

  $\displaystyle o = \frac{\phi(n)}{d}$

  for some $d$ which divides $n$.
  
  By the corollary of Euler's Theorem, for any $a$ which is coprime with $n$

  $a^{k(\phi(n))} \equiv 1 \mod n$

  We can make a slight modification to the **rearrangement property** and state that $a^{k}$, $k \in Q$ where $Q$ is the set of rational numbers, is still coprime with $n$ since if $a$ is coprime with $n$; $\sqrt{a}, \sqrt[3]{a}, \sqrt[\frac{3}{2}]{a} \dots$ will be still coprime with $n$. Thus applying the **cancellation law** we would end up having:

  $\displaystyle a^{k(\phi(n))} \equiv 1 \mod n, k \in Q$

  Now, considering the order $o$ of any subgroup, this will fall into this corollary:

  $\displaystyle a^{k(\frac{\phi(n)}{d})} \equiv 1 \mod n$

  Now, considering 
  
  $\displaystyle k = \frac{1}{2}, \frac{1}{3}, \dots, \frac{1}{\frac{\phi(n)}{d}}, \dots \frac{2}{\frac{\phi(n)}{d}}, \dots$
  
  proves the cyclicness of the subgroups towards $\infty$.
  Now we can proceed to prove that every element is cyclic, not only the $1s$. By the corollary of the Euler's theorem:

  $a^{k(\phi(n)) + 1} \equiv a \mod n$

  We can proceed in the same way above to show that for any $a$ which is coprime with $n$ and $a \in Z_{o}^{*} \subset Z_{\phi(n)}^{\ast}$, $a$ 'produces' itself into the next cycle (of order $o$), towards $\infty$. This proves that any multiplicative group (following the papers definition) and subgroup (following mine) is cyclic towards $\infty$ in its entirety.
</p>

## Generators theorem
### Introduction

<p>
  $Z_{n}^{*}$ for any $n$, has order $n - 1$. By the Lagrange's Theorem, the greatest order for a subgroup is $\phi(n)$. Now:

  $\phi(n) < n - 1$

  for any $n$ which is non-prime.<br>

  Hence $Z_{n}^{*}$ for $n$ non-prime can't have generators.<br>

  Now we consider $Z_{n}^{*}$ as the subgroup of itself of order $\phi(n)$ and refer to it as $Z_{\phi(n)}^{\ast}$ (it must exist to safely set this hypotesis, but we will see later). Remember that the generator of such subgroup will necessary be a generator of $Z_{\phi(n)}^{\ast}$. I know this sound nosense, just accept that $Z_{\phi(n)}^{\ast}$ is exactly the same as the subgroup of $Z_{n}^{\ast}$ of order $\phi(n)$.
  Now, let $o(Z_{\phi(n)}^{\ast})$ be the function which calculates the order of a subgroup; $Z_{\phi(n)}^{\ast}$ can have generators because
  
  $o(subgroups(Z_{n}^{\ast})) \leq o(Z_{\phi(n)}^{\ast})$

  indeed the group itself is generated by a generator of a subgroup of $Z_{n}^{\ast}$.<br>

  Otherwise let $p$ be a prime, then $o(Z_{p}^{*}) = p - 1$, and $\phi(p) = p - 1$, then

  $o(subgroups(Z_{p}^{\ast})) \leq o(Z_{p}^{*})$

  hence $Z_{p}^{*}$ can have generators, without the need of any transformation.
</p>

### Clarifications about $Z_{\phi(2)}^{\ast}, Z_{\phi(4)}^{\ast}, Z_{\phi(8)}^{\ast} \dots$

<p>
  Refer to [https://crypto.stanford.edu/pbc/notes/numbertheory/gengen.html].

  Any group of the form $Z_{\phi(2^t)}^{*}$ where $t \geq 3$ will not have generators. This can be proved by induction but I'm not taking this challenge to the end (excuse me Ben).

  This whole reasoning should be extended for any $Z_{\phi(n)}^{*}$ where $\phi(n) = 2^t, t \geq 3$. For example

  $Z_{\phi(12)}^{*} \mapsto \phi(12) = \phi(3)\phi(2^2) = 2\ast\phi(2^2) = \phi(2^3)$<br>

  Anyways this last result is just an intuition and for the moment such behaviour is not proved.
</p>

### Refinition of the reasoning before the proof

<p>
  Since the last three sections:<br>

  * $Z_{p}^{\ast}$ for $p$ prime always have generators (we are going to 'prove' it in the next section).
  * $Z_{n}^{\ast}$ for $n$ non-prime can't have generators (proved).
  * $Z_{\phi(n)}^{\ast}$ for $n$ non-prime can have generators (we are going to 'prove' it in the next section).
  * $Z_{\phi(n)}^{\ast}$ for $n = 2^t$ can't have generators (it's provable by induction), therefore keep in mind that the next section applies just for $n \neq 2$ and also the cases like the one listed in the previous section, which will be delved into the last section of this article.

  Note that I'm actively studying while writing, hence there could be some other rules. In such case I'll update this document, but for the moment this is  complex enough so let's go over.
</p>

### Proof of generators theorem

<p>
  Consider

  $a^{\phi(n)} \equiv 1 \mod n$

  This congruence has $\phi(n)$ distinct solutions, and

  $a^{1} \equiv 1 \mod n$

  has $1$ solution which is $1$. Now consider

  $a^{2} \equiv 1 \mod n$

  This congruence by the CRT has $2 * nCofactors$ (distinct) solutions.
  Indeed all these solutions can't be generators since they 'produce' $1$ before $\phi(n)$. Iterating this reasoning for every degree which we know will 'produce' $1$ 
  before $\phi(n)$ will allow us to remove all the non-generators from $\phi(n)$ that is, finding the number of generators after a 'simple' difference with $\phi(n).<br>
  
  Now, $\phi(n)$, for any $n$, must be of the form

  $\phi(n) = p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}}$

  It's not possible to have a prime number as $\phi(n)$ because the calculation made to get it always expect the difference between a power of a prime number (or multiplication of them) minus the same power of degree $-1$, hence there 
  always is a prime multiplication involved (or a prime number minus $1$, which is never a prime except for $2$ and $3$, which are trivial cases).<br>

  We know by the **cyclicness** of subgroups and by Lagrange's Theorem that there will exist:

  $a^{k(p_{1})} \equiv 1 \mod n$<br>
  $b^{k(p_{2})} \equiv 1 \mod n$<br>
  $\dots^{\dots} \equiv 1 \mod n$<br>
  $z^{k(p_{?})} \equiv 1 \mod n$

  Thus all the multiples of $p_{1}, p_{2}, \dots, p_{?} \lt p^k_{1, 2, \dots}$ won't be solutions of our problem.<br>
  Let $m(p)$ be the function which represent every multiple of a number $< p^k$. We can say that for ex.

  $a^{m(p_{1})p_{2}^{k_{2}} \dots p_{?}^{k_{?}}} \equiv 1 \mod n$

  Since the multiples of any $p^{k}$ are $p^{k - 1}$, we can say that for each co-factor of $\phi(n)$ there will be $p^{k - 1}$ to remove. Now we could stop here already and state that this directly means that:
  
  $generators = p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}} - p_{1}^{k_{1} - 1}p_{2}^{k_{2} - 1} \dots p_{?}^{k_{?} - 1} = \phi(\phi(n))$

  But I derived a more intuitive solutions below.<br>
  
  Since all these $(p_{1}^{k_{1} - 1} / p_{2}^{k_{2} - 1} / \dots / p_{?}^{k_{?} - 1})$ will be multiplied by the others before reaching $\phi(n)$ (i.e. these 
  solutions must not reach $\phi(n)$ since we are only removing from $0 < n < \phi(n)$ interval):

  $p_{1}^{k_{1} - 1}p_{2}^{k_{2}} \dots p_{?}^{k_{?}}$

  numbers can't be our solution. And this is the same for all the other co-factors, thus:

  $p_{1}^{k_{1}}p_{2}^{k_{2} - 1} \dots p_{?}^{k_{?}}$<br>
  $\dots$<br>
  $p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?} - 1}$

All these are $nonGenerators$ calculated factor-by-factor, now to get the number of $generators$, we will need to consider each one of the former solutions, thus:<br>
[https://github.com/Z323323/Totient-extension-to-non-primes]<br>
$[(x \cdot a) - (x \cdot b) = x(a - b)]$

$p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}} - p_{1}^{k_{1} - 1}p_{2}^{k_{2}} \dots p_{?}^{k_{?}} = \phi(p_{1}^{k_{1}})p_{2}^{k_{2}} \dots p_{?}^{k_{?}}$<br>
or<br>
$p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}} - p_{1}^{k_{1}}p_{2}^{k_{2} - 1} \dots p_{?}^{k_{?}} = p_{1}^{k_{1}}\phi(p_{2}^{k_{2}}) \dots p_{?}^{k_{?}}$<br>
$\dots$<br>
or<br>
$p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}} - p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?} - 1} = p_{1}^{k_{1}}p_{2}^{k_{2}} \dots \phi(p_{?}^{k_{?}})$<br>

Now keep in mind that operating these subtractions we are actually considering $p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}}$, $n_{cofactors} - 1$ more times than we should (i.e. we should subtract all of $p_{1}^{k_{1} - 1}p_{2}^{k_{2}} \dots p_{?}^{k_{?}}$, etc. from $p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}}$ only $1$ time, not $n_{cofactors}$ times, but since this is required to solve this theorem, what we are effectively finding is the number of generators $+ p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}}$, multiplied $n_{cofactors} - 1$ times). Now we need to get a sum of all these terms in order to find the $generators$, hence these: 

$\phi(p_{1}^{k_{1}})p_{2}^{k_{2}} \dots p_{?}^{k_{?}}$<br>
$p_{1}^{k_{1}}\phi(p_{2}^{k_{2}}) \dots p_{?}^{k_{?}}$<br>
$\dots$<br>
$p_{1}^{k_{1}}p_{2}^{k_{2}} \dots \phi(p_{?}^{k_{?}})$<br>

equal

$\phi(p_{1}^{k_{1}})\phi(p_{2}^{k_{2}}) \dots \phi(p_{?}^{k_{?}}) + (n_{cofactors} - 1)(p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}})$

and finally

$generators + (p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}})(n_{cofactors} - 1)  = \phi(p_{1}^{k_{1}})\phi(p_{2}^{k_{2}}) \dots \phi(p_{?}^{k_{?}}) + (n_{cofactors} - 1)(p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}})$

$generators = \phi(\phi(n))$

And for $\phi(p)$ where $p$ is a prime number we would get [ since $\phi(p) = p - 1$ ]:

$generators = \phi(p - 1)$

Now

$nonGenerators = \phi(n) - \phi(\phi(n)) = p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}} - p_{1}^{k_{1}}p_{2}^{k_{2}} \dots p_{?}^{k_{?}} + p_{1}^{k_{1} - 1}p_{2}^{k_{2} - 1} \dots p_{?}^{k_{?} - 1} = p_{1}^{k_{1} - 1}p_{2}^{k_{2} - 1} \dots p_{?}^{k_{?} - 1}$<br>

It's really interesting how we can't imply basically anything (using this construction) about $n$; indeed we never care about $n$ when we talk about generators, since $Z_{n}^{*}$ can't have generators.
</p>

## Some prompts
>[2,988s][~/Scrivania]$ python3 Zn.py
>
>Enter integer number to see every multiplicative subgroup and its order:
>
>8
>
>Printing results using Zn as modulo and stopping at ϕ(n)...
>
>1 ->[ 1 1 1 1 ]
>
>2 ->[ 2 4 0 0 ]
>
>3 ->[ 3 1 3 1 ]
>
>4 ->[ 4 0 0 0 ]
>
>5 ->[ 5 1 5 1 ]
>
>6 ->[ 6 4 0 0 ]
>
>7 ->[ 7 1 7 1 ]

>[0,900s][~/Scrivania]$ python3 Zn.py
>
>Enter integer number to see every multiplicative subgroup and its order:
>
>9
>
>Printing results using Zn as modulo and stopping at ϕ(n)...
>
>1 ->[ 1 1 1 1 1 1 ]
>
>2 ->[ 2 4 8 7 5 1 ]
>
>3 ->[ 3 0 0 0 0 0 ]
>
>4 ->[ 4 7 1 4 7 1 ]
>
>5 ->[ 5 7 8 4 2 1 ]
>
>6 ->[ 6 0 0 0 0 0 ]
>
>7 ->[ 7 4 1 7 4 1 ]
>
>8 ->[ 8 1 8 1 8 1 ]
</p>

### Generators for $Z_{\phi(p^2)}^{*}$, "Squares of odd primes" section

<p>
  This section is part of [https://crypto.stanford.edu/pbc/notes/numbertheory/gengen.html].<br>

  Here I will try to collapse the results of proofs of the linked resource. Since those proofs are really complex, and I don't want to copy paste them, I'll just try to extrapolate the results, and provide some useful tips in order to better understand such theorems.

  Initially I would say that one of the worst things to understand is the first binomial expansion. There $kp$ in the binomial disappears, I guess that it's because we know that the remainder $kp$ in the right part is produced directly by the $kp$ part of the binomial, hence we can discard that part and keep $g^p$ to further analyze $k$. The rest is just an outstanding construction to show that if we take a generator of $Z_{p}^{*}$ and generalize the formula with $kp$ (which is another genius move) we can use it to expand the binomial with $kp$ and show that in the $\mod p$ case, the part $kp$ of the binomial disappears (trivial), while in the $\mod p^2$ it doesn't, and after another couple smart moves we can show that the only case where $g + kp \mod p^2$ doesn't generate the whole set [with $g \in Z_{p}^{\ast}$] is the one where $g + kp$ order is $p - 1$. In such case we can even find the number which follows this case, that is, which is not a generator.<br>

  Honestly, I guess we are far away from planet Earth here, let's proceed over this stupid galaxy.<br>

From the first theorem of the aforementioned section, we can see that any generator we find in $Z_{p}^{*}$ can be reused in $Z_{p^2}^{\ast}$, and not only that, we can even add $kp$ to our generators, to spot $(p - 1) * generators$ on $Z_{p^2}^{\ast}$, i.e. every generator of $Z_{p^2}^{\ast}$, since:

$\phi(\phi(p^2)) = \phi(p(p - 1)) = \phi(p)\phi(p - 1) = (p - 1)\phi(\phi(p))$

All this keeping an eye to the exceptional case. Let's make an example.<br>

$generators(Z_{49}^{\ast}) = \phi(\phi(49)) = \phi(7)\phi(6) = 6 \times 2 = 12$

We proceed taking $\\{3, 5\\}$ which are generators of $Z_{7}^{\ast}$. Now we could start calculating every $3 + k7 \mod 49$ and $5 + k7 \mod 49$, but before doing that, let's remove our special cases (since we are considering $2$ generators we will have $2$ special cases), and show the magic essence of math, and how smart are people (I can't believe it ahah).<br>
We know the magic formula is 

$\displaystyle k = \frac{g^p - g}{p} \mod p$

then

$\displaystyle k_1 = \frac{3^7 - 3}{7} \mod 7 = 4$<br>
$\displaystyle k_2 = \frac{5^7 - 5}{7} \mod 7 = 2$

substituting in the formula $(g + kp \mod p^2)$

$3 + 4 \times 7 \mod 49 = 31$<br>
$5 + 2 \times 7 \mod 49 = 19$

Now, let's fire off my Zn.py using of course 49. Let's start calculating every $3 + k7 \mod 49$ and $5 + k7 \mod 49$. You will find out that every number is a generator but $31$ and $19$.
 
</p> 

### Extending the reasoning for $Z_{\phi(p^k)}^{*}, k \geq 2$

<p>
  
</p>

### Using the CRT to expand the reasoning to every $n$, providing useful insights about powers of $2$

<p>
  
</p>
