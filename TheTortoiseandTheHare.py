import heapq
def find_rout(g,S,T,ids):
    visited = set()
    max_dist = -1
    min_path = []
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
        for next_node, dist in g[curr_node]:
            if next_node in visited:
                continue
            next_dist = curr_dist + dist
            if(min_dist[next_node] == -1) or (min_dist[next_node] >= next_dist):
                min_dist[next_node] = next_dist
                former[next_node] = curr_node
                heapq.heappush(queue, (next_dist, next_color,next_node))
    k = former[T]
    while k != S and k > 0:
        min_path.insert(0, k)
        k = former[k]
    return min_dist[T], min_path


if __name__ == '__main__':
    N, M, S, T = [int(x) for x in input().split(' ')]
    ids = []
    g = {}
    for i in range(1, N+1):
        ids.append(i)
        g[i] = []
    for i in range(int(M)):
        a, b, d = [int(x) for x in input().split(' ')]
        g[a].append((b, d))
        g[b].append((a, d))
    min_dist_Tortoise, min_path_Tortoise = find_rout(g,S,T,ids)
    # 判断是否存在路
    if min_dist_Tortoise > -1:
        flag = False
        for i in min_path_Tortoise:
            g_Hare = g.copy()
            g_Hare[i] = []
            min_dist_Hare, min_path_Hare = find_rout(g_Hare,S,T,ids)
            if min_dist_Hare > -1:
                flag = False
                print(i)
                break
            else:
                flag = True
        if flag:

            min_path_Tortoise.append(S)
            min_path_Tortoise.append(T)
            flag1 = False
            for k in ids:
                if k in min_path_Tortoise:
                    print(k)
                    break
                else:
                    flag1 = True
            if flag1:
                print(-1)
    else:
            print(-1)