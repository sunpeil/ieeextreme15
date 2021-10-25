import heapq
def find_rout(g,S,T,ids):
    visited = set()
    max_dist = -1
    min_path = [S]
    min_dist = {town_id: max_dist for town_id in ids}
    min_dist[S] = 0
    former = {town_id: -1 for town_id in ids}
    queue = [(0, S)]
    while queue:
        curr_dist, curr_node = heapq.heappop(queue)
        if curr_node in visited:
            continue
        if curr_node == T:
            break
        visited.add(curr_node)
        for next_node, dist, next_color in g[curr_node]:
            if next_node in visited:
                continue
            next_dist = curr_dist + dist
            if(min_dist[next_node] == -1) or (min_dist[next_node] >= next_dist):
                min_dist[next_node] = next_dist
                former[next_node] = curr_node
                heapq.heappush(queue, (next_dist, next_node))
    k = former[T]
    while k != S and k > 0:
        min_path.insert(1,k)
        k = former[k]
    min_path.append(T)
    return min_dist[T], min_path


def get_max_C(path,g,K,ids,dist,T):
    # 求最大C
    exc_t = K - dist
    # 需要变色的次数
    num_tran = 0
    g_t = {}
    for i in ids:
        g_t[i] = {}
    for i in ids:
        for ss in g[i]:
            g_t[i][ss[0]] = ss[2]
            g_t[ss[0]][i] = ss[2]
    ini_color = 'a'
    for i in range(1,len(path)):
        next_color = g_t[path[i]][path[i-1]]
        if next_color == ini_color :
            d = 0
        elif next_color =='a':
            if ini_color == 'b' or ini_color =='e':
                d = 1
            else:
                d = 2
        elif next_color =='b':
            if ini_color == 'a' or ini_color == 'c':
                d = 1
            else:
                d= 2
        elif next_color == 'c':
            if ini_color == 'b' or ini_color == 'd':
                d = 1
            else:
                d = 2
        elif next_color == 'd':
            if ini_color == 'c' or ini_color == 'e':
                d = 1
            else:
                d = 2
        elif next_color == 'e':
            if ini_color == 'a' or ini_color == 'd':
                d = 1
            else:
                d = 2
        num_tran += d
        ini_color = next_color

    if num_tran== 0:
        print('relaxing')
    elif exc_t < num_tran:
        print('impossible')
    else:
        print(int(exc_t/num_tran))



if __name__ == '__main__':
    T = int(input())
    for k in range(T):
        N, M, K = [int(i) for i in input().split(' ')]
        # 构建链表图
        g = {}
        ids = []
        for i in range(1, int(N) + 1):
            ids.append(i)
            g[i] = []
        for i in range(M):
            x,y,d,c = [j for j in input().split(' ')]
            g[int(x)].append([int(y), int(d), str(c)])
            g[int(y)].append([int(x), int(d), str(c)])
        S = min(ids)
        T = max(ids)
        dist, path = find_rout(g, S, T, ids)
        if dist> K:
            print('impossible')
        else:
            get_max_C(path,g,K,ids,dist,T)

