import math
def fpowx(x, n,M):

    res = 1
    x = x%M
    while n:
        if n & 1:
            res = (res * x) % M
        # compute x^2 x^4 x^8
        x = (x*x)%M
        n >>= 1
    return res



if __name__ == '__main__':
    P, Q, N, M = [int(i) for i in input().split(' ')]
    k_q = {}
    S = P
    for i in range(2, int(N) + 1):
        S += fpowx(i,Q,M)*fpowx(P,i,M)
    print(S%M)

