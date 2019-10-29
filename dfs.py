"""
dfsに二種類あるイメージ
1. 予めグラフが決まっていて、探索
    見たかのどうかフラグが必要
    連結範囲内全部見ると終了になることがほとんど
2. グラフを作りながら探索
    基本木構造になる？
    作られるグラフは探索サれているわけがないので
    別に終了条件を置く必要がある

"""

# 1
import sys
sys.setrecursionlimit(100000)
N = #頂点の数
used = [False] * N
def dfs(G, v):
    # vを訪問済みにする
    used[v] = True
    #グラフ中の次のVについて
    for next_v in G[v]:
        # すでに見られていたら無視
        if used[next_v]: continue
        # 見られていない場合、再帰的に探索
        ### なにかやりたい処理を書く
        dfs(G, next_v)

# 2
import sys
sys.setrecursionlimit(100000)
def dfs(v):
    if # 終了条件
        ### 最後にしたい処理を書く
        continue
    loops = #ループ
    for loop in loops:
        next_v = # 次の選び方を
        dfs(next_v)

from collections import deque
# 木構造を作る
N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    # グラフに頂点を追加(距離があるときは,u,vの後に入れる)
    u,v = map(int,input().split())
    G[u-1].append((v-1))
    G[v-1].append((u-1))

# 木をBFSをする
used = [False] * N
used[] = True # 始めどこから行くか
q = deque([K-1])
while len(q) > 0:
    a = q.popleft()
    Vs = G[a]
    for u in Vs: # 頂点以外の要素がグラフにあるときはここ
        if not used[u]:
            q.append(u)
            # なにか処理を書きたいときはここに書く
            used[u] = True