def fib(n):
    tbl = [0] * (n+1)
    tbl[0] = 0
    tbl[1] = 1

    for i, _ in enumerate(tbl):
        if i<=1:
            continue
        tbl[i] = tbl[i-1] + tbl[i-2]
    return tbl[-1]


print(f"{fib(2)=}")
print(f"{fib(3)=}")
print(f"{fib(6)=}")
print(f"{fib(10)=}")
print(f"{fib(1030)=}")
