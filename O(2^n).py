def generate_subsets(nums):
    subsets = []
    n = len(nums)

    # 0부터 2^n까지의 모든 숫자에 대해 반복
    for i in range(2 ** n):
        subset = []

        # 해당 비트가 1인 원소를 subset에 추가
        for j in range(n):
            if (i >> j) & 1:
                subset.append(nums[j])

        subsets.append(subset)

    return subsets