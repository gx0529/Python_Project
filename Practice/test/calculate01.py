import csv


def not_empty(s):
    return s and s.strip()


def read_column(i):
    # 读取excel的某列
    with open('./data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        column = [row[i] for row in reader]
    # print(list(filter(not_empty, column[1:])))
    return list(column[1:])


def calculate_sum(i):
    # 计算excel的某列的和
    numbers = list(map(float, read_column(i)))
    total = 0
    for item in numbers:
        total += item
    return total


def calculate_average(i):
    # 计算excel的某列的平均值
    numbers = list(map(float, read_column(i)))
    total = 0
    for item in numbers:
        total += item
    return total / len(numbers)


def result():
    a1 = calculate_average(2) / 8
    a2 = calculate_average(3) / 1024
    a3 = calculate_average(4) / 1024
    a4 = calculate_average(5) / 1024 / 1024
    a5 = calculate_sum(3) / 1024 / 1024
    a6 = calculate_sum(4) / 1024 / 1024
    print("cpu(占比)：" + '%.2f' % a1 + "%")
    print("io读平均值(KB/S)：" + '%.2f' % a2)
    print("io写平均值(KB/S)：" + '%.2f' % a3)
    print("内存平均值(MB/S)：" + '%.2f' % a4)
    print("io读总量(M)：" + '%.2f' % a5)
    print("io写总量(M)：" + '%.2f' % a6)


result()
