"""
プリム法
グラフが疎の場合有向
最小全域木を求める問題
参考 : https://www.hamayanhamayan.com/entry/2018/09/17/163004
参考 : 
"""
import heapq
def prim(n,edges,s):
    """
    input
        - n : 頂点の数
        - edges: edges[i] = (コスト, 到達頂点)
        - s : スタート位置
    output
        - res : 最小全域木のコスト
    """
    q  = []
    used = [False] * n
    used[s] = True
    res = 0
    for c, b in edges[s]:
        heapq.heappush(q, (c, b))
    while q:
        c_min, b_min = heapq.heappop(q)
        if used[b_min]:
            continue
        used[b_min] = True
        res += c_min
        for c, b in edges[b_min]:
            if not used[b]:
                heapq.heappush(q,(c,b))
        
    return res

def prim_fast(n,edges,s,N):
    """
    input
        - n : 頂点の数
        - edges: edges[i] = (コスト, 到達頂点)
        - s : スタート位置
        - N : 大きな数(max(b))少なくとも頂点数よりでかい
    """
    q  = []
    used = [False] * n
    used[s] = True
    res = 0
    for c, b in edges[s]:
        heapq.heappush(q, c*N+b)
    while q:
        num = heapq.heappop(q)
        c_min = num // N
        b_min = num % N 
        if used[b_min]:
            continue
        used[b_min] = True
        res += c_min
        for c, b in edges[b_min]:
            if not used[b]:
                heapq.heappush(q,c*N+b)
    return res
    
    
    e = []
if __name__ == "__main__":
    """
    7 9
    1 2 1
    2 3 2
    2 4 3
    3 6 10
    2 5 7
    4 5 1
    4 7 5
    5 7 8
    6 5 5
    想定 : 17
    """
    INF = 10**18
    n, m  = map(int, input().split())
    edge = [[] for _ in range(n)]
    for i in range(m):
        a,b,c = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append((c,b))
        edge[b].append((c,a))
    print(prim(n, edge, 0))
    print(prim_fast(n, edge, 0, INF))

