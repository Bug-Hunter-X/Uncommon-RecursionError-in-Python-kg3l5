def function_with_uncommon_error_solution(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result

# This iterative solution avoids the RecursionError
result = function_with_uncommon_error_solution(1000) # Works without error