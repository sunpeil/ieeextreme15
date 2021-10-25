def get_index(lst, item):
    return [i + 1 for i in range(len(lst)) if lst[i] == item]


def cost_compare(cost_a, num_a, cost_b, num_b):
    if cost_a == 0 and cost_b == 0:
        return 'TIE'
    elif cost_b == 0:
        return 'A'
    elif cost_a == 0:
        return 'B'
    elif cost_a / num_a < cost_b / num_b:
        return 'A'
    elif cost_a / num_a > cost_b / num_b:
        return 'B'
    else:
        return 'TIE'





def find_route(graph,start,end):
    # g为输入的链表{1:[2,3],2:[1],3:[1]}
    # a为起点(1-N)
    # b为终点(1-N)
    # 输出a,b路上的所有点（包括a,b)
    path = []
    stack = []
    stack.append(start)
    visited = set()
    visited.add(start)
    seen_path = {}
    # seen_node=[]
    while (len(stack) > 0):
        start = stack[-1]
        nodes = graph[start]
        if start not in seen_path.keys():
            seen_path[start] = []
        g = 0
        for w in nodes:
            if w not in visited and w not in seen_path[start]:
                g = g + 1
                stack.append(w)
                visited.add(w)
                seen_path[start].append(w)
                if w == end:
                    path.append(list(stack))
                    old_pop = stack.pop()
                    visited.remove(old_pop)
                break
        if g == 0:
            old_pop = stack.pop()
            del seen_path[old_pop]
            visited.remove(old_pop)
    return path




if __name__ == '__main__':
    N = int(input())
    g = {}
    for i in range(1, int(N) + 1):
        g[i] = []
    # 车站归属
    owned = [i for i in input().split()]
    edge_ab = []
    # 构建链表
    for i in range(N - 1):
        a, b = [int(i) for i in input().split()]
        g[a].append(b)
        g[b].append(a)
    # 得到属于a的和属于b的城市车站点，对应下标0-N-1分别对应1-N城市
    owned_a = get_index(owned, '0')
    owned_b = get_index(owned, '1')
    N_event = int(input())
    for i in range(N_event):
        get_lines = [i for i in input().split()]
        flag = get_lines[0]
        if flag == '1':
            # 交易事件
            if (owned[int(get_lines[1]) - 1] == '1'):
                owned[int(get_lines[1]) - 1] = '0'
            else:
                owned[int(get_lines[1]) - 1] = '1'
            # 重新划定归属
            owned_a = get_index(owned, '0')
            owned_b = get_index(owned, '1')
        else:
            # 比较事件
            u, v = int(get_lines[1]), int(get_lines[2])
            # 得到u-v路上的所有点
            u_v_point = find_route(g, u, v)[0]
            temp_th = len(u_v_point)
            a_cost = 0  # 记录a的路总长
            b_cost = 0  # 记录b的路总长
            num_a = 0  # 记录a简单路的个数
            num_b = 0  # 记录b简单路的个数
            # 遍历a的路，寻找包含u-v的路
            for ii in range(len(owned_a)):
                start = owned_a[ii]
                for kk in range(ii + 1, len(owned_a)):
                    end = owned_a[kk]
                    temp = 0
                    a_point = find_route(g, start, end)[0]

                    for point in u_v_point:
                        if point in a_point:
                            temp += 1
                    if temp == temp_th:
                        num_a += 1
                        a_cost += len(a_point)
            # 遍历b的路，寻找包含u-v的路
            for ii in range(len(owned_b)):
                start = owned_b[ii]
                for kk in range(ii + 1, len(owned_b)):
                    end = owned_b[kk]
                    temp = 0
                    b_point = find_route(g, start, end)[0]

                    for point in u_v_point:
                        if point in b_point:
                            temp += 1
                    if temp == temp_th:
                        num_b += 1
                        b_cost += len(b_point)

            print(cost_compare(a_cost, num_a, b_cost, num_b))
