function dblLinear(n) {
    var u = [1],
        seen = { 1: true },
        queue = [3, 4],
        x, x2, x3;
        
    while (u.length <= n) {
      x = queue.splice(0, 1)[0];
      x2 = 2 * x + 1;
      x3 = 3 * x + 1;
      
      if (!seen[x]) {
        u.push(x);
        seen[x] = true;
        
        if (!seen[x2]) { addToQueue(x2, queue); }
        if (!seen[x3]) { addToQueue(x3, queue); }
      }
    }
    
    return u[n];
}

function addToQueue(x, queue) {
  var min = 0,
      max = queue.length,
      idx = Math.floor(max / 2);
      
  if (x < queue[0]) {
    queue.splice(0, 0, x);
    return;
  }

  while (min !== max && min !== max-1) {
    if (queue[idx] === x) {
      return;
    } else if (queue[idx] < x) {
      min = idx;
    } else {
      max = idx;
    }
    
    idx = Math.floor((max + min) / 2);
  }
    
  queue.splice(max, 0, x);
}
