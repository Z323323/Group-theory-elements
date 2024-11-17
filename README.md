# Group theory elements

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
 Now having made this important clarification we can safely assume that the number of subgroups is always $\phi(n)$, i.e. all generators (of the subgroups) which are coprime with $n$. Also, for everything I just said, the set mapped by all the subgroups will be $Z_{\phi(n)}^{\ast}$, hence non-coprimes of $n$ will never appear in the subgroups. This is a direct consequence of the text in bold; if we remove $3$ from the above example (left part), $z_{187 coprime}$ will be both coprime with $3$ and $187$. Now if we imagine $z_{187 coprime} > 3 \times 187$ we can represent it as series of $3$ elements. It's clear that since it's not a multiple of $3$, after the removal operated by the modulo, we would end up having a number $< 3 \times 187$ which is coprime with both $3$ and $187$. The same reasoning goes for powers of such number.
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
  Papers normally refer to $Ha, Hb, \dots H_{\phi(n)}$ as the left cosets. This proof proves the importance of such concept besides the theorem, since as I already mentioned, this theorem allows to prove the cyclicness (next section), which believe me, it would be one hell of a ride to prove without this theorem.
  
</p>

## Proof of cyclicness of subgroups

<p>
  By the corollary of Euler's Theorem, for any $a$ which is coprime with $n$

  $a^{k(\phi(n))} \equiv 1 \mod n$

  and by the Lagrange's Theorem, let $o$ be the order of any subgroup of $Z_{n}^{*}$, then:

  $o|\phi(n)$

  proves the cyclicness of the subgroups towards $\infty$, since any subgroup must be generated by a generator which is coprime with $n$.
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

### Clarifications about $Z_{4}^{\ast}, Z_{8}^{\ast} \dots$

<p>
  All multiplicative groups like $Z_{4}^{\ast}, Z_{8}^{\ast} \dots$ have particular properties. If we employ the previous structure to any of those, obtaining $Z_{\phi(4)}^{\ast}, Z_{\phi(8)}^{\ast} \dots$ we should in turn obtain subgroups of order which is at max $\phi(4), \phi(8) \dots$ (otherwise we wouldn't have generators), which in turn since $\phi(n)$ calculates the coprimes of $n$ and since $n$ is a power of $2$, we get $2, 4 \dots$. Now, this means that every time we consider multiplicative groups defined on powers of $2$ which we indicate as $2^{S}$, we should get a max order of subgroups which is $\phi(2^{S}) = 2^{S - 1}$. However this doesn't happen. The reason is a strange property of odd numbers which always produce
  
  $\displaystyle odd^{\phi(\phi(2^{S}))} = odd^{2^{S - 2}} = n * 2 + 1$ for $n$ unknown,

  i.e.

  $\displaystyle odd^{2^{S - 2}} \equiv 1 \mod 2^{S}$ 

  or

  $\displaystyle odd^{\phi(\phi(2^{S}))} \equiv 1 \mod 2^{S}$ 

  or

  $\displaystyle odd^{\phi(2^{S - 1})} \equiv 1 \mod 2^{S}$

  which is somehow more similar to the Euler's Theorem. To conclude: when we have $Z_{4}^{\ast}, Z_{8}^{\ast} \dots$ we always? (it should be proved) end up having the order of subgroups which is $\phi(n)$ but halved, hence all these multiplicative groups can't have generators. I'm quite sure we will face this formula in the next article about quadratic residues.
</p>

### Refinition of the reasoning before the proof

<p>
  Since the last two sections:<br>

  * $Z_{p}^{\ast}$ for $p$ prime always have generators (we are going to prove it in the next section).
  * $Z_{n}^{\ast}$ for $n$ non-prime can't have generators (proved).
  * $Z_{\phi(n)}^{\ast}$ for $n$ non-prime can have generators (we are going to prove it in the next section).
  * $Z_{\phi(n)}^{\ast}$ for $n = 2^{S}$ can't have generators (we need further research).

  Note that I'm actively studying while writing, hence there could be some other rules. In such case I'll update this document, but for the moment this is  complex enough so let's go over.
</p>

### Proof of generators theorem

<p>
  Every element of the starting set $Z_{\phi(n)}^{\ast}$ represents a generator for its subgroup. Note that writing multiplicative groups using this form can be more intuitive, because we immediately spot that the number of subgroups is $\phi(n)$, and this works for both primes and non-primes. The $2^{S}$ exception only regards generators, but the number of subgroups of $Z_{2^{S}}^{\ast}$ is still $\phi(2^{S})$. The generators of $Z_{\phi(n)}^{\ast}$ are the subgroups which order divides $\phi(n)$ and produce $1$; all the others will be non-generators, hence the solution is the number of subgroups which satisfy this equation:

  $\displaystyle \frac{\phi(n)}{o(subgroup)} = 1$
  
  The immediate conclusion could be that there only exists $1$ generator for $Z_{\phi(n)}^{\ast}$ but it's not correct. This is not intuitive at all.
  It turns out that we need to use a tactic similar to the 'left cosets' concept, to find the number of non-generators first:

  $\displaystyle \frac{\phi(n)}{o(subgroup)} \neq 1$

  Since the Lagrange's Theorem (see how important it is) we know that every subgroup's order divides $\phi(n)$, hence the number of subgroups which satisfy the above inequality are the ones which divide it more than once. Now since every number (except for primes) can be represented as powers of primes multiplied:

  $n = p_{1}^{k_1}p_{2}^{k_2} \dots p_{?}^{k_?}$

  the number of non-generators will exactly be

  $nonGenerators = p_{1}^{k_1 - 1}p_{2}^{k_2 - 1} \dots p_{?}^{k_? - 1}$

  Yes, this one is hard to figure out, and it's not even over. To get the former think about this: you have $p_{1}^{k_1}p_{2}^{k_2} \dots p_{?}^{k_?}$ numbers, which generate only numbers (the order of the subgroups) which are multiples of $p_{1}^{k_1}p_{2}^{k_2} \dots p_{?}^{k_?}$, from all these, how many divide such number more than once?<br>
$->$<br>
"How many divisors of $p_{1}^{k_1}p_{2}^{k_2} \dots p_{?}^{k_?}$ divide it more than once?" is the same as saying how many multiples of $x$ such that $x$ do not reach $p_{1}^{k_1}p_{2}^{k_2} \dots p_{?}^{k_?}$ are there? Since $x$ must divide $\phi(n)$ and $\phi(n) = p_{1}^{k_1}p_{2}^{k_2} \dots p_{?}^{k_?}$, the multiples we are talking about are the multiples of $p_{?}^{k_?}p_{1}p_{2} \dots p_{?}$, and there are $p_{1}^{k_1 - 1}p_{2}^{k_2 - 1} \dots p_{?}^{k_? - 1}$ of those.
Hence the number of non generators is $p_{1}^{k_1 - 1}p_{2}^{k_2 - 1} \dots p_{?}^{k_? - 1}$ and the number of generators must be:

$p_{1}^{k_1}p_{2}^{k_2} \dots p_{?}^{k_?} - p_{1}^{k_1 - 1}p_{2}^{k_2 - 1} \dots p_{?}^{k_? - 1} = \phi(\phi(n))$ 

This is one hell of mess, look the below proof.

$\displaystyle x = \frac{p_{1}^{k_1}p_{2}^{k_2} \dots p_{?}^{k_?}}{p_{1}p_{2} \dots p_{?}}$
</p>

## Generators theorem for $Z_{p}^{*}$

<p>
  Let $Z_{p}^{*}$ be a multiplicative group with $p$ prime, then the number of generators of $Z_{p}^{*}$ is $\phi(p - 1)$.<br>
  <br>
  As I already mentioned in the second-black-hole-section the number of generators of $Z_{n}^{*}$ is $\phi(n)$, but I'm not delving it for the moment, since everything I wrote in that section.
</p>

### Proof of generators theorem for $Z_{p}^{*}$

<p>
From the former proofs, we know that since every $z$ which divides $\phi(p) = p - 1$ is not a generator [ since they form subgroups of order $o < \phi(p)$ by the corollary, hence not the whole $Z_{p}^{\ast})$ ], then it must be that all the coprimes of $p - 1$ are generators, because by the Euler's Theorem they produce $G^{\phi(p)} \equiv 1 \mod p$ and by the reasoning made in the first section . This is enough actually to state that the number of generators are $\phi(p - 1)$ for $Z_{p}^{\ast}$ and $\phi(n)$ for $Z_{n}^{\ast}$, but if you want to follow the calculation:

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

<p>

Since the 'cancellation law' [ https://github.com/xyzhyn/Fermat-Little-Theorem-proof ]:

$(x)(x) \equiv (x)(1) \mod p$<br>
-><br>
$x \equiv 1 \mod p$

is not possible if $x < p - 1$ and $x \neq 1$.

</p>

## $Z_{561}^{\ast}, Z_{8}^{\ast}, Z_{9}^{\ast}$

<p>
  We know that the number of $generators$ is the number of coprimes of $Z_{561}^{\ast}$. If we do a fast math we get $\phi(561) = 192$. Now, from the previous reasoning, the generators for this group were the generators of $Z_{3}^{\ast} \times Z_{11}^{\ast} \times Z_{17}^{\ast}$ so how is it possible that this number is so high? The generators for any group $Z_{p}^{\ast}$ with $p$ prime are $\phi(p - 1)$ (we are going to prove this fact later), hence by the multiplicativity of the Totient function we will just need to calc. a quick multiplication to find that $192$ is correct. Now how does this match with the CRT? If we take any of those $generators$, every combination (the multiplication of them) will produce a virtual result mapped on $Z_{561}^{\ast}$, even though $Z_{561}^{\ast}$ itself do not have any generator (yep I know). Now let's take the previous fact about any $Z_{p}^{\ast}$ having $\phi(p - 1)$ generators, and see what happens for $\phi(16)$. $16 = 2^4$ then we can't use the CRT again, but we know that it has $8$ generators, let's find them. Since $Z_{16}^{\ast}$ is quite high, let's reduce it and do the same with $Z_{8}^{\ast}$, since the reasoning is the same [ $4$ generators ].

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

Sum them and you get $4$, and once you did it, take this reasoning and throw it in the garbage :'D. Do you remember the reasoning made in the previous section when I told you that some papers refer to groups like $Z_{8}^{*}$ as  $Z_{\phi(8)}^{\ast}$? Here you are why is (very likely) that. If we consider $Z_{\phi(8)}^{\ast}$ instead of $Z_{8}^{\ast}$ then the prompt result showed above is the correct representation of the generators, otherwise it's not.
As you can see there's a lot of magic involved with prime numbers, cryptography and group theory.
Let's try with $Z_{9}^{\ast}$.

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

Now you can transfer the same reasoning to $Z_{561}^{\ast}$... ops, $Z_{\phi(561)}^{\ast}$ to understand why it has $\phi(561)$ generators. The really strange thing is that once we have primes co-factors we can take those and generate everything through the CRT. With $Z_{561}^{\ast}$ it was easy. But what would happen if we had a $2^{3}$ like co-factors initially? I mean, how could we exploit the CRT? My man, the only restriction imposed by the CRT is that we have coprimes co-factor, hence we would not care about generators.<br>
Now, why are we actually getting mad with generators? For two purposes mainly: 1. to understand how theorems hold, and to understand how multiplicative groups work, and 2. because we need to understand how they work to set up unbreakable crypto systems. Here the purpose is mainly the first point, but let's widen the surface. We need to set up a crypto system (very vague I know, imagine ECDSA in Ethereum), if our group is made up of non-prime co-factors the set produced by generators (if we can actually use them to generate anything) is clearly reduced, this could be a problem (indeed elliptic curves solves this). But for the moment, let's proceed with our real goal, i.e. the previous 'first point'.<br>
This reasoning about real-world scenarios is a set-up to say that generators are a huge variable in a crypto system, so we don't just 'look at the CRT'. Now, let's conclude this madness section. It's clear that even if mathematicians call them generators, in the $Z_{561}^{\ast}, Z_{8}^{\ast}, Z_{9}^{\ast}$ cases they clearly don't generate the whole set, hence they shouldn't be called generators, at least in the real world, but note that mathematicians are **never** wrong (indeed, they have 100% a way to explain that mathematically this concept works). If we take a prime number $p$, you will see that $Z_{p}^{*}$ contains $\phi(p - 1)$ **real** generators. When I say _real_ I mean that they actually generate the whole $Z_{p}^{\ast}$ group. In every other case (non-primes) this behaviour do not subsist. And it's not over. In the $Z_{9}^{\ast}$ example above:

>2 ->[ 2 4 8 7 5 1 ]
>
>5 ->[ 5 7 8 4 2 1 ]

Effectively generate $Z_{\phi(9)}^{\ast}$, but not $Z_{9}^{\ast}$, while the other $4$ so-called generators do not (if taken singularly). If we take the $Z_{8}^{\ast}$ example, not even one of those so-called generators do generate $Z_{\phi(8)}^{\ast}$ (if taken singularly), hence we would end up not having a singular real generator. Note that these are my actual conclusions at this point of the research, but I could be wrong. Now let's continue with our theorems. But before continuing, this is $Z_{7}^{*}$:

>1 ->[ 1 1 1 1 1 1 ]
>
>2 ->[ 2 4 1 2 4 1 ]
>
>3 ->[ 3 2 6 4 5 1 ]
>
>4 ->[ 4 2 1 4 2 1 ]
>
>5 ->[ 5 4 6 2 3 1 ]
>
>6 ->[ 6 1 6 1 6 1 ]

Indeed if you do $\phi(7 - 1) = \phi(6)$, we know that only $\\{1, 5\\}$ are coprimes with $6$, hence there must be only $2$ generators. Indeed $\\{3, 5\\}$ are **real** generators of the set, and everything works fine (with primes).

Is anyone still here? If you are, congrats, let's proceed through the dark forest.
</p>
