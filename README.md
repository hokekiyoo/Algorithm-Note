# Algorithm-Note
書いたものまとめ
(python3で動作)

|Filename|Algorithm|Description|
|---|---|---|
|bfs|幅優先探索|全探索系(deque利用)|
|dfs|深さ優先探索|全探索系(再帰関数利用、2パターン用意)|
|gcd_lcm|最大公約数/最小公倍数|ユークリッドの互除法を利用|
|divisors|約数列挙|`O(sqrt(N))`で動作|
|eratosthenes|エラトステネスの篩|素数列挙|
|modconv|余り考慮型組み合わせ数|大きい数でも高速。フェルマー小定理利用|
|p_factorization|素因数分解|エラトステネスの篩を利用|
|bellmanford|ベルマンフォード法|最短路問題。`O(VE)`負の閉路判定|
|dijkstra|ダイクストラ法|最短路問題(正のコスト)。`O(VlogE`。heapq利用|
|topologicalsort|トポロジカルソート|DAGのソート。入次数を利用|
|warshallfloyd|ワーシャルフロイド法|全点対最短路。`O(V^3)`で動作|
|prim|プリム法|最小全域木。`O(VlogE)`。heapq利用|
|kruskal|クラスカル法|最小全域木。`O(VlogE)` unionfind利用|
|unionfind|UnionFind木|データ構造の一種。グループの結合、同一グループかの判断が高速|
|binarysearch|二部探索|`O(log(N))`で動作。自作とbisect利用版|
|shakutori|しゃくとり法|単調性があるものに対し`O(N)`で動作。|
|bipartite_judge|二部グラフ判定|二部グラフに帰着させると色々楽なので。判定用のもの。dfsで実装|
|bipartite_matchning|最大二部マッチング|増大路を利用。`O(V(V+E))`で動作(多分)|
|dinic|最大フロー|ディニック法を用いて、最大フローを出す。`O(VE^2)`で動作|
|segmented_tree|セグメント木|区間クエリをさばく。モノイドならOK更新、計算ともに`O(log(N))`で動作|