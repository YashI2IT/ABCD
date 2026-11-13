calls = 0

def fib_rec(n):
    global calls
    calls += 1

    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iter(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


n = int(input("Enter n (n >= 0): "))

print("Series:", [fib_iter(i) for i in range(n + 1)])

print("Non-recursive: F(%d) = %d | O(n) time, O(1) space"
      % (n, fib_iter(n)))

if n <= 30:
    print("Recursive    : F(%d) = %d | calls = %d | O(2^n) time"
          % (n, fib_rec(n), calls))
else:
    print("Recursive    : skipped, n > 30 would take too long")
