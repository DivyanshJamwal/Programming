def binarysearch(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysearch(arr, low, mid - 1, x)
        else:
            return binarysearch(arr, mid + 1, high, x)
    else:
        return -1

if __name__ == '__main__':
    arr = input().split(',')
    arr = [int(i) for i in arr]
    x = int(input())
    result = binarysearch(arr, 0, len(arr) - 1, x)
    if result != -1:
        print(f'Element {x} is present at index', str(result))
    else:
        print(f'Element {x} is not present in array')