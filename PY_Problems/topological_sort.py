from collections import deque

def topoSort(V, adj):
    in_degree = [0] * V
    
    for i in range(V):
        for neighbor in adj[i]:
            in_degree[neighbor] += 1
    
    queue = deque([i for i in range(V) if in_degree[i] == 0])
    
    topo_order = []
    
    while queue:
        current = queue.popleft()
        topo_order.append(current)
        
        for neighbor in adj[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(topo_order) != V:
        return [] 
    
    return topo_order

if __name__ == "__main__":
    V = 6
    adj = [[2, 3], [3, 4], [], [5], [], []]
    print(topoSort(V, adj))