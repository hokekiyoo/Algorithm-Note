"""
二部マッチング
図解 : http://topcoder.g.hatena.ne.jp/agw/20120716/1342405575
詳説 : https://ikatakos.com/pot/programming_algorithm/graph_theory/bipartite_matching

増大路を探すやつ

- すでにマッチングMがある
- ペアのいないA側のaiを始点
- ペアのいないB側のbjを終点
- 増大路上の辺を入れ替える
と、辺の数が1増えた新しいマッチングが作れる

辿っていって増大路(左右共に新しい未マッチング頂点があるか)

"""
import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

def dfs(v, visited):
    """
    :param v: x側のマッチングしていない頂点
    :param visited: すでに探索した点かどうか判断
    :return: 増大路が見つかればTrue
    """
    next_vs = edges[v]
    print(v,next_vs)
    for next_v in next_vs:
        if visited[next_v]:
            continue
        visited[next_v] = True
        # 増大路の交代を行っている
        # 新しい終点を発見するとTrueを返す
        # すでにmatchingされているならば、そこからさかのぼって増大路があるか検索
        if matched[next_v] == -1 or dfs(matched[next_v],visited):
            matched[next_v] = v
            return True
    return False

if __name__ == '__main__':
    """
    入力
    Nx,Ny : x,yの頂点の数
    M : 辺の数
    a,b 辺となりうるペア
    x->yの有向辺だけで良い。(yからのxはmatchedに保存)
    # matched : yとマッチングされたxの頂点
    """
    Nx, Ny, M = map(int, input().split())
    matched = [-1] * Ny
    edges = defaultdict(list) 
    for i in range(M):
        a,b = map(int, input().split())
        edges[a].append(b)   
    ans = 0
    # 各頂点ごとに、マッチングできるか決めていく。
    # 左は常に新しい点となるので、
    # そこから辺を辿って新しい右の点に到達すればOK。しなければマッチングしない。
    for i in range(Nx):
        ans += dfs(i,[False for i in range(Ny)])
    print(ans)


    """
    ex1.
    5 4 10
    0 0 
    0 1
    1 1
    1 2
    2 1
    2 3
    3 0
    3 2
    4 1
    4 3

    ex2. 
    4 4 7
    0 0
    0 1
    1 0
    1 2
    2 1
    2 3
    3 1
    """
