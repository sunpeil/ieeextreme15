import re

def split_str(shizi):
    #将整个字符串切割
    str = re.split(r"(\D)",shizi) #指定分割符用（）括起来，表示保留匹配项
    #print(str)
    #str.pop()

    for index,i in enumerate(str):
        if i == '':
            str.pop(index)
    #print(str)
    return str

def for_find_jian(l,i):
    if i < 0:
        return False
    try:
        x = int(l[i])
        return True
    except ValueError:
        if l[i] == '+' or l[i] == '*' or l[i] == '-':
            return False
        else:
            flag = True
            return for_find_jian(l, i-1)

def for_find_jia(l,i,flag):
    if i < 0:
        return False
    try:
        x = int(l[i])
        return True
    except ValueError:
        if flag == False:
            if l[i] == '+' or l[i] == '*' or l[i] == '-':
                return False
            else:
                if l[i] == '(':
                    flag = True
                return for_find_jia(l, i - 1, flag)
        else:
            if l[i] == '+' or l[i] == '-':
                return False
            else:
                if l[i] == '(':
                    flag = True
                return for_find_jia(l, i - 1, flag)


def for_find_cheng(l,i):
    if i < 0:
        return False
    try:
        x = int(l[i])
        return True
    except ValueError:
        if l[i] == '+' or l[i] == '*' or l[i] == '-':
            return False
        else:
            flag = True
            return for_find_cheng(l, i - 1)


def isnotinvalid(list):
    for i in range(len(list)):
        flag = False
        if list[i] == '-':
            if not for_find_jian(list,i-1):
                return False
        elif list[i] == '+':
            if not for_find_jia(list,i-1,flag):
                return False
        elif list[i] == '*':
            if not for_find_cheng(list,i-1):
                return False
    return True

if __name__ == '__main__':
    eee = 1000000007
    T = int(input())
    for i in range(T):
        #传入一个式子
        line = input()
        list = split_str(line)
        if isnotinvalid(list):
            try:
                result = eval(line)
                print(int(result)%eee)
            except:
                print('invalid')
        else:
            print('invalid')
