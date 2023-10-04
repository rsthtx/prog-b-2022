def fib(n):
    # return fib_recursive(n)
    # return fib_recursive_memo(n)
    return fib_iterative(n)


def fib_recursive(n):
    if n == 0:
        return 0
    
    if n < 2:
        return 1
    
    
    return fib_recursive(n - 1)  + fib_recursive(n -2)


def fib_iterative(n):
    if n == 0:
        return 0

    x = 0
    y = 1

    for _ in range(n-1):
        x, y = y, x + y
    
    return y
    
memo = {}
def fib_recursive_memo(n):
    if n == 0:
        return 0
    
    if n < 2:
        return 1
    
    if memo.get(n):
        return memo[n]
    
    result = fib_recursive_memo(n - 1)  + fib_recursive_memo(n -2)
    memo[n] = result
    return result


def test_0():
    assert fib(0) == 0

def test_1():
    assert fib(1) == 1

def test_first_12():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    for idx, val in enumerate(expected):
        assert fib(idx) == val

def test_fib_49():
    assert fib(49) == 7778742049

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    import time

    for n in range(50):
        start = time.perf_counter()
        result = fib(n)
        print(f"fib({n}) : {result}, Elapsed time: {time.perf_counter() - start}")