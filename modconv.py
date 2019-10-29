from math import factorial

"""
nCr = n!/(n-r)!(r)!
x^(p-1) = 1 (modp)

http://drken1215.hatenablog.com/entry/2018/06/08/210000

1 <= k <= n <= 10**7
pは素数(p>n)
"""

def modconb(n,k,mod):
    # テーブルを作る
    fac = [0]*(n+1)
    finv = [0]*(n+1)
    inv = [0]*(n+1)  

    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,n+1):
        fac[i] = fac[i-1]*i % mod
        inv[i] = mod - inv[mod%i] * (mod//i) % mod
        finv[i] = finv[i-1] * inv[i] %mod
    # 計算
    if n<k: return 0
    if n<0 or k<0: return 0
    return(fac[n]*(finv[k]*finv[n-k]%mod)%mod)
    

    

if __name__ == "__main__":
    a,b = map(int, input().split())
    mod = 10**9 + 7
    print(modconb(a,b,mod))

