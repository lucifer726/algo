def binary_search(list, item):
    n = len(list)
    if n < 1:
        return None
    mid = n // 2
    if list[mid] > item:
        return binary_search(list[0:mid], item)
    elif list[mid] < item:
        return binary_search(list[mid + 1:], item)
    else:
        return mid


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 4))
