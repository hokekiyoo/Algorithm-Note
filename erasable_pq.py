import heapq

class erasable_pq:
    def __init__(self, desc=False):
        self.p = []
        self.q = []
        self.sign = -1 if desc else 1
    
    def insert(self, x):
        heapq.heappush(self.p, x*self.sign)
        return 

    def erase(self, x):
        heapq.heappush(self.q, x*self.sign)
        return
        
    def top(self):
        if len(self.p) == 0:
            return -1

        while len(self.q)>0 and self.p[0] == self.q[0]:
            heapq.heappop(self.p)
            heapq.heappop(self.q)
            if len(self.p) == 0:
                return -1
        return self.sign * self.p[0]

    def pop(self):
        while len(self.q)>0 and self.p[0] == self.q[0]:
            heapq.heappop(self.p)
            heapq.heappop(self.q)
        p = heapq.heappop(self.p)
        return self.sign * p


if __name__ == "__main__":
    """
    1 : 挿入
    2 : 削除
    0 : 取り出し

    7
    1 3
    1 5
    1 7
    2 5
    0
    1 4
    0

    output
    昇順だと3,4
    降順だと7,4
    """
    pq = erasable_pq(desc=True)
    n = int(input())
    ans = []
    for _ in range(n):
        q = input().split()
        if int(q[0]) == 0:
            x = pq.pop()
            ans.append(x)
        elif int(q[0]) == 1:
            x = int(q[1])
            pq.insert(x)
        else:
            x = int(q[1])
            pq.erase(x)
    print(*ans)