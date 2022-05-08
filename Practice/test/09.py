import csv

def read_column(i):
    # 读取某一列
    with open("./data.csv",'r') as filename:
        reader = csv.reader(filename)
        column = [row[i] for row in reader]
        print(column)
        return column[1:]

def sum(i):
    # 读取某一列的总和
    number = list(map(float,read_column(i)))
    temp = 0
    for num in number:
        temp = temp + num
    return temp

def average(i):
    # 读取某一列的平均值
    number = list(map(float,read_column(i)))
    temp = 0
    for num in number:
        temp = temp + num
    return temp / len(number)

def max(i):
    # 读取某一列的最大值
    number = list(map(float,read_column(i)))
    temp = 0
    for num in number:
        if num > temp:
            temp = num
    return temp

def time(i):
    # 获取某一列共有多少行
    number = read_column(i)
    return len(number)

def result():
    a1 = time(0) / 60
    a2 = average(1)
    a3 = sum(2) / 1024 /1024
    a4 = sum(3) /1024 /1024
    a5 = average(4) /1024 /1024
    a6 = max(4) / 1024 /1024
    print("总时间为：%.2f" % a1 + "min")
    print("平均CPU为：%.2f" % a2  + "%")
    print("IO读总：%d" % a3 +"M")
    print("IO写总：%.2f" % a4 + "M")
    print("内存平均为：%.2f" % a5 +"M")
    print("内存最大值为：%.2f" % a6 + "M")
result()