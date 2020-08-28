def sum_of_intervals(intervals):
    visited = []

    sum = 0
    for interval in intervals:
        for i in range(interval[0], interval[1]):
            if i in visited:
                continue
            else:
                sum += 1
                visited.append(i)
    return sum
