"""
ベルマンフォードアルゴリズム
単一始点最短路
負の辺があっても使える。 O(VE)
辺が多いと E = O(V^2)くらいになりかねんのか
負の閉路があっても使える

参考(実装) : https://juppy.hatenablog.com/entry/2018/10/30/最短経路関連_python_競技プログラミング
参考(負のループ) : 
"""

INF = 10 ** 18
def bellmanFord(n, edges, s):
    """
    input
        n : 頂点の数
        edges : (始点, 終点, コスト)のリスト
        s : 探索の始点
        g : 探索の終点
    output
        sから各点への最短距離
    """    
    d = [INF] * n
    d[s] = 0
    # アップデートが終わるまで繰り返す
    # 負閉路がなければwhileは高々|V|-1回しか通らない
    # 無向グラフを想定
    cnt = 0
    while True:
        update = False
        for a, b, c in edges:
            if d[a] != INF and d[b] > d[a] + c:
                d[b] = d[a] + c
                update = True
        if not update:
            break
        cnt += 1
        # 負閉路の存在をチェック
        if cnt == n:
            print("Negative loop is founded")
            break
    return d

if __name__ == "__main__":
    """
    sample
    7 10
    1 2 2
    1 3 5
    2 3 4
    3 4 2
    2 4 6
    2 5 10
    4 6 1
    5 6 3
    5 7 5
    6 7 9
    """
    N, W = map(int, input().split())
    edges = []
    for _ in range(W):
        a,b,c = map(int, input().split())
        # 1-indexの場合
        a -= 1
        b -= 1
        # 有向グラフ
        edges.append((a, b, c))
        edges.append((b, a, c))
    # bellmanford
    for i in range(N):
        ans = bellmanFord(N,edges,i)
        print(ans)