
def rotate_(image, mode):
    if mode == 1:
        temp = list(zip(*image))[::-1]
    elif mode == 3:
        temp = list(zip(*image))[::-1]
        temp = list(zip(*temp))[::-1]
        temp = list(zip(*temp))[::-1]
    return temp

def reverse_(image, mode):
    if mode == 1: # up down
        temp = image
        temp.reverse()
    elif mode == 2:
        temp = image
        temp = [list(reversed(x)) for x in image]
    return temp




def get_result(image1, image2):
    result = []
    result.append(compare(image1, image2))
    result.append(compare(rotate_(image1, 1), image2)) # 顺时针90
    result.append(compare(rotate_(image1, 3), image2)) # 逆时针90
    result.append(compare(reverse_(image1, 1), image2))
    result.append(compare(reverse_(image1, 2), image2))
    result.append(compare(reverse_(rotate_(image1, 1), 1), image2))
    result.append(compare(reverse_(rotate_(image1, 1), 2), image2))
    result.append(compare(reverse_(rotate_(image1, 3), 1), image2))
    result.append(compare(reverse_(rotate_(image1, 3), 2), image2))
    return max(result)


def compare(image1, image2):
    result = []
    r1, c1 = len(image1), len(image1[0])
    r2, c2 = len(image2), len(image2[0])
    for i in range( 2 *r1 +r2 -2):
        for j in range( 2 *c1 +c2 -2):
            temp = 0
            for k in range(r1):
                for q in range(c1):
                    if i + k >= r1 -1 and i+ k < r1 + r2 - 1 and j + q >= c1 - 1 and j + q < c1 + c2 - 1:
                        if image1[k][q] == '#' and image2[i + k - r1 + 1][j + q - c1 + 1] == '#':
                            temp += 1
            result.append(temp)
    return max(result)


if __name__ == '__main__':
    t = int(input())
    for T in range(t):
        image1, image2 = [], []
        r1, c1 = [int(x) for x in input().split(' ')]
        for i in range(r1):
            image1.append(input())
        r2, c2 = [int(x) for x in input().split(' ')]
        for i in range(r2):
            image2.append(input())
        image1_list = [list(x) for x in image1]
        image2_list = [list(x) for x in image2]
        result = get_result(image1_list, image2_list)
        print(result)
