"""
参考
https://ta7uw.hatenablog.com/entry/2019/05/21/122405
"""

from collections import deque
from collections import defaultdict

def topological_sort(G):

    cnt_in = defaultdict(int)
    # outs = defaultdict(list)
    for vs in G:
        for v in vs:
            cnt_in[v] += 1

    # print(cnt_in)
    res = []
    # 入次数==0
    q = deque([i for i in range(N) if cnt_in[i]==0])
    while len(q) > 0:
        v = q.popleft()
        res.append(v)
        for next_v in G[v]:
            # 入次数を下げていく
            cnt_in[next_v] -= 1
            # 入次数が0に残ったところを次に追加
            if cnt_in[next_v] == 0:
                q.append(next_v)

    return res

if __name__ == "__main__":
    """
    例
    5 8
    5 3
    2 3
    2 4
    5 2
    5 1
    1 4
    4 3
    1 3
    """
    N,M = map(int, input().split())
    G = [[] for i in range(M)]
    for i in range(M):
        u,v = map(int,input().split())
        G[u-1].append((v-1))
    
    sorted = topological_sort(G)
    print(*sorted)