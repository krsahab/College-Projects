def findGCD(a, b):
    if(b == 0):
        return a;
    return findGCD(b, a%b)

def findCoefficients(a, b):
    if(a%b == 1):
        return 1, -(a//b)
    x, y = findCoefficients(b, a%b)
    u = y
    v = x - y*(a//b)
    return u, v

def inverse(a, b):
    if (findGCD(a, b) == 1):
        x, y = findCoefficients(a, b)
        print("Value of x is {} and value of y is {}".format(x, y))
    else:
        print ("{} and {} are not co - prime".format(a, b))

inverse(2613, -2171)
#Output: 2613 and -2171 are not co - prime