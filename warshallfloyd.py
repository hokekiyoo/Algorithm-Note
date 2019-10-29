"""
全点対最短距離 : O(N^3)
想定入力(1-index)

scipyだともっと早いっぽい
参考 : https://juppy.hatenablog.com/entry/2019/06/04/scipyのFloyd-WarshallとDijkstraのすすめ_Python_競技プログラミング_Atcoder_1#Floyd-WarshallとDijkstraってなんだっけ

"""

def warshall_floyd(d):
    """
    input
        d : 初期全点対距離
    output
        d : 最適化後全点対距離
    """
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    return d



if __name__ == "__main__":
        
    """
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

    想定出力
    [0, 4, 6, 10, 7, 15, 2]
    [4, 0, 2, 6, 3, 11, 5]
    [6, 2, 0, 4, 1, 9, 7]
    [10, 6, 4, 0, 3, 5, 11]
    [7, 3, 1, 3, 0, 8, 8]
    [15, 11, 9, 5, 8, 0, 16]
    [2, 5, 7, 11, 8, 16, 0]
    """

    """
    d(各辺へのコスト)の作り方
    """
    INF = 10**18
    N,W = map(int, input().split())

    d = [[INF for i in range(N)] for j in range(N)]
    # 確保できるなら確保した方が早い
    edges = []
    for i in range(W):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edges.append((a, b, c))

    for a,b,c in edges:
        # 始点、終点、コスト
        # 1-indexのとき
        a -= 1
        b -= 1
        d[a][b] = c
        d[b][a] = c #無向グラフのときはこれも
    for i in range(N):
        d[i][i] = 0

    d_optimized = warshall_floyd(d)
    for d in d_optimized:
        print(d)