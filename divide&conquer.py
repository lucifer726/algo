# 递归求和
def sum(list):
    if not list:
        return 0
    return list[0] + sum(list[1:])


# 递归计数
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


# 找最大的数
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]  # 三目运算符，如果list[0]>list[1],就返回list[0],否则返回list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(sum(arr))
    print(count(arr))
    print(max(arr))
