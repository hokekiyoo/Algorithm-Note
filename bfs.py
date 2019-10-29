"""
Breadth First Search
queue(dequeライブラリ)を使って進める

dfsと同じで、グラフが定まっている場合と、
グラフが定まっていない場合がある。
後者の恒例は迷路とか。自分で方向を定めながら次の位置を決めていく感じ
"""

from collections import deque
# グラフを作る
N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    # グラフに頂点を追加(距離やコストがあるときは,u,vの後に入れる)
    u,v = map(int,input().split())
    v -= 1
    u -= 1
    # これは無向グラフの場合
    G[u].append(v)
    G[v].append(u)

# 木をBFSをする
def bfs(N, G, s):
    """
    input
        N : 頂点の数
        G : グラフ
        s : 探索の始点
    output
        None(その時に応じて)
    """
    q = deque([])
    s = 0 # スタート
    used = [False] * N
    used[s] = True # 始めどこから行くか
    q.append(s)

    while len(q) > 0:
        v = q.popleft()
        Vs = G[v]
        for next_v in Vs: 
            # 一度走査しているところは省く
            if not used[next_v]:
                q.append(next_v)
                # なにか処理を書きたいときはここに書く
                used[next_v] = True
    print(used)