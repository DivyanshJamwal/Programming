def bitonicarr(arr, n):
    arr.sort()
    arr1 = arr[0:n//2]
    arr2 = arr[n//2:]
    arr1.sort()
    arr2.sort(reverse=True)
    return arr1 + arr2
if __name__ == '__main__':
    arr = input().split(',')
    arr = [int(i) for i in arr]
    n = len(arr)
    result = bitonicarr(arr, n)
    print(result)
    for i in arr:
        print(max(arr))
        break