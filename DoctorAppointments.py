import numpy as np
def BFS_hungary(g,Nx,Ny,Mx,My,chk,Q,prev):
    res=0
    for i in range(Nx):
        if Mx[i]==-1:
            qs=qe=0
            Q[qe]=i
            qe+=1
            prev[i]=-1

            flag=0
            while(qs<qe and not flag):
                u=Q[qs]
                for v in range(Ny):
                    if flag:continue
                    if g[u][v] and chk[v]!=i:
                        chk[v]=i
                        Q[qe]=My[v]
                        qe+=1
                        if My[v]>=0:
                            prev[My[v]]=u
                        else:
                            flag=1
                            d,e=u,v
                            while d!=-1:
                                t=Mx[d]
                                Mx[d]=e
                                My[e]=d
                                d=prev[d]
                                e=t
                qs+=1
            if Mx[i]!=-1:
                res+=1
    return res,My



if __name__ == '__main__':
    T = int(input())
    for iii in range(T):
        N = int(input())
        dict = {}
        # 匹配数组  匹配为1 不匹配为0
        g = []
        for kkk in range(N):
            L, R = [int(i) for i in input().split()]
            if L == 1 and R == N:
                g_k = [1]*N
            elif L == 1:
                g_k =([1] * (R))+[0]*(N-R)
            elif R == N:
                g_k = [0] * (L - 1) + ([1] * (N - L + 1))
            else:
                g_k = [0]*(L-1)+[1]*(R-L+1)+[0]*(N-R)
            g.append(g_k)
        Mx = [-1]*N
        My = [-1]*N
        chk = [-1]*N
        prev = [0]*N
        Q = [0 for i in range(100000)]
        res = BFS_hungary(g, N, N, Mx, My, chk, Q, prev)
        if res[0] == N:
            list_ans = res[1]
            result = [str(int(i)+1) for i in list_ans]
            print(" ".join(result))
        else:
            print('impossible')
