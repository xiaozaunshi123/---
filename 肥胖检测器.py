user = int(input("请输入你的身高："))
user2 = int(input("请输入你的体重"))
gender = input("请输入你的性别：")
if gender == "男":
    if (user - 100) + 3 < user2:
        print("你太重了")
    elif (user - 100) - 3 > user2:
        print("你太轻了")
    else:
        print("标准体重")
elif gender == "女":
    if (user - 110) - 3 <user2:
        print("你太重了")
    elif (user - 110) - 3 > user2:
        print("你太轻了")
    else:
        print("标准体重")
else:
    print("请输入正确的性别（男/女）")