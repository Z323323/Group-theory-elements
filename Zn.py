import sys

def factorize(n):
	factors = []
	c = 0
	exp = 0
	i = 2
	while i <= n:
		while n%i == 0:
			n/=i
			exp+=1
		if exp > 0:
			factors.append([i, exp])	
			exp=0
		i+=1
	return factors
	
def phiExpansion(factors):
	phis = []
	z = 1
	for factor in factors:
		z *= (factor[0]**factor[1] - factor[0]**(factor[1]-1))
		phis.append(z)
		z = 1
	return phis

def synthPhi(phisFactors):
	synthPhi = 1
	for phis in phisFactors:
		synthPhi *= phis
	return synthPhi
	
	
Zn = int(input("Enter integer number to see every multiplicative subgroup and its order:\n"))
factors = factorize(Zn)

phis = phiExpansion(factors)
ϕ = synthPhi(phis)

ϕϕf = factorize(ϕ)
ϕϕs = phiExpansion(ϕϕf)
ϕϕ = synthPhi(ϕϕs)

print("\nPrinting results using Zn as modulo and stopping at ϕ(n)...")

for j in range(1, Zn+2):
	print("\n", j, "->[", end = " ")
	for i in range(1, ϕ+1):
		print(j**i % Zn, end = " ")
	print("]")
	
print("\nPrinting results using Zn+1 as modulo, i.e. if you set n = 78, this calc. Zp, p = 79...")
	
for j in range(1, Zn+2):
	print("\n", j, "->[", end = " ")
	for i in range(1, Zn+1):
		print(j**i % (Zn+1), end = " ")
	print("]")
	
print("Factors:", factors)
print("Every co-factor Phi:", phis)
print("Multiplied co-factors phis:", ϕ)
print("Phi factors:", ϕϕf)
print("Every Phi's co-factors Phi:", ϕϕs)
print("Multiplied Phi's co-factors phis:", ϕϕ)
print("Resume: ϕ(n) = ", ϕ, ", ϕ(ϕ(n)) = ", ϕϕ)

# zμλn

