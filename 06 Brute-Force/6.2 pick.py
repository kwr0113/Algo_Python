# n개의 원소 중 m개를 고르는 모든 조합을 찾는 알고리즘
import itertools


def pick(population, num):
    ans = []
    # 정의된 값인지 확인한다.
    if num > len(population):
        return ans
    # Base Case
    if num == 1:
        for i in population:
            ans.append([i])
    # General Case
    elif num > 1:
        # i가 시작하는 값 - len(population) - (n-1)이고 이 때 n은 lst로부터 추출할 개수와 같다.
        for i in range(len(population) - num + 1):
            for temp in pick(population[i + 1:], num - 1):
                ans.append([population[i]] + temp)

    return ans



