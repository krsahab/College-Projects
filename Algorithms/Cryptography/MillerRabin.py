def findModulo(a, b, c):
    #0^b = 0
    if a==0:
        return 0
    #a^0 = 1 (if c!=1)
    if b==0:
        if c==1:
            return 0
        return 1
    temp = 0
    #If c is even
    if b%2 == 0:
        temp = findModulo(a, b/2, c)%c
        temp = (temp*temp)%c
    #If c is odd
    else:
        temp = a%c
        temp = (temp*(findModulo(a, b-1, c)%c))%c
    #Handle -ve a
    return (temp+c)%c

def findPowerTerms(x):
    s = 0
    while x%2 == 0:
        s+=1
        x = x/2
    return s, x

#Miller-Rabin Primality Test
def isMillerRabinPrime(n):
    if n<2:
        return False
    if n == 2 or n == 3:
        return True
    s, d = findPowerTerms(n-1)
    a = 2 # 2 is co-prime to all ramaining numbers
    if findModulo(a, d, n) == 1:
        return True
    for i in range(s):
        if findModulo(a, (2**i)*d, n) == n-1: #-1(mod n) is equal to n-1
            return True
    return False

#True Primality Test
def isTruePrime(x):
    if x<=1:
        return False
    if x<=3:
        return True
    if x%2 == 0 or x%3 ==0:
        return False
    i = 5
    while(i*i <= n) : 
        if n%i == 0 or n%(i + 2) == 0: 
            return False
        i = i + 6
    return True

#strong pseudo primes base 2 up to 10^5
for n in range(1,100000): 
    if isMillerRabinPrime(n) and not isTruePrime(n): 
        print(n , end=", ");

#Output: 2047, 3277, 4033, 4681, 8321, 15841, 29341, 42799, 49141, 52633, 65281, 74665, 80581, 85489, 88357, 90751, 