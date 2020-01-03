"""
二部グラフ判定
色を2色どんどん塗っていく
- 自ノードが白ならば、隣接ノードはすべて黒である。
- アウトなら二部グラフではない
"""
import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

def dfs(v, color):
    """
    :param v: 調べる点
    :param color: 何色で塗るか(0:未着色, 1:黒 -1:白)
    :return: 二部グラフかどうか
    """
    colors[v] = color
    next_v = edges[v]
    for nv in next_v:
        # 隣接点が同じ色になっちゃう
        if colors[nv] == color:
            return False
        if colors[nv] == 0:
            dfs(nv, -color)
    return True

if __name__ == '__main__':
    """
    入力
    N : 頂点の数
    M : 辺の数
    """
    N, M = map(int, input().split())
    edges = defaultdict(list)
    colors = [0 for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        edges[a].append(b) 
        edges[b].append(a)
    
    print(dfs(0,1))
    print(colors)
