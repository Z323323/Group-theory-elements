# Group theory elements

## (Cyclic) Subgroups, generators and multiplicative groups

<p>
  Here I want to make a slight modification to the normal definitions of subgroups in the group theory, since the definition already assumes what we want to prove here.<br>
  We define a subgroup of $Z_{n}^{*}$ as a non-empty subset $H$ of $Z_{n}^{*}$ such that all $e \in H$ are delimited by $e$ and by the production of $1$ by $e^{o} \mod n, 0 \lt o \lt n \in N$, i.e. the whole subgroup $H$ is:

  $\langle e \rangle = \\{e, e^{2}, e^{3}, \dots, e^{o} = 1\\}$

  I called the $degree$ ' $o$ ' because $o$ defines the $order$ of the subgroup, i.e. the number of its elements. Also $\langle e \rangle$ is a convention to indicate that $e$ 'generates' the whole (sub)group, indeed all the elements which generate the same set/group/subgroup are called $generators$ for that set/group/subgroup.<br>
  Now, another clarification is necessary. Sometimes when papers refer to $Z_{n}^{*}$, they refer to a group of this kind: $\\{1, 2, 3, \dots, n - 1\\}$ but without all the numbers which are not coprime with $n$. From another article which I'm still writing:
<strong>

  $3 \times z_{187 coprime} \mod (3 \times 187)$

  From this example we can easily imagine the left part as series of $3$ elements added, and the right part too. This means that since $z_{187 coprime}$ and $187$ are coprimes, their modulo will never 'produce' $0$, and this means that any result produced (which will be $0 < z < 187$) will be multiplied by $3$. This is why having a term which is not coprime with the modulo will never 'produce' $1$ as remainder, but only multiples of that term, and this is why the Euler's Theorem holds only for $a$ and $n$ coprimes and also why every non-coprime $z$ with $0 < z < n$ can't have a multiplicative modular inverse.<br>
  <br>
  [ This reasoning works in general proving this fact ].<br>
</strong>

 Now, placing this reasoning into this context, having non-coprimes in $Z_{n}^{*}$ has a direct effect in the subgroups we just discussed about. Since the modulo operation does not produce $1$ (but only multiples of the co-factor(s) of $e$ and $n$, or 0) we could not care about those subsets since they don't match our definition of subgroup, hence we could delete them from the reasoning. Now it's really important to understand that this is not always the case, indeed if we always reason this way $Z_{n}^{\ast}$ would become $Z_{\phi(n)}^{\ast}$. Before going over, if we follow the previous reasoning, we can notice that for ex. $Z_{3}^{\ast}$ and $Z_{\phi(4)}^{\ast}$ behave in the same way, since $2$ is the only generator of of $Z_{3}^{\ast}$, and it's cyclic (still haven't talked about cyclicness, it means generators always generate the same subgroup towards $\infty$) of order $2$, and $3$ is the only generator of $Z_{\phi(4)}^{\ast}$ and it's cyclic of order $2$. Now that this clarification has been made, I want you to take it and put it aside. For the moment, when I refer to $Z_{n}^{\ast}$, I don't refer to $Z_{\phi(n)}^{\ast}$, and when I do I write it as I did. <br>
 Now having made this important clarification we can safely assume that the number of subgroups is always $\phi(n)$, i.e. all generators which are coprime with $n$. Now yet another clarification: some papers refer to ' generators of $Z_{n}^{\ast}$ '; this has to do with some magic and the CRT, i.e. it's completely fine to have more than $1$ generator for the same set, but here the reasoning is quite more magical and complex, while it's not for $Z_{p}^{\ast}$ with $p$ prime.<br>
 It's possible to generate the whole $Z_{n}^{\ast}$ set using co-factors of $Z_{n}^{\ast}$ (as long as they are coprime) and applying the CRT. For ex. $Z_{561}^{\ast} (561 = 3 \times 11 \times 17)$ is generable using (generators of) these (sub?)groups: $Z_{3}^{\ast} \times Z_{11}^{\ast} \times Z_{17}^{\ast}$ which in turn don't have coprimes since $3, 11, 17$ are prime numbers. Hence we can consider the whole set of generators of these groups as the generators of $Z_{n}^{\ast}$ (the whole one).
 Now you can jump into a black hole in the next section, or jump to the next one which is our standard path among theorems, your choice.
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

## Lagrange's Theorem

<p>
  This theorem is probably the most important because allows to prove the cyclicness of subgroups (and note that I tried many different ways to prove cyclicness without success). I wrote the definition of subgroups as I did because this theorem is vital in order to prove the cyclicness of subgroups of $Z_{n}^{*}$. Also note that as already mentioned, this theorem don't need to refer to $Z_{n}^{*}$ as $Z_{\phi(n)}^{*}$, since we are talking about subgroups, and the definition I wrote is exactly architected to avoid this assumption (we are not talking about generators, but subgroups).<br>
<br>
  Let $H$ be a subgroup of $Z_{n}^{*}$ of size $m$. Then $m|\phi(n)$.
</p>

### Proof

<p>
  
  If $H = Z_{n}^{\ast}$ then $m = \phi(n)$. This is a consequence of everything said in the former sections.<br>
  Otherwise, let $H = \\{z_{1}, \dots, z_{m}\\}$. Let $a$ be some element $a \in Z_{n}^{\ast}$ not in $H$ and consider the set $Ha = \\{z_{1}a, \dots, z_{m}a \\}$. Every element of this new set must be **distinct** since 

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

  Now, let's say that there are still some elements left in $Z_{n}^{\ast}$. Iterating the previous procedure/reasoning for $H, Ha, Hb$ where 

  $Hb = \\{z_{1}b, \dots, z_{m}b \\}$

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

  and by the Lagrange's Theorem, let $m$ be the order of any subgroup of $Z_{n}^{*}$, then:

  $m|\phi(n)$

  proves the cyclicness of the subgroups towards $\infty$, since any subgroup must be generated by $G$ which is coprime with $n$.
</p>

## Generators theorem for Z_{p}^{*}

<p>
  Let $Z_{p}^{*}$ be a multiplicative group with $p$ prime, then the number of generators of $Z_{p}^{*}$ is $\phi(p - 1)$.<br>
  <br>
  As I already mentioned in the second-black-hole-section the number of generators of $Z_{n}^{*}$ is $\phi(n)$, but I'm not delving it for the moment, since everything I wrote in that section.
</p>

### Proof of generators theorem for Z_{p}^{*}

<p>
From the former proofs, we know that since every $q$ which divides $\phi(p) = p - 1$ is not a generator (since they form subgroups of order \phi(m)and not the whole $Z_{p}^{\ast})$ then it must be that all the coprimes are generators, since all elements of $Z_{p}^{\ast}$ 'produce' $1$ at $x^{p - 1} \mod p$ by Fermat. This is enough actually to state that the number of generators are $\phi(p - 1)$ for $Z_{p}^{\ast}$ and $\phi(n)$ for $Z_{n}^{\ast}$, but if you want to follow the calculation:

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


  

  
</p>
