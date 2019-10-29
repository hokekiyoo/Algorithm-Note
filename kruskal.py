"""
クラスカル法
http://drken1215.hatenablog.com/entry/20121223/1356230697
http://spinda2.blog48.fc2.com/blog-entry-560.html


"""

from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        class KeyDict(dict):
            # 辞書にないときの対応
            def __missing__(self,key):
                self[key] = key
                return key
        self.parent = KeyDict()
        self.rank = defaultdict(int)
        self.weight = defaultdict(int)

    # 根を探す
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            # 経路圧縮
            # 自分自身じゃない場合は、上にさかのぼって検索(再帰的に)
            y = self.find(self.parent[x])           
            self.weight[x] += self.weight[self.parent[x]]   #圧縮時にweightを更新(和)
            self.parent[x] = y      #親の置き換え(圧縮)
            return self.parent[x]

    # 結合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        # 低い方を高い方につなげる(親のランクによる)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    ### 重み付き
    def weighted_union(self, x, y, w):
        # print("unite",x,y,w,self.weight)
        px = self.find(x)
        py = self.find(y)
        # 低い方を高い方につなげる(親のランクによる)
        # if px == py: return 0
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.weight[px] = - w - self.weight[x] + self.weight[y]
        else:
            self.parent[py] = px
            self.weight[py] =  w + self.weight[x] - self.weight[y]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return 0

    # 判定
    def judge(self, x, y):
        return self.find(x) == self.find(y)

def kruskal(n, edges, s):
    used = [True]
    uf = UnionFind(n)
    edges.sort()
    res = 0
    for c, a, b in edges:
        if not uf.judge(a, b):
            res += c 
            uf.union(a, b)
    return res


if __name__ == "__main__":
    """
    7 9
    1 2 1
    2 3 2
    2 4 3
    3 6 10
    2 5 7
    4 5 1
    4 7 9
    5 7 8
    6 5 5

    """
    n, m  = map(int, input().split())
    edge = []
    for i in range(m):
        a,b,c = map(int, input().split())
        a -= 1
        b -= 1
        edge.append((c,a,b))
    ans = kruskal(n, edge, 0)
    print(ans)


