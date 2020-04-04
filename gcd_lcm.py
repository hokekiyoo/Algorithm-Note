"""
最大公約数と最小公倍数
最大公約数 GCD : ユークリッドの互除法を用いる。
最小公倍数 LCM(m,n) = m * n // GCD(m,n)
"""

def gcd(n, m):
    # 最大公約数
    a = max(n,m)
    b = min(n,m)
    while b:
        a, b = b, a % b
    return a

def lcm(n, m):
    # 最小公倍数
    a = max(n,m)
    b = min(n,m)
    while b:
        a, b = b, a % b
    return (n*m//a)

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(gcd(n,m))
    print(lcm(n,m))