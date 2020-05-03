"""
https://maspypy.com/segment-tree-%e3%81%ae%e3%81%8a%e5%8b%89%e5%bc%b71
https://judge.yosupo.jp/submission/7795

構築は1-indexed
クエリは0-indexedを想定
初期値 
    - [n,2n)まで入れる。
    - i(i<n)においては、2*iと2*i+1の演算結果
更新 iにx
    - i+nにxを代入
    - i==0になるまで
        - i//=2
        - iは2*iと2*i+1の演算結果
区間取得 [l,r)
    - l+n, r+n
    - 左側の区間
        - 区間の右側(l%2==1)にいると、値を更新
        - 区間の左側だと、もう１段上に演算を委ねる事ができる
    - 右側の区間
        - 開区間に注意
        - 区間の左側(r%2==0)だと値を更新
        - 区間の右側だと、もう１段上
    - 左右のインデックスの差が1になるまでやる

"""
import sys
input = sys.stdin.readline
class segmented_tree:
    X_unit = 1 << 30
    X_f = lambda self, a, b: min(a,b)
    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (2*N)
        
    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x 
        # 後ろから入れていく
        for i in range(self.N-1, 0, -1):
            self.X[i] = self.X_f(self.X[i<<1], self.X[i<<1|1])

    # 1点更新
    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i<<1],self.X[i<<1|1])
    
    # 区間取得
    def fold(self, l, r):
        l += self.N
        r += self.N
        vl = self.X_unit
        vr = self.X_unit
        # 外から決めていく
        while l < r:
            # print(l,r)
            if l & 1:
                vl = self.X_f(vl, self.X[l])
                l += 1
            if r & 1:
                r -= 1
                vr = self.X_f(vr, self.X[r])
            l >>= 1
            r >>= 1
        return self.X_f(vl,vr)

if __name__ == "__main__":
    n, q = map(int, input().split())
    As = list(map(int, input().split()))
    st = segmented_tree(n)
    st.build(As)
    x = []
    for _ in range(q):
        l,r = map(int, input().split())
        ans = st.fold(l,r)
        x.append(ans) 
    print("\n".join(map(str,x)))

