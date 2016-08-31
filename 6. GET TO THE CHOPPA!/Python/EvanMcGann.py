global sptn
global spl

def find_shortest_path(grid, start_node, end_node):
    global sptn
    global spl
    sptn = {}
    spl = 0
    if (len(grid) == 0):
        return []
    
    direct_result = direct(grid, start_node, end_node)
    if direct_result is not None:
        return direct_result

    return recurse(grid, start_node, end_node, [])

def direct(grid, start, end):
    path = [start]
    curr = start

    while (curr.position.x != end.position.x or curr.position.y != end.position.y) and curr.passable == True:
        xdelta = 0
        ydelta = 0
        if curr.position.x < end.position.x:
            xdelta = 1
        elif curr.position.x > end.position.x:
            xdelta = -1
        elif curr.position.y < end.position.y:
            ydelta = 1
        elif curr.position.y > end.position.y:
            ydelta = -1        
        
        path.append(curr)
        curr = grid[curr.position.x + xdelta][curr.position.y + ydelta]
    
    if curr.position.x == end.position.x and curr.position.y == end.position.y:    
        return path
    else:
        return None

def recurse(grid, start, end, path):
    global sptn
    global spl

    if (start in sptn and sptn[start] < len(path)):
        return None
    else:
        sptn[start] = len(path)

    if (len(path) > spl and spl > 0):
        return None

    potential_next_steps = [] 
    
    if (start.position.x == end.position.x and start.position.y == end.position.y):
        return path + [start]
    
    if (start.position.x - 1 >= 0 is not None and grid[start.position.x - 1][start.position.y].passable):
        potential_next_steps.append(grid[start.position.x - 1][start.position.y])

    if (start.position.y + 1 < len(grid[start.position.x]) and grid[start.position.x][start.position.y + 1].passable):
        potential_next_steps.append(grid[start.position.x][start.position.y + 1])

    if (start.position.x + 1 < len(grid) and grid[start.position.x + 1][start.position.y].passable):
        potential_next_steps.append(grid[start.position.x + 1][start.position.y])

    if (start.position.y - 1 >= 0 and grid[start.position.x][start.position.y - 1].passable):
        potential_next_steps.append(grid[start.position.x][start.position.y - 1])

    potential_paths = []
    for step in potential_next_steps:
        if (step not in path):
            recurse_result = recurse(grid, step, end, path + [start])
            if recurse_result is not None:
                potential_paths.append(recurse_result)

    if (len(potential_paths) != 0):
        min_len = min([len(potential_path) for potential_path in potential_paths])
        for potential_path in potential_paths:
            if (len(potential_path) == min_len):
                if (spl == 0 or spl > min_len):
                    spl = min_len
                return potential_path

    return None
