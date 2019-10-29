"""
しゃくとり法
 区間の銭湯と末尾を交互に進めながら条件を満たす最小区間を求める方法
|5 1 3 5 10|7 4 9 2 8
 5|1 3 5 10|7 4 9 2 8
 5 1|3 5 10|7 4 9 2 8
 5 1 3|5 10|7 4 9 2 8
 5 1 3 5|10 7|4 9 2 8
 5 1 3 5 10|7 4 9|2 8
 5 1 3 5 10 7|4 9 2|8
 5 1 3 5 10 7 4|9 2 8|

長さnの数列a1,...,anと整数Sが与えられる。
"連続する"文字列のうちその総和がS以上となるもののうち
"最小"の長さを求めなさい。

しゃくとりの区間に"単調性"がある時がポイント

参考１https://qiita.com/drken/items/ecd1a472d3a0e7db8dced
「条件」を満たす区間 (連続する部分列) のうち、最小の長さを求める
「条件」を満たす区間 (連続する部分列) のうち、最大の長さを求める
「条件」を満たす区間 (連続する部分列) を数え上げる
"""
n = int(input())
S = int(input())
L = list(map(int, input().split()))

"""
10
15
5 1 3 5 10 7 4 9 2 8
"""
INF = 10**10
def solve():
    left = 0
    right = 0
    res = INF
    sum = 0
    for left in range(n):
        # leftを固定しながら、条件を満たす最大のrightをさがす
        while right < n and sum < S: #rightが進んだ時に条件を満たす
            # rightを1進めた時の処理
            sum += L[right]
            right += 1
        # left固定で条件を満たす最大のrightが得られている
        # right == nのときは注意
        # retの更新
        if sum >= S:
            res = min(res,right-left)
        # leftを更新する準備(この場合だと、sumから引いてやらないといけない)
        if right == left:
            right += 1
        else:
            sum -= L[left]
    print(res)

solve()
            


