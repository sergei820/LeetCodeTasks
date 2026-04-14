
def recursion_sum(n: int):
    if n == 1:
        return 1
    return n + recursion_sum(n - 1)


print(recursion_sum(5))  # 15
