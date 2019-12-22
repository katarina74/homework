def f1(n0):
    n = list(map(int, str(n0)))
    if len(n) == 1:
        return n[0]
    else:
        return f1(sum(n))


def f2(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return f2(m-1, 1)
    else:
        return f2(m-1, f2(m, n-1))


def f3(n0):
    print(n0 % 10)
    n = n0 // 10
    if n != 0:
        return f3(n)
    else:
        return None


def f4(n, res=""):
    res = str(n % 2) + res
    n = n // 2
    if n > 0:
        return f4(n, res)
    else:
        return res


def f5(n, k=2):
    if k > n/2:
        print(int(n))
        return None
    if n % k == 0:
        print(int(k))
        f5(n/k, k)
    else:
        f5(n, k+1)