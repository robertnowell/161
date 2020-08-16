import math
import heapq
 
class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
 
    def __gt__(self, other):
        return self.dist > other.dist
 
    def __repr__(self):
        return "N(%s,%s)" % (self.id, self.dist)
 
 
G = [[Node(1, 3), Node(3, 9)], # s
     [Node(3, 5), Node(2, 2)], # u
     [Node(3, 1)],             # v
     []]                       # t
 

def Dijkstra_st_path(G, s, t):
    d = [math.inf for v in G] # "d" is "distance"
    p = [None for v in G] # "p" is "path"
    d[s] = 0 # The source node distance to itself is 0
    # Put all s's neighbors into the min-heap
    F = []
    heapq.heappush(F, Node(s, 0))
    while len(F) > 0:
        print(d, p)
        x = heapq.heappop(F)
        for y in G[x.id]:
            d_y_prev = d[y.id]
            d[y.id] = min(d[y.id], d[x.id] + y.dist)
            if d_y_prev != d[y.id]:
                p[y.id] = x.id
            heapq.heappush(F, y)
 
    path = [t]
    current = t
    while current != s:
        current = p[current]
        path.append(current)
    path.reverse()
    print(path, d[t]) 

# Dijkstra_st_path(G, 0, 3)

def delicious(T):
    D = [ 0 for i in range(len(T)) ]
    D[0] = T[0]
    D[1] = max(T[0], T[1])
    for i in range(2, len(T)):
        D[i] = max(D[i-2] + T[i], D[i-1])
    return max(D)

print(delicious([21, 4, 6, 20, 2, 5]))