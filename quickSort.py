def quickSort(arr):
    if len(arr) < 2:
        return arr  # 基线条件：为空或只包含一个元素的数组是“有序”的
    else:
        pivot = arr[0]  # 选择基准值
        less = [i for i in arr[1:] if i <= pivot]  # 由所有小于等于基准值的元素组成的子数组

        greater = [i for i in arr[1:] if i > pivot]  # 由所有大于基准值的元素组成的子数组

        return quickSort(less) + [pivot] + quickSort(greater)


if __name__ == '__main__':
    print(quickSort([10, 5, 2, 1, 6, 9, 8, 4, 7, 3]))
