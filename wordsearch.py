
def change_xy(x,y,i):

    if i == 0:
        x, y = x-1, y - 1
    elif i == 1:
        x, y = x-1, y
    elif i == 2:
        x, y = x-1, y +1
    elif i == 3:
        x, y = x, y - 1
    elif i == 4:
        x, y = x, y + 1
    elif i == 5:
        x, y = x+ 1, y - 1
    elif i == 6:
        x, y = x+1, y
    elif i == 7:
        x, y = x+1, y + 1
    return x,y

def find_first_ch(A,chara,R,C):
    x_first,y_first =[], []
    for i in range(R):
        for j in range(C):
            if A[i][j] == chara:
                x_first.append(i)
                y_first.append(j)
    return x_first,y_first



def find_bfs(A,word,R,C):
    chara = word[0]
    x_first,y_first = find_first_ch(A, chara, R, C)
    flag = False

    for kkk in range(len(x_first)):
        x, y = x_first[kkk],y_first[kkk]
        x_ini, y_ini = x, y
        k = 0
        while k<8:
            x, y = x_ini, y_ini
            l = 0
            for ch in word[1:]:
                l += 1
                x, y = change_xy(x, y, k)
                if x >= R or y >= C or x < 0 or y < 0:
                    break
                if A[x][y] == ch:
                    if l == len(word)-1:
                        return [x_ini,y_ini,x,y]
                    continue
                else:
                    break

            k+=1
    return []




if __name__ == '__main__':
    R,C,Q= [int(i) for i in input().split(' ')]
    A = []
    for k in range(R):
        A.append(list(input()))
    words = []
    for k in range(Q):
        words.append(list(input()))
    for k in range(Q):
        res = find_bfs(A,words[k],R,C)
        if res == []:
            print(-1)
        else:
            for kkk in range(len(res)):
                if kkk < len(res)-1:
                    print(res[kkk],end=' ')
                else:
                    print(res[kkk])
