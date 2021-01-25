import math
number=int(input("Enter the number"))
primes=[]
for i in range(2,number+1):
    primes.append(i)
i=2
while(i<=int(math.sqrt(number))):
    if i in primes:
        for j in range(2*i,number+1,i):
            if j in primes:
                primes.remove(j)
    i=i+1
print(primes)
