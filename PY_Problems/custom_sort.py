def custom_sort(arr, key_func):
    return sorted(arr, key=key_func)

if __name__ == "__main__":
    arr = [5,8,2,1,3,4]
    key_func = lambda x: x
    print(custom_sort(arr, key_func))