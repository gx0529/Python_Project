
def input_password():

    pas = input("请输入密码：")

    if len(pas) >= 8:
        return pas

    print("主动抛出异常")

    ex = Exception("密码长度不够")

    raise ex

try:
    print(input_password())

except Exception as result:
    print(result)