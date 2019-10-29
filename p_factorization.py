"""
素因数分解
1. eratosthenesから割りまくる
"""


def getprime(n):
    if not isinstance(n, int):
        raise TypeError("Input int")
    if n < 2:
        raise ValueError("N >= 2")
    prime = []
    # 約数はsqrt(N)まで調べればOK
    data = [i+1 for i in range(1,n)]
    while True:
        p = data[0]
        if p >= int(n**0.5):
            return prime+data
        prime.append(p)
        # pで割り切れないものだけを残す
        data = [d for d in data if d%p != 0]

from collections import defaultdict
def factorization(n):
    factors = defaultdict(int)
    primes = getprime(int(n**0.5))
    for prime in primes:
        while n % prime == 0:
            factors[prime] += 1
            n //= prime
            # print(factors,n)
    if n != 1:
        factors[n] += 1
    return factors

if __name__ == "__main__":
    from datetime import datetime as dt
    # for i in range(2,7):
    print("input some numbers (<10^12)")
    N = int(input())
    st = dt.now()
    data = factorization(N)
    diff = dt.now()-st
    for k in data.keys():
        print("k^n k:{}   n:{}".format(k,data[k]))
    
    # print("10^{} : {}s".format(i,diff.total_seconds()))

    def gcd(n, m):
        # 最大公約数
        a = max(n,m)
        b = min(n,m)
        while b:
            a, b = b, a % b
        return a