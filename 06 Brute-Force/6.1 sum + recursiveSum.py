# 1부터 n까지의 합을 계산하는 반복 함수와 재귀 함수

def ssum(n):
    ret = 0
    for i in range(1, n+1):
        ret += i
    return ret


def recursiveSum(n):
    if n == 1:
        return 1
    return n + recursiveSum(n-1)


print(ssum(10))
print(recursiveSum(10))
