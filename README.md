# Group theory elements

## Multiplicative groups, (cyclic) subgroups and generators
<p>
  Here I want to make a slight modification to the normal definition of subgroups in the group theory. Becuse we are totally not interested in subgroups but cyclic subgroups. Since the definition of subgroup is useless, and the definition of cyclic subgroup already assumes what the Lagrange's Theorem proves (and we need to prove it), I'm going to set the definition of subgroups as the normal definition of cyclic subgroup but without the assumption of cyclicness.<br>
  
  We define a subgroup of $Z_{n}^{\ast}$ as a non-empty subset $H$ of $Z_{n}^{*}$ such that, taken any element $e \in Z_{n}^{\ast}$, all elements $z \in H$ are delimited by $e^{1}$ and the first $1$ 'produced' by $e^{o} \mod n, 0 \lt o \lt n \in N$, i.e the whole subgroup $H$ is:

  $\langle e \rangle = \\{e, e^{2}, e^{3}, \dots, e^{o} = 1\\}$

  I called the $degree$ ' $o$ ' because $o$ defines the $order$ of the subgroup, i.e. the number of its elements. Also $\langle e \rangle$ is a convention to indicate that $e$ 'generates' the whole (sub)group, indeed all the elements which generate the same set/group/subgroup are called $generators$ for that set/group/subgroup.<br>
  Now, another clarification is necessary. Sometimes when papers refer to $Z_{n}^{*}$, they refer to a group of this kind: $\\{1, 2, 3, \dots, n - 1\\}$ but without all the numbers which are not coprime with $n$. From another document which I was writing, imagine to have $(187 = 11 \times 17)$

  $3 \times z_{187 coprime} \mod (3 \times 187)$

  From this example we can easily imagine the left part as series of $3$ elements added, and the right part too. This means that since $z_{187 coprime}$ and $187$ are coprimes, their modulo will never 'produce' $0$, and this means that any result produced (which will be $0 < z < 187$) will be multiplied by $3$. This is why having a term which is not coprime with the modulo will never 'produce' $1$ as remainder, but only multiples of that term, and this is why the Euler's Theorem holds only for $a$ and $n$ coprimes and also why every non-coprime $z$ with $0 < z < n$ can't have a multiplicative modular inverse etc.
  
  [ This reasoning works in general proving this fact ].<br>

 Now, placing this reasoning into this context, having only coprimes of $n$ in $Z_{n}^{*}$ has sense, since the modulo operation for non-coprimes does not produce $1$ but only multiples of the co-factor(s) of $e$ and $n$, or 0. Hence we could not care about those subsets since they don't match our definition of subgroup. Now important imho to remember that  they exist, indeed if we always reason this way $Z_{n}^{\ast}$ would become $Z_{\phi(n)}^{\ast}$ (and that's why I decided to use this convention).<br>
 Now having made this important clarification we can safely assume that the number of subgroups is always $\phi(n)$, i.e. all generators (of the subgroups) which are coprime with $n$. Also, for everything I just said, the set mapped by all the subgroups' sets (joint) will be $Z_{\phi(n)}^{\ast}$, hence non-coprimes of $n$ will never appear in the subgroups. This is a direct consequence of what I said previously but it's quite intuitive at this point; if we remove $3$ from the above example (left part), and consider $z_{187 coprime}$ as both coprime with $3$ and $187$ then is clear that if we consider $z_{561 coprime} (> 3 \times 187 = 561)$, since it's not a multiple of $3$ nor of $187$, after the removal operated by the modulo, we will end up having a number $< 3 \times 187$ which is both coprime with $3$ and $187$. The same reasoning goes for powers of such number.
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

## Proof of cyclicness of subgroups (and uniqueness of each element)

<p>
  Let $a$ be a generator for a subgroup of $Z_{n}^{\ast}$, we know that in order to have

  $az \equiv 1 \mod n$

  $z$ is either a multiplicative inverse of $a$ or, by Lagrange Theorem, let $o$ be the order of the subgroup, then

  $z = a^{(o | \phi(n)) - 1}$

  Since the definition of subgroups I wrote implies $a$ to only be multiplied by itself, the first hypothesis is excluded and

  $az = aa^{(o | \phi(n)) - 1} = a^{o | \phi(n)} \equiv 1 \mod n$

  for any $a$ which is coprime with $n$.

  This proof is particularly important because it proves that every element of any subgroup of $Z_{n}^{\ast}$ will be different before $a^{o + 1}$ because in order to have a repetition we should necessarily have

  $aa^{o} = a^{o + 1} \mod n$

  for an $a$ repetition, or
  
  $a^2a^{o} = a^{o + 2} \mod n$

  for an $a^2$ repetition and so on.

  This proves the fact each element is different before $a^{o + 1}$ and also that each element $a^{exp}$ will be repeated towards infinity at the $k(o) + exp$-th multiplication.

  Now, if we start reasoning deeply about the potential repetitions of elements, we can understand that the uniqueness proof was already implied even before Lagrange's Theorem, because the definition of subgroup itself implies the elements of them being delimited by the last element which is $1$, and we can get a repetition only right after we get a $1$.
  
</p>

## Generators theorem
### Introduction

<p>
  Let $Z_{n}^{*}$ for $n$ non-prime. In order to be fully generated $Z_{n}^{\ast}$ should have order $o = n - 1$. By Lagrange's Theorem, the greatest order for a subgroup is $\phi(n)$. Now

  $\phi(n) < n - 1$

  for any $n$ which is non-prime.

  Hence $Z_{n}^{*}$ for $n$ non-prime can't have generators.<br>

  Now consider $Z_{\phi(n)}^{\ast}$ as the subgroup of $Z_{n}^{\ast}$ of order $\phi(n)$ and let $o(Z_{\phi(n)}^{\ast})$ be the function which calculates the order of a subgroup; $Z_{\phi(n)}^{\ast}$ can have generators because
  
  $o(subgroups(Z_{n}^{\ast})) \leq \phi(n)$

  indeed $Z_{\phi(n)}^{\ast}$ is itself a subgroup of $Z_{n}^{\ast}$ and therefore if it exists it necessarily have a generator (you'll find out that even $Z_{\phi(n)}^{\ast}$ could not exist).

  Now let $p$ be a prime, then $o(Z_{p}^{*}) = p - 1$, and $\phi(p) = p - 1$, then

  $o(subgroups(Z_{p}^{\ast})) \leq \phi(p)$

  hence $Z_{p}^{*}$ can have generators, without the need of any transformation.
</p>

### Clarifications about $Z_{\phi(2)}^{\ast}, Z_{\phi(4)}^{\ast}, Z_{\phi(8)}^{\ast} \dots$

<p>
  Refer to [https://crypto.stanford.edu/pbc/notes/numbertheory/gengen.html].

  Any group of the form $Z_{\phi(2^t)}^{*}$ where $t \geq 3$ will not have generators. This can be proved by induction but I'm not taking this challenge to the end (even though I verified the induction).
</p>

### Refinition of the reasoning before the proof

<p>
  Since the last three sections:<br>

  * $Z_{p}^{\ast}$ for $p$ prime always have generators (we are going to 'prove' it in the next section).
  * $Z_{n}^{\ast}$ for $n$ non-prime can't have generators (proved).
  * $Z_{\phi(n)}^{\ast}$ for $n$ non-prime can have generators (we are going to 'prove' it in the next section).
  * $Z_{\phi(n)}^{\ast}$ for $n = 2^t, t \geq 3$ can't have generators (it's provable by induction), therefore keep in mind that the next section won't apply for $n = 2^t, t \geq 3$ and also the cases like $Z_{\phi(12)}^{\ast} \dots$, which will be delved into the last section of this article.

</p>

### Proof of generators theorem

<p>
   
</p>

### $Z_{8}^{\ast}$ and $Z_{9}^{\ast}$ using Zn.py
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

  Initially I would say that one of the worst things to understand is the first binomial expansion. There $kp$ in the binomial disappears, I guess that it's because we know that the remainder $kp$ in the right part is produced directly by the $kp$ part of the binomial, hence we can discard that part and keep $g^p$ to further analyze $k$. The rest is just an outstanding construction to show that if we take a generator of $Z_{p}^{*}$ and generalize the formula with $kp$ (which is another non-intuitive-smart move) we can use it to expand the binomial with $kp$ and show that in the $\mod p$ case, the part $kp$ of the binomial disappears (trivial), while in the $\mod p^2$ it doesn't. After another couple smart moves we can show that the only case where $g + kp \mod p^2$ doesn't generate $Z_{\phi(p^2)}^{\ast}$ [with $g \in Z_{p}^{\ast}$] is the one where $g + kp$ order is $p - 1$. In such case we can even find the number which follows this case, that is, which is not a generator.<br>

  Honestly, I guess we are far away from planet Earth here, let's proceed over the galaxy then.<br>

From the first theorem of the aforementioned section, we can see that any generator we find in $Z_{p}^{*}$ can be reused in $Z_{p^2}^{\ast}$, and not only that, we can even add $kp$ to our generators, to spot $(p - 1) * generators$ on $Z_{p^2}^{\ast}$, i.e. every generator of $Z_{p^2}^{\ast}$, since:

$\phi(\phi(p^2)) = \phi(p(p - 1)) = \phi(p)\phi(p - 1) = (p - 1)\phi(\phi(p))$

All this keeping an eye to the exceptional case. Let's make an example.<br>

$generators(Z_{49}^{\ast}) = \phi(\phi(49)) = \phi(7)\phi(6) = 6 \times 2 = 12$

We proceed taking $\\{3, 5\\}$ which are generators of $Z_{7}^{\ast}$. Now we could start calculating every $3 + k7 \mod 49$ and $5 + k7 \mod 49$, but before doing that, let's remove our special cases (since we are considering $2$ generators we will have $2$ special cases).<br>
We know the magic formula is 

$\displaystyle k = \frac{g^p - g}{p} \mod p$

then

$\displaystyle k_1 = \frac{3^7 - 3}{7} \mod 7 = 4$<br>
$\displaystyle k_2 = \frac{5^7 - 5}{7} \mod 7 = 2$

substituting in the formula $(g + kp \mod p^2)$

$3 + 4 \times 7 \mod 49 = 31$<br>
$5 + 2 \times 7 \mod 49 = 19$

Now, let's fire off my Zn.py using of course 49. Let's start calculating every $3 + k7 \mod 49$ and $5 + k7 \mod 49$. You will find out that every number is a generator but $31$ and $19$.

After flying around using the Zn.py spaceship we can get back to planet Earth, and observe that this theorem (the one at the link) basically proves that the generators of $Z_{p}^{*}$ are generators of $Z_{p^2}^{\ast}$ too, and that we can use them to build every generator of $Z_{p^2}^{\ast}$.

### Extending the reasoning for $Z_{\phi(p^k)}^{*}, k \geq 2$

<p>

Now, let's try to expand the reasoning to $Z_{p^3}^{\ast}$ noting that it should hold for every power, because

$\phi(\phi(p^3)) = \phi(p(p(p - 1))) = \phi(p)\phi(p)\phi(p - 1) = (p - 1)(p - 1)\phi(\phi(p))$<br>
$\phi(\phi(p^4)) = \phi(p(p(p(p - 1)))) = \phi(p)\phi(p)\phi(p)\phi(p - 1) = (p - 1)(p - 1)(p - 1)\phi(\phi(p))$

and so on.<br>

Using the same intuitions of Ben (this is for my mental safety), let $t = p(p(p - 1))$ be the order of $g + kp$ in $Z_{p^3}^{\ast}$, then

$(g + kp)^t = g^t = 1 (\mod p)$

always generates $Z_{p}^{\ast}$ simply because we have chosen $g$ as a generator of $Z_{p}^{*}$, and because $p - 1|t$. Expanding the reasoning to $Z_{p^2}^{\ast}$ we get the exact same structure we saw earlier, because the order $t$ either divides $p(p(p - 1))$, or $p(p - 1)$, or $p - 1$. Since the first two cases both generate $Z_{p^2}^{\ast}$, we end up considering the same case above, hence we can safely proceed. Now expanding to $Z_{p^3}^{\ast}$ we will have two cases where $g + kp$ doesn't generate $Z_{p^3}^{\ast}$, which are $p - 1$ and $p(p - 1)$, since the third generates $Z_{p^3}^{\ast}$. Thus

1. $(g + kp)^{p} = g + kp (\mod p^3)$

and

2. $(g + kp)^{p(p - 1) + 1} = g + kp (\mod p^3)$

$(g + kp)^{p} = g + kp (\mod p^3)$<br>
$g^{p} - g = kp (\mod p^3)$<br>
$\displaystyle k_1 = \frac{g^{p} - g}{p} (\mod p^2)$

$(g + kp)^{p(p - 1) + 1} = g + kp (\mod p^3)$<br>
$g^{p(p - 1) + 1} - g = kp (\mod p^3)$<br>
$\displaystyle k_2 = \frac{g^{p(p - 1) + 1} - g}{p} (\mod p^2)$

Let's deploy another example, if it works we can state that the generators of powers of a prime which are $\gt 1$ can be constructed using the generators of the same $prime^1$. It's not the same for spotting fake-generators by the way, we are going to see that we will need the preceding power generators in order to spot every single one of them.

#### Ex

Using the first formula we derived [i.e. using $\{2\}$] to build $Z_{\phi(27)}^{*}$, we get

$\displaystyle k_1 = \frac{2^{3} - 2}{3} (\mod 9) = 2$

and substituting:

$2 + 2 \times 3 = 8 \mod 27 = 8$

which is not a generator indeed.

$\displaystyle k_2 = \frac{2^{3(3 - 1) + 1} - 2}{3} (\mod 9) = 8$

$2 + 8 \times 3 = 26 \mod 27 = 26$

which also is not a generator.

Now a fast check enables us to see that there's still $1$ non-generator which is not spotted. Using $5$, which is a generator of $Z_{9}^{\ast}$ [but not of $Z_{3}^{\ast}$]:

$\displaystyle k_3 = \frac{5^3 - 5}{3} (\mod 9) = 4$

$5 + 4 \times 3 = 17 \mod 27 = 17$

which is our last fake-generator.
Now, what happens if we consider the second case using $5$ as generator?

$\displaystyle k_4 = \frac{5^{3(3 - 1) + 1} - 5}{3} (\mod 9) = 8$

$5 + 8 \times 3 = 29 \mod 27 = 2$

which is not a fake gen (it's the first generator), then why is this result wrong? The reason is (not) simple; basically $5$ is a generator of $Z_{9}^{\ast}$; this means that it generates $Z_{9}^{\ast}$ at

$(g + kp^2)^{p(p - 1) + 1} = g + kp^2 (\mod p^2)$<br>

Thus the right calculation for $k$ would be

$(g + kp^2)^{p(p - 1) + 1} = g + kp^2 (\mod p^3)$<br>
$g^{p(p - 1) + 1} - g = kp^2 (\mod p^3)$<br>
$\displaystyle k_4 = \frac{g^{p(p - 1) + 1} - g}{p^2} (\mod p)$<br>
$->$<br>
$\displaystyle k_4 = \frac{5^{3(3 - 1) + 1} - 5}{3^2} (\mod 3)$<br>
$\displaystyle k_4 = 1$<br>
$5 + 1 \times 3 = 8 \mod 27 = 8$

which is correct although we already found it. I know this is kinda messy. This whole reasoning proves that in order to find every fake-generator we will need to keep into consideration every 

$g + kp \mod p^q$

and derive every $k$ following this section's reasoning.

It's really messy but in general we won't need all of these calculations I guess, so we can safely proceed.  

</p> 

### Using the CRT to provide useful insights about powers of $2$

<p>
  Following [https://crypto.stanford.edu/pbc/notes/numbertheory/gengen.html].<br>
  Let $\phi(n) = 2^{k}q$, using the CRT is clear that if $k \gt 3, Z_{\phi(2^{k}q)}^{\ast}$ won't have generators. Now, let $k = 2$, we have 

  $lcm(\phi(4q)) \gt lcm(\phi(4)\phi(q))$

  thus for any $\phi(n) = 2^{k}p_{1}^{k_1}\dots$ if $k \geq 2$, $Z_{\phi(n)}^{*}$ won't have generators. This is easily verifiable looking at $Z_{\phi(12)}^{\ast}, Z_{\phi(20)}^{\ast}, \dots$

  $\phi(12) = \phi(2^2)\phi(3)$<br>
  $\phi(20) = \phi(2^2)\phi(5)$

  But this doesn't still prove why $Z_{\phi(15)}^{\ast}$

  $\phi(15) = \phi(3)\phi(5) = 8 = 2^3$<br>

  doesn't have generators. As a general rule of thumb I guess that the $2^3$ rule could work, but I'm not sure at all. Every time $\phi(n) = 2^k, k \geq 3$ where $n$ is not prime, and has at least two factors's $\phi$ which produce such power could not have generators, I'm not sure at all by the way.
  
</p>
