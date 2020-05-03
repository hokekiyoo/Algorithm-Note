"""
LCA : Lowest Common Anscestor
最小共通祖先
手順1 EulerTourを求める
手順2 SegmentTreeにEulerTourの順にdepthを載せる
手順3 queryを発行

Euler Tourとは
頂点/辺からインデックスへの写像を与えるデータ構造
「木上の区間」と「インデックスの区間」がうまく対応するように写像を選ぶと、
いろいろなクエリが処理できる。
行きがけ順と帰りがけ順をうまく保持しておくことで計算する

EulerTour⇨SegmentTree⇨LCA 
1. 頂点の訪問順を並べた列をセグメント木にのせる
vi = [i番目に訪れた頂点]
⇨ セグメント木には、i番目の要素に(viの深さ,vi)を保存
2. クエリ
fu = [頂点uを始めに訪れた時間]
⇨ u,v のLCAの計算 min(fu,fv) <= i <= max(fu,fv)
"""

"""
木をread
"""
n = int(input())
edges = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
    
"""
segtreeを用意(unitをtupleにしておいた)
"""
class segmented_tree:
    X_unit = (1 << 30,-1)
    X_f = lambda self, a, b: min(a,b)
    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (2*N)
        
    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x 
        # 後ろから入れていく
        for i in range(self.N-1, 0, -1):
            self.X[i] = self.X_f(self.X[i<<1], self.X[i<<1|1])

    # 1点更新
    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i<<1],self.X[i<<1|1])
    
    # 区間取得
    def fold(self, l, r):
        l += self.N
        r += self.N
        vl = self.X_unit
        vr = self.X_unit
        # 外から決めていく
        while l < r:
            # print(l,r)
            if l & 1:
                vl = self.X_f(vl, self.X[l])
                l += 1
            if r & 1:
                r -= 1
                vr = self.X_f(vr, self.X[r])
            l >>= 1
            r >>= 1
        return self.X_f(vl,vr)


"""
euler tourの計算
"""
eulertour = [0]     # 根からの順路
depth = [0] * n     # 根からの深さ
first = [0] * n     # 何回目に初めて訪れたか
def dfs(v,p):
    first[v] = len(eulertour)-1
    for u in edges[v]:
        if u == p:continue
        eulertour.append(u)
        depth[u] = depth[v] + 1 
        dfs(u,v)
        eulertour.append(v)
dfs(0,-1)
# print(*eulertour)
# print(*first)
# print(*depth)

"""
LCAと、その深さを求めるquery eulertourの順番iにおける深さ
"""
def query(u,v):
    depth_tour = [(depth[e],i) for i,e in enumerate(eulertour)]
    f1 = first[u]
    f2 = first[v]
    if f1 > f2: f1,f2 = f2,f1 #swap
    st = segmented_tree(len(depth_tour))
    st.build(depth_tour)
    d, ind = st.fold(f1,f2+1)
    return eulertour[ind],d
    
"""
queryの読み込み
"""
q = int(input())
for i in range(q):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    print(query(u,v))
