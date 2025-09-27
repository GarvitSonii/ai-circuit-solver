import numpy as np
from collections import deque, defaultdict

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n  # or use size array

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


r1=1
r2=1
r=1000
r3=1
r4=1
v=20

matrix=[[1,0,0,0]]
const=[0]
dsu = DisjointSet(4)

graph={
    0: [[1,1,r1], [2,1,r2], [3,0,v]], #nodes connected to 0
    1: [[0,1,r1], [2,1,r], [3,1,r3]], #nodes connected to 1
    2: [[0,1,r2], [1,1,r], [3,1,r4]], #nodes connected to 2
    3: [[0,0,-v], [1,1,r3], [2,1,r4]] #nodes connected to 3
}

queue = deque([0])
visited = {0}

while queue:

    current_node = queue.popleft()

    for edge_info in graph.get(current_node, []):

        destination_node = edge_info[0]
        edge_type=edge_info[1]
        edge_weight=edge_info[2]

        if edge_type==0 :
            visited.add(destination_node)
            dsu.union(current_node, destination_node)
            w=edge_weight/abs(edge_weight)
            l=[]
            for i in range(4):
                if i==current_node :
                    l.append(w)
                elif i==destination_node:
                    l.append(-1*w)
                else :
                    l.append(0)
            matrix.append(l)
            const.append(abs(edge_weight))


        elif destination_node not in visited:
            visited.add(destination_node)
            queue.append(destination_node)



graph_modified = defaultdict(list)
for i in range(4):
    representative = dsu.find(i)
    graph_modified[representative].append(i)


# print(graph)
for representative, members in graph_modified.items():
    if len(members)!=1 :
        continue
    l=[0,0,0,0]

    for node in members:
        # print(node,end='=>')
        for child in graph.get(node, []):
            destination_node = child[0]
            edge_type=child[1]
            edge_weight=child[2]
            
            l[node]+=(1/edge_weight)
            l[destination_node]-=(1/edge_weight)
            
            # print(destination_node,end=' ')
        # print()
    matrix.append(l)
    const.append(0)


matrix_np=np.array(matrix)
const_np=np.array(const)

print(matrix_np)
print(const_np)

ans=np.linalg.solve(matrix_np, const_np)
print(ans)




