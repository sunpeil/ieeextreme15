
ans = 0
K = 0
mode = 998244353

def dfs(g, sum, i):
    global ans
    while True:
        if g[i][0] != 0:
            sum += g[i][1]
            g[i][0] -= 1
            if sum == K:
                ans += 1
            elif sum < K:
                dfs(g, sum, i )
            g[i][0] += 1
            sum -= g[i][1]
        i += 1
        if i >= len(g):
            break


if __name__ == "__main__":
    N, K = [int(i) for i in input().split(' ')]
    g = []
    for i in range(N):
        bag, candy = [int(i) for i in input().split(' ')]
        g.append([bag,candy])
    dfs(g, 0, 0)
    print(ans%mode)