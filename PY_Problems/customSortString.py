def custom_sort_string(order, s):
    order_index = {char: index for index, char in enumerate(order)}
    sorted_s = sorted(s, key=lambda x: order_index.get(x, len(order)))
    return ''.join(sorted_s)

if __name__ == "__main__":
    order = "cba"
    s = "abcd"
    print(custom_sort_string(order, s))