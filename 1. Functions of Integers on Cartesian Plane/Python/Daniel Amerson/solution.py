def sumin(n):
    if n == 0:
        return 0

    range_list = list(range(1, n + 1))
    intermediate_sum_function = min_memoize()
    return sum_rows(lambda x: intermediate_sum_function(range_list[:x]) + (x * (n - x)), range(1, n + 1))

    
def sumax(n):
    if n == 0:
        return 0

    range_list = list(range(1, n + 1))
    intermediate_sum_function = max_memoize()
    return sum_rows(lambda x: intermediate_sum_function(range_list[(x - 1):], n) + (x * (x - 1)), range(n, 0, -1))


def sumsum(n):
    return sumin(n) + sumax(n)


def min_memoize():
    memoize_map = {}

    def intermediate(row):
        if row[-1] == 1:
            memoize_map[1] = 1
        else:
            memoize_map[row[-1]] = memoize_map[row[-1] - 1] + row[-1]

        return memoize_map[row[-1]]
    return intermediate


def max_memoize():
    memoize_map = {}

    def intermediate(row, n):
        if row[0] == n:
            memoize_map[n] = n
        else:
            memoize_map[row[0]] = memoize_map[row[0] + 1] + row[0]

        return memoize_map[row[0]]
    return intermediate


def sum_rows(row_calculation_function, range_to_map):
    return reduce(lambda x, y: x + y, map(row_calculation_function, range_to_map))