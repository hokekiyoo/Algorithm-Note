"""
二部探索
参考 : https://qiita.com/hamko/items/794a92c456164dcc04ad
普通に配列内での場所を探す場合
下記で必ず狙った値(なければ右側)が求まる
A = [1,3,5,7,9]
from bisect import bisect_right
bisect_right(A,4)

大小関係だけじゃなく、ある特定条件でOK, NGの判定を出したいときは
f(x)に条件式を書く(trueになったらうれしい条件)。
r,lの幅を縮めていって、
l=false,r=trueになるところまで続ける
"""


A = [1,3,5,7,9]
q = int(input())

def f(x):
    """
    判定の条件式を書く
    等号あるなしで、False/Trueの協会が変わる
    等号を書いておくと、Aの配列とイコールだった時もTrueとなるので、そのままrが答えになる
    等号ありがbisect_leftと同じイメージ

    等号がない場合は、A > qは満たさないので、rは1大きな値を返す
    """
    return A[x] >= q


def  binarySearch(l,r):
    while r - l > 1:
        mid = (l+r)//2
        if f(mid):
            r = mid
        else:
            l = mid
    return r


if __name__ == '__main__':
    from bisect import bisect_right
    from bisect import bisect_left
    ind_l = bisect_left(A,q)
    ind_r = bisect_right(A,q)
    ind_orig = binarySearch(-1,len(A))
    print(ind_l, ind_r, ind_orig)