"""
dijkstra法
コストが正のときはこっちが大抵早い
heapをうまく使う

参考 : https://juppy.hatenablog.com/entry/2019/02/18/蟻本_python_プライオリティキュー%28heapq%29を用いたプリム法
"""
import heapq
INF = 10 ** 18
def dijkstra(n, edges, s):
    """
    input
        n : 頂点数
        edges : リスト(始点, 終点, コスト)
        s : 始点
    output
        d : 始点からの最短距離
    """
    d = [INF] * n
    used = [False] * n
    d[s] = 0
    used[s] = True
    edgelist = []
    # 初期のやつ
    for v, c in edges[s]:
        # print("v{},c{}".format(v,c))
        # コストを前にしてpushしておく(そこから最小値を取り出すので)
        heapq.heappush(edgelist, (c, v))
    # 空になるまで
    while len(edgelist):
        # コスト最小値を取り出す
        c_min, v_min = heapq.heappop(edgelist)
        # そのエッジがすでに確定していたら終わり
        if used[v_min]:
            continue
        # 確定していなければ、そこから派生するエッジをコスト付与して与える
        d[v_min] = c_min
        used[v_min] = True
        for v, c in edges[v_min]:
            if not used[v]:
                heapq.heappush(edgelist, (c+c_min, v))
    return d

def dijkstra2(n, edges, s, X):
    """
    ダイクストラ2
    ヒープに入れる中身を
    (c, v)とせず、1次元にしようぜ。という話
    v < Xの元では、c*X+vがcだけで大小が決まる
    c // X : コスト
    c % X :  頂点

    input
        n : 頂点数
        edges : リスト(始点, 終点, コスト)
        s : 始点
        X : 上乗せ分
    output
        d : 始点からの最短距離
    """
    d = [INF] * n
    used = [False] * n
    d[s] = 0
    used[s] = True
    edgelist = []
    # 初期のやつ
    for v, c in edges[s]:
        # コストを前にしてpushしておく(そこから最小値を取り出すので)
        heapq.heappush(edgelist, c*X+v)
    # 空になるまで
    while len(edgelist):
        # コスト最小値を取り出す
        X_min = heapq.heappop(edgelist)
        # そのエッジがすでに確定していたら終わり
        c_min = X_min//X
        v_min = X_min%X
        if used[v_min]:
            continue
        # 確定していなければ、そこから派生するエッジをコスト付与して与える
        d[v_min] = c_min
        used[v_min] = True
        for v, c in edges[v_min]:
            if not used[v]:
                heapq.heappush(edgelist, (c+c_min)*X+v)
    return d

if __name__ == "__main__":
    """
    入力
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
    edges = [[] for i in range(N)]
    for i in range(W):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        # 無向グラフ
        edges[a].append([b,c])
        edges[b].append([a,c])
    print(edges)
    for i in range(N):
        ans = dijkstra(N, edges, i)
        ans2 = dijkstra2(N,edges,i,10**5)
        print(i)
        print(*ans)
        print(*ans2)


