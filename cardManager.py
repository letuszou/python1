# -*- coding:utf-8 -*-

# 一个增删改查的小项目

# 1. 打印功能提示
print("=" * 50)
print("    名字关系系统 V8.6")
print(" 1:添加一个新的信息")
print(" 2:删除一个信息")
print(" 3:修改一个信息")
print(" 4:查询一个信息")
print(" 5:退出系统")
print("=" * 50)

cards = []  # 定义一个空的列表用来存储添加的名字

while True:
    # 2. 获取用的选择
    num = int(raw_input("请输入功能序号:"))
    # 3. 根据用户的选择,执行相应的功能

    if num == 1:
        name = raw_input("请输入名字:")
        qq = raw_input("请输入你的qq")
        email = raw_input("请输入你的电子邮箱")

        card = {}
        card["name"] = name
        card["qq"] = qq
        card["email"] = email
        cards.append(card)

        print(cards)
    elif num == 2:
        name = raw_input("你输入你要删除的姓名？")
        i = 0
        for item in cards:
            if name == item["name"]:
                cards.remove(item)
            else:
                print "查无此人"
            i += 1
        print cards
    elif num == 3:
        name = raw_input("你输入你要修改的姓名？")
        i = 0
        for item in cards:
            if name == item["name"]:
                name = raw_input("请输入修改后的名字")
                qq = raw_input("请输入修改后的qq")
                email = raw_input("请输入修改后的email")
                card = {}
                card["name"] = name
                card["qq"] = qq
                card["email"] = email
                cards[i] = card
            else:
                print "查无此人"
            i += 1
        print cards
    elif num == 4:
        name = raw_input("你输入你要查的姓名？")
        for item in cards:
            if name == item["name"]:
                print ("找到了，姓名为%s，qq为%s，email为%s" % (item["name"], item["qq"], item["email"]))
            else:
                print "查无此人"
    elif num == 5:
        break
    else:
        print("您的输入有误,请重新输入")
