function sumIntervals(intervals){
  var seenIntervals = {};
  
  intervals.forEach(interval => {
    for (var i = interval[0]; i < interval[1]; i++) {
      seenIntervals[i] = 0;
    }
  });
  
  return Object.keys(seenIntervals).length;
}
