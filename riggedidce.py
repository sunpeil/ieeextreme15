

if __name__ == '__main__':
    T = int(input())
    for iii in range(T):
        N = int(input())
        # 骰子的分，输出分高的
        die1, die2 = 0, 0
        # 人的分
        flag = True
        a, b = 0, 0
        for i in range(N):
            a_get, b_get = [int(x) for x in input().split(' ')]
            a += a_get
            b += b_get
            if flag:
                die1 += a_get
                die2 += b_get
            else:
                die2 += a_get
                die1 += b_get
            if a != b:
                flag = ~flag
        if die1 > die2:
            print(1)
        else:
            print(2)

