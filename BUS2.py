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


# def find_route_2(graph,start,end,visited,path):
#     # g为输入的链表{1:[2,3],2:[1],3:[1]}
#     # a为起点(1-N)
#     # b为终点(1-N)
#     # 输出a,b路上的所有点（包括a,b)
#     c = 0
#     for k in graph[start]:
#         c = k
#         if k in visited:
#             continue
#         visited.add(k)
#         path.append(k)
#         if path[-1] == end:
#             break
#         find_route_2(graph,k,end,visited,path)
#
#         visited.remove(c)
#         del path[-1]
#     return path
#

def find_route_2(graph,start,end,visited_input,path_input):
    path = []
    stack = []
    stack.append(start)
    visited = visited_input.copy()
    seen_path = {}
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
                    path = list(stack)
                    old_pop = stack.pop()
                    visited.remove(old_pop)
                break
        if g == 0:
            old_pop = stack.pop()
            del seen_path[old_pop]
            visited.remove(old_pop)
    path_res = []
    for k in range(len(path_input)):
        path_res.append(path_input[k])
    for k in range(1, len(path)):
        path_res.append(path[k])
    return path_res


def find_father(g,u_v_point,owned):
    # u_v_point 为uv路上的点
    # owned为需要找的集合点
    # g为链表
    # 返回总的长度和个数
    visited = set(u_v_point) # 记录下已经经过的点
    # 伸出树枝的节点
    u, v = u_v_point[0], u_v_point[-1]

    if u in owned and v in owned:
        num = 1
        cost = len(u_v_point) - 1
    else:
        cost = 0
        num = 0
    for i in owned:
        path_v_ini = u_v_point.copy()
        path_u_ini = path_v_ini[::-1]
        if i not in u_v_point:
            path_u = find_route_2(g, u, i, visited, path_u_ini)
            path_v = find_route_2(g, v, i, visited, path_v_ini)
            if (not path_u[-1] == [u]) and path_u[-1] in owned and v in path_u:
                num += 1
                cost += len(path_u) - 1
            if (not path_v[-1] == [v]) and path_v[-1] in owned and u in path_v:
                num += 1
                cost += len(path_v) - 1
    return cost,num


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
            # 通过u-v-point点迭代找出经过该路到达其他的
            a_cost, num_a = find_father(g,u_v_point,owned_a)
            b_cost, num_b = find_father(g, u_v_point, owned_b)
            print(cost_compare(a_cost, num_a, b_cost, num_b))
