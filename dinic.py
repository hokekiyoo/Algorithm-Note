"""
Dinic's Algorithm
最大フロー問題をO(VE^2)で解く
参考 : https://tjkendev.github.io/procon-library/python/max_flow/dinic.html

最大フローとはどんなものか
参考 : https://qiita.com/drken/items/e805e3f514acceb87602

Ford-Fulkerson Algorithm -> 最悪計算量がO(|f|(|V|+|E|))
DinicとEdmond-Karpが改良版としてある
どちらもO(VE^2)だけどDinicのほうが実用上早く動作することが多い。
違いはここに。
https://kopricky.github.io/code/NetworkFlow/dinic_memo.html

1. BFSで、sourceから各頂点までの距離(level)を計算する
2. DFSで、sourceからの距離が遠くなるようなパスを見つけフローを流す

DFSのキャパ更新方法(帰りがけ順)
参考 : https://qiita.com/drken/items/4a7869c5e304883f539b#3-4-dfs-%E3%81%AE%E6%8E%A2%E7%B4%A2%E9%A0%86%E5%BA%8F%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E3%81%AE%E8%A9%B3%E7%B4%B0
"""

from collections import deque
from collections import defaultdict
class Dinic:
    def __init__(self):
        # self.N = N
        self.G = defaultdict(list)
    
    def add_edge(self, fr, to, cap):
        """
        :param fr: 始点
        :param to: 終点
        :param cap: 容量
        """
        # forwardの最後には、キャパのうちどれだけ使ったかが入る
        forward = [to, cap, None]
        backward = [fr, 0, forward]
        forward[-1] = backward
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        """
        :param v1: 始点
        :param v2: 終点
        :param cap1: 容量1
        :param cap2: 容量2
        """
        edge1 = [v2, cap1, None]
        edge2 = [v1, cap2, edge1]
        edge1[-1] = edge2
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        """
        :param s: bfsの始点(source)
        :param t: bfsの終点(sink)
        :return: tに到達したかどうか。(sourceからの距離を保存しながら)
        """
        self.level = level = [-1]*len(self.G)
        q = deque([s])
        level[s] = 0
        G = self.G
        while len(q) > 0:
            v = q.popleft()
            lv = level[v] + 1
            nexts = G[v]
            for w, cap, _ in nexts:
                if cap > 0 and level[w] == -1:
                    level[w] = lv
                    q.append(w)
        is_reach = (level[t] > 0)
        return is_reach

    def dfs(self, v, t, f):
        """
        :param v: 点v
        :param t: 終点(sink)
        :param f: v時点でのフロー
        :return: 終点到達時のフローを返す
        """   
        if v == t:
            return f
        level = self.level
        nexts = self.G[v]
        for edge in nexts:
            w, cap, rev = edge
            # まだキャパがあるならば
            if cap > 0 and level[v] < level[w]:
                # キャパが余ってるなら全部流すし
                # カツカツならキャパのmaxまで流す
                d = self.dfs(w, t, min(f, cap))
                # 帰りがけに、更新
                if d > 0:
                    # 順方向のキャパをd下げる
                    # 逆方向のキャパをd増やす
                    edge[1] -= d
                    rev[1] += d
                    return d
        # 次の道が見つからなければ終了
        return 0
    
    def flow(self, s, t):
        """
        :param s: 始点
        :param t: 終点
        :return : 最大フロー
        """
        flow = 0
        INF = 10**10
        G = self.G
        # ルートが存在する限り、続ける
        while self.bfs(s, t):
            f = INF
            while f > 0:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

if __name__ == '__main__':
    """
    テストケースはここ
    http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A
    
    eg.
    4 5
    0 1 2
    0 2 1
    1 2 1
    1 3 1
    2 3 2

    ->3
    """
    N, M  = map(int, input().split())
    dinic = Dinic()
    for i in range(M):
        u, v, cap = map(int, input().split())
        dinic.add_edge(u, v, cap)
    s = 0
    t = N-1
    ans = dinic.flow(s,t)
    print(ans)