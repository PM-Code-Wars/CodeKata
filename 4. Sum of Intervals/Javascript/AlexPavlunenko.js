var test1 = sumIntervals([[1, 5]]);
console.log('test1:' + test1);

test1 = sumIntervals([[1, 5], [6, 10]]);
console.log('test2:' + test1);

test1 = sumIntervals([[1, 5], [1, 5]]);
console.log('test3:' + test1);

test1 = sumIntervals([[1, 4], [7, 10], [3, 5]]);
console.log('test4:' + test1);

function sumIntervals(intervals) {
    var current,
            start = 0,
            end = 0,
            total = 0,
            sorted = intervals.sort(compareIntervals);

    start = sorted[0][0];
    end = sorted[0][1];

    if (sorted.length > 1)
    {
        for (var i = 1; i < sorted.length; i++) {
            current = sorted[i];

            if (current[0] < end && current[1] > end)
            {
                end = current[1];
            } else {                
                if (current[0] > end && current[1] > end)
                {
                    total += end - start;
                    start = current[0];
                    end = current[1];
                }
            }

            if (i === sorted.length - 1)
            {
                total += end - start;
            }
        }
    } else {
        total += end - start;
    }

    return total;
}

function compareIntervals(a, b) {
    if (a[0] > b[0]) {
        return 1;
    } else if (a[0] < b[0]) {
        return -1;
    } else {
        return 0;
    }
}


