def function_with_uncommon_error(n):
    if n == 0:
        return 0  # this part is wrong and will cause the error
    else:
        return n + function_with_uncommon_error(n-1)

# This will cause a RecursionError, but only for large enough n values.
result = function_with_uncommon_error(1000)