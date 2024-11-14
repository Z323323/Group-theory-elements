# Group theory elements

## (Cyclic) Subgroups, generators and multiplicative groups

<p>
  Here I want to make a slight modification to the normal definitions of subgroups in the group theory, since the definition already assumes what we want to prove here.<br>
  We define a subgroup of $Z_{n}^{*}$ as a non-empty subset $H$ of $Z_{n}^{*}$ such that all $e \in H$ are delimited by $e$ and by the production of $1$ by $e^{o} \mod n, 0 \lt o \lt n \in N$, i.e. the whole subgroup $H$ is:

  $\langle e \rangle = \\{e, e^{2}, e^{3}, \dots, e^{o} = 1\\}$ [ all these operations are always made $(\mod n)$ ]

  I called the $degree$ ' $o$ ' because $o$ defines the $order$ of the subgroup, i.e. the number of its elements. Also $\langle e \rangle$ is a convention to indicate that $e$ 'generates' the whole (sub)group, indeed all the elements which generate the same set/group/subgroup are called $generators$ for that set/group/subgroup.<br>
  Now, another clarification is necessary. Sometimes when papers refer to $Z_{n}^{*}$, they refer to a group of this kind: $\\{1, 2, 3, \dots, n - 1\\}$ but without all the numbers which are not coprime with $n$. From another article which I'm still writing:
<strong>

  $3 \times z_{187 coprime} \mod (3 \times 187)$

  From this example we can easily imagine the left part as series of $3$ elements added, and the right part too. This means that since $z_{187 coprime}$ and $187$ are coprimes, their modulo will never 'produce' $0$, and this means that any result produced (which will be $0 < z < 187$) will be multiplied by $3$. This is why having a term which is not coprime with the modulo will never 'produce' $1$ as remainder, but only multiples of that term, and this is why the Euler's Theorem holds only for $a$ and $n$ coprimes and also why every non-coprime $z$ with $0 < z < n$ can't have a multiplicative modular inverse.<br>
  <br>
  [ This reasoning works in general proving this fact ].<br>
</strong>

 Now, placing this reasoning into this context, having non-coprimes in $Z_{n}^{*}$ has a direct effect in the subgroups we just discussed about. Since the modulo operation does not produce $1$ (but only multiples of the co-factor(s) of $e$ and $n$, or 0) we could not care about those subsets since they don't match our definition of subgroup, hence we could delete them from the reasoning. Now it's really important to understand that this is not always the case, indeed if we always reason this way $Z_{n}^{\ast}$ would become $Z_{\phi(n)}^{\ast}$. Before going over, if we follow the previous reasoning, we can notice that for ex. $Z_{3}^{\ast}$ and $Z_{\phi(4)}^{\ast}$ behave in the same way, since $2$ is the only generator of of $Z_{3}^{\ast}$, and it's cyclic (still haven't talked about cyclicness, it means generators always generate the same subgroup towards $\infty$) of order $2$, and $3$ is the only generator of $Z_{\phi(4)}^{\ast}$ and it's cyclic of order $2$. Now that this clarification has been made, I want you to take it and put it aside. For the moment, when I refer to $Z_{n}^{\ast}$, I don't refer to $Z_{\phi(n)}^{\ast}$, and when I do I write it as I did. <br>
 Now having made this important clarification we can safely assume that the number of subgroups is always $\phi(n)$, i.e. all generators which are coprime with $n$. Now yet another clarification: some papers refer to ' generators of $Z_{n}^{\ast}$ '; this has to do with the CRT.<br>
 It's possible to generate the whole $Z_{n}^{\ast}$ set using co-factors of $Z_{n}^{\ast}$ (as long as they are coprime) and applying the CRT. For ex. $Z_{561}^{\ast} (561 = 3 \times 11 \times 17)$ is generable using (generators of) these (sub?)groups: $Z_{3}^{\ast} \times Z_{11}^{\ast} \times Z_{17}^{\ast}$ which in turn don't have coprimes since $3, 11, 17$ are prime numbers. Hence we can consider the whole set of generators of these groups as the generators of $Z_{n}^{\ast}$ (the whole one).
 Now let's dig into the essence of cryptography, prepare for madness :').
</p>

### $Z_{561}^{\ast}$

<p>
  We know that the number of $generators$ is the number of coprimes of $Z_{561}^{\ast}$. If we do a fast math we get $\phi(561) = 192$. Now, from the previous reasoning, the generators for this group were the generators of $Z_{3}^{\ast} \times Z_{11}^{\ast} \times Z_{17}^{\ast}$ so how is it possible that this number is so high? The generators for any group $Z_{p}^{\ast}$ with $p$ prime are $\phi(p - 1)$ (we are going to prove this fact later), hence by the multiplicativity of the Totient function we will just need to calc. a quick multiplication to find that $192$ is correct. Now how does this match with the CRT? If we take any of those $generators$, every combination (the multiplication of them) will produce a virtual result mapped on $Z_{561}^{\ast}$, even though $Z_{561}^{\ast}$ itself do not have any generator (yep I know). Now let's take the previous fact about any $Z_{p}^{\ast}$ having $\phi(p - 1)$ generators, and see what happens for $\phi(16)$. $16 = 2^4$ then we can't use the CRT again, but we know that it has $8$ generators, let's find them. Since $16$ is quite high, let's reduce it and do the same with $8$, since the reasoning is the same [ $4$ generators ].

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

So where the actual hell are our $4$ generators? As I told you, all of these are virtual results and somehow complex numbers are involved. But before completely going crazy, what happens if we follow the $ones$?

$\phi(1) = 1$<br>
$\phi(3) = \phi(3 - 1) = \phi(2 - 1) = 1$<br>
$\phi(5) = \phi(5 - 1) = \phi(4) [same reasoning]-> \phi(1) = 1 * \phi(3) = \phi(3 - 1) = \phi(2) = \phi(2 - 1) = 1$<br>
$\phi(7) = ? -> 1$<br>

Sum them and you get $4$, and once you did it, take this reasoning and throw it in the garbage :'D. Do you remember the reasoning made in the previous section when I told you that some papers refer to groups like $Z_{9}^{*}$ as  $Z_{\phi(9)}^{\ast}$? Here you are why is (very likely) that. If we consider $Z_{\phi(9)}^{\ast}$ instead of $Z_{9}^{\ast}$ then the prompt result showed above is the correct representation of the generators, otherwise it's not.
As you can see there's a lot of magic involved with prime numbers, cryptography and group theory.
Let's try with $9 = 3^2$, this time, instead of following the $ones$, why don't we just take our coprimes reasoning and say that there are $6$ generators, and they actually are the coprimes of $9$? :')
Now you can transfer the same reasoning to $Z_{561}^{\ast}$... ops, $Z_{\phi(561)}^{\ast}$ to understand why it has $\phi(561)$ generators. The good/really strange thing is that once we have primes co-factors we can take those and generate everything through the CRT. With $Z_{561}^{\ast}$ it was easy. But what would happen if we had a $2^{3}$ like co-factors initially? I mean, how could we exploit the CRT? My man, the only restriction imposed by the CRT is that we have coprimes co-factor, hence we don't give a fuck about generators. Also, if we take the coprimes of $8 = \\{1, 3, 5, 7\\}$ we can easily see that they are primes, hence we could use them with the CRT (throwing $1$ out of the window). Generators and the CRT are (as everything else in this field) really connected but separated entities. Nonetheless the CRT would use $\mod 8$ results to generate everything, and the madness continues...

Is anyone still here? If you are, congrats, let's proceed through the dark forest.
</p>

## Analysis of the Totient function for powers of primes

A deep understanding of the Totient function is required in order to really understand what the actual hell is happening. First: let's see how the Totient of the power of a prime divides that number.

$\displaystyle \frac{p^q}{\phi(p^{q})} = \frac{p^{q}}{p^{q} - p^{q - 1}} = \frac{p^{q}}{p^{q - 1}(p - 1)} = \frac{p}{p - 1}$

$\displaystyle \frac{\phi(p^{q})}{p^q} = \frac{p - 1}{p}$

And now look at this, this holds for any prime $p$:

$\displaystyle \frac{p}{\phi(p)} = \frac{p}{p - 1} = 1 + \frac{1}{p - 1}$

$\displaystyle \frac{\phi(p)}{p} = \frac{p - 1}{p} = 1 - \frac{1}{p}$

Which means that if we multiply the Totient function of a prime by the same prime we get $p - 1$.

Now we can state that if

$\displaystyle \frac{p^q}{\phi(p^{q})} = \frac{p}{p - 1}$

then

$\displaystyle \phi(p^{q})(\frac{p}{p - 1}) = p^{q}$

and also

$\displaystyle \phi(p^{q})2^{S}(\frac{p}{p - 1}) = p^{q}2^{S}$

and considering $p_{1}$ as prime where $p_{1} - 1 = p^{q}2^{S}$

$\displaystyle \phi(p^{q})2^{S}(\frac{p_{1}}{p_{1} - 1}) = \phi(p^{q})(\frac{p_{1}}{p^q})$ _ <---

Now if we consider $p_{1} - 1 = p^{q}2^{S}$ where $p_{1}$ is a prime number $\neq p$ and composed by $p$:

$\displaystyle p_{1} - 1 = \phi(p^{q}) 2^{S} (\frac{p_{1}}{p_{1} - 1})$

$\displaystyle p = \displaystyle \frac{\phi(p^{q})2^Sp_{1}}{p_{1} - 1} = \frac{\phi(p^{q})p_{1}}{p^{q}} = p^{q}2^{S} - 2^{S} + \phi(p^{q})$

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
