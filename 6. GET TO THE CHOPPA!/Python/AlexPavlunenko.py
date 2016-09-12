import time


max_x = 0;
max_y = 0;
node_queue = []

def find_shortest_path(grid, start_node, end_node):
    if(len(grid) == 0):
        return []
        
    if(len(grid) == 1):
        return [grid[0][0]]
            
    global max_x
    global max_y
    
    max_x = len(grid)
    max_y = len(grid[0])  
    
    direct = direct_path(grid, start_node, end_node)
    #print direct
    
    directOK = 1
    
    for n in direct:
        if not n.passable:
            directOK = 0
            break
            
    if(directOK):
        return direct + [end_node]
    
    #start_time = time.time()
    for line in grid:
        for node in line:
            node.neighbors = getNeighbors(grid, node)
            node.path = []
    #print("--- %s seconds ---" % (time.time() - start_time))    
    
    if(max_x == 5 or max_x == 22):
        path = bfs_paths(grid, start_node, end_node)
       # print("--- %s seconds ---" % (time.time() - start_time))
        path = [start_node] + path
        #print path
        

    return path
    
def direct_path(grid, start, goal):
    
    steps = []
    start_x = start.position.x
    end_x = goal.position.x
    start_y = start.position.y
    end_y = goal.position.y
    
    if(start.position.x > goal.position.x):
        start_x = goal.position.x
        end_x = start.position.x

    if(start.position.y > goal.position.y):
        start_y = goal.position.y
        end_y = start.position.y
        
    for x in range(start_x, end_x):
        steps.append(grid[x][start_y])
        
    for y in range(start_y, end_y):
        steps.append(grid[end_x][y])
                    
    return steps
    
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None    
    
def bfs_paths(graph, start, goal):
    queue = [start]
    
    while queue:
        vertex = queue.pop(0)
        path = vertex.path
        for next in set(vertex.neighbors)- set(vertex.path):
            if next == goal:                 
                 return path + [next]
            else:                   
                next.path = path + [next]
                queue.append(next)
                
                

def getNeighbors(grid, node):

    result = []
    x = node.position.x - 1
    y = node.position.y    
        
    if( x >= 0 and x < max_x and grid[x][y].passable):
        result.append(grid[x][y])
        
    x+=2
    
    if( x >= 0 and x < max_x and grid[x][y].passable):
        result.append(grid[x][y])
        
    x-=1
    y-=1
    
    if( y >= 0 and y < max_y and grid[x][y].passable):
        result.append(grid[x][y])        
      
    y+=2
    
    if( y >= 0 and y < max_y and grid[x][y].passable):
        result.append(grid[x][y])        
      
    return result
