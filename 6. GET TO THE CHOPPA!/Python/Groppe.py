import sys

def find_shortest_path(grid, start_node, end_node):
    path = []
    
    # if it is an empty grid
    if len(grid) == 0:
        return []
    
    # if this node has no step count, it is the real start_node
    # and it needs to be set
    if not hasattr(start_node, 'step'):
        
        start_node.step = 0
    
    # if this is the end node, then we have arrived!
    if start_node is end_node:
        path.append(end_node)
        return path
    
    # if this node is not passable then return None
    if start_node.passable is False:
        return None
    
    x = start_node.position.x
    y = start_node.position.y
    results = [None] * 4
    
    # evaluate each adjacent node
    results[0] = evaluate_adjacent_node(grid, start_node.step, x, y + 1, end_node)        
    results[1] = evaluate_adjacent_node(grid, start_node.step, x, y - 1, end_node)   
    results[2] = evaluate_adjacent_node(grid, start_node.step, x + 1, y, end_node)
    results[3] = evaluate_adjacent_node(grid, start_node.step, x - 1, y, end_node)   
    
    optimum_index = -1
    top_distance = sys.maxint
    
    for index, p in enumerate(results):
        if p is None:
            continue
        if len(p) < top_distance:
            optimum_index = index
        
    if optimum_index == -1:
        return None
        
    results[optimum_index].insert(0, start_node)
        
    return results[optimum_index]

def evaluate_adjacent_node(grid, current_step, x, y, end_node):
    grid_width =  len(grid)
    grid_height = len(grid[0])
    
    # if it is in the grid
    if 0 <= y < grid_height and 0 <= x < grid_width:                                
        adjacent_node = grid[x][y]
        
        # if it is passable
        if adjacent_node.passable:
            
            # if it hasn't been stepped on OR its step is greater than current plus one
            if ((not hasattr(adjacent_node, 'step')) or (current_step + 1 < adjacent_node.step)):
                
                # set its step
                adjacent_node.step = current_step + 1
                
                # recursively call
                return find_shortest_path(grid, adjacent_node, end_node)
                
    return None