'''Write a python program to implement BFS algorithm
Use the following graph 
'''

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}    
visited = []
queue = []
def bfs(visited, graph, node):
 # mark node as visited and add it to the queue    
    visited.append(node)
    queue.append(node)
    while queue:
 # remove the front vertex or the vertex at the 0th index from the queue        
        v = queue.pop(0)
        print(v,end=" ")
    #get all adjacent nodes  of the removed node v from the graph hash table
    #if an adjacent node has not been visited yet, then mark it as visisted and add it to the queue.
        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)
                
bfs(visited, graph, 'A')       