from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]
h = [11,12,13,14,5,10,7,8,9,0,1,2,3,4]
def best_first_search(actual_src,target,n):
    closed_list = [False]*n
    open_list = PriorityQueue()
    open_list.put((h[actual_src],actual_src))
    closed_list[actual_src] = True

    while open_list.empty() == False:
        u = open_list.get()[1]
        print(u,end =' ')
        if u==target:
            break
        for v,c in graph[u]:
            if closed_list[v]==False:
                closed_list[v] = True
                open_list.put((h[v],v))
    print()
def addedge(x,y,cost):
    graph[x].append((y,cost))
    graph[y].append((x,cost))
addedge(0,1,3)
addedge(1,10,3)
addedge(0,2,6)
addedge(0,3,5)
addedge(1,4,9)
addedge(1,5,8)
addedge(8,9,5)
addedge(8,10,6)
addedge(9,11,1)
addedge(9,12,10)
addedge(9,13,2)
addedge(2,6,12)
addedge(2,7,14)
addedge(3,8,5)
source = 0
target = 9
best_first_search(source,target,v)







