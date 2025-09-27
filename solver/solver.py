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


def solver(n,graph):
    ini=[0]*n
    ini[0]=1
    matrix=[ini]
    const=[0]
    dsu = DisjointSet(n)

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
                for i in range(n):
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
    for i in range(n):
        representative = dsu.find(i)
        graph_modified[representative].append(i)


    # print(graph)
    for representative, members in graph_modified.items():
        if len(members)!=1 :
            continue
        l=[0]*n

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

    try:
        ans = np.linalg.solve(matrix_np, const_np)
        return ans
    except np.linalg.LinAlgError:
        return "inconsistent or indeterminate system"



