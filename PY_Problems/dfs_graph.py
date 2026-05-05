def dfs(arr, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for n in arr[start]:
        if n not in visited:
            dfs(arr, n, visited)

if __name__ == "__main__":
    arr = [[2, 3, 1],[0],[0, 4],[0],[2]]
    dfs(arr, 0)