import tqdm
from math import sqrt
def isprime(n): 
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(sqrt(n))+1, 2): 
        if n % x == 0:
            return False
    return True

def factors(l):
    n = int(l)
    for x in tqdm.tqdm(range(1,int(sqrt(n))+1)):
        if n%x == 0 and n%(n//x)==0 and isprime(x) == True and isprime(n//x) == True:
            return [x, n//x]

print(factors("407756900493095869"))