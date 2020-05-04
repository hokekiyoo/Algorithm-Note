"""
Fenwick Tree (Binary Indexed Tree)
http://hos.ac/slides/20140319_bit.pdf

SegTreeの機能を限定。早いし簡単。
N個の変数v1,...,vnに対して
- vaに値wを加える
- aまでの和v1+v2+...+vaを求める
をlog(N)で行う
累積和だと updateがO(N)、部分和がO(1)

Note:ある数xの最も下位のビットは `x&-x`で取り出せる！
補数の関係上、桁上りの一歩手前
 x  = 00000000 00000000 00101110 01011000
 -x = 11111111 11111111 11010001 10101000

最下位bitから調整していって登っていく
すでに0の場合は更新しなくて良い

1-indexed
☑ https://judge.yosupo.jp/problem/point_add_range_sum
"""

class BIT:
    def __init__(self, n):
        """
        初期化
        Input:　
            n: 配列の大きさ
        """
        self.n = n
        self.bit = [0] * (n+10)

    def add(self, x, w):
        """
        更新クエリ(add)
        Input:
            x: インデックス
            w: 加える値
        Note:
            self.bitが更新される
        """        
        while x <= self.n:
            self.bit[x] += w
            x += x&-x
    
    def sum(self, x):
        """
        部分和算出クエリ
        Input:
            x: インデックス
        Return:
            [1,a]の部分和
        """
        cnt = 0
        while x > 0:
            cnt += self.bit[x]
            # 次の最下位桁はどこか
            x -= x&-x
        return cnt   
    
    def psum(self, a, b):
        """
        区間[a,b)(0-indexed)における和
        Input
            a,b: 半開区間
        Return
            [a,b)の和
        """
        return self.sum(b-1) - self.sum(a-1)
    
    def bisect(self, w):
        """
        二分探索クエリ
        (すべての要素が0以上のとき)
        Input:
            w: 値
        Return:
            w以上となる最小のindex
        """    
        if w <= 0: return 0
        x = 0 #index
        k = 1
        while k < self.n:
            k *= 2

        while k > 0:
            if x + k <= self.n and self.bit[x+k] < w:
                # 右に移動
                w -= self.bit[x+k]
                x += k
            k //= 2 
        return x + 1
        
    

if __name__ == "__main__":
    As = [3,1,4,1,5,9,2]
    # q1 = [2,5]
    
    bit = BIT(len(As))
    # 更新
    for i,a in enumerate(As):
        bit.add(i+1,a)
    # [a,b)の和
    print("ORIG")
    print("[2,6)の部分和",bit.psum(2,6))
    # 和が10を超える最初のk
    print("二部探索",bit.bisect(10))
    """
    区間の更新
    """
    # update
    bit.add(x=2, w=3)
    print("ADD 3 at index 2") 
    print("[2,6)の部分和",bit.psum(2,6))
    # 和が10を超える最初のk
    print("二部探索",bit.bisect(10))
    
        
    