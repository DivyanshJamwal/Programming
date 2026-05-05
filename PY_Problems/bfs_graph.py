from collections import deque

def bfs(arr, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for n in arr[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

if __name__ == "__main__":
    arr = [[2, 3, 1],[0],[0, 4],[0],[2]]
    bfs(arr, 0)