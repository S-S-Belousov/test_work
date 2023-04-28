from random import randint


class SearchForDuplicateNumbers:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def findDuplicate(self) -> list[int]:
        result_set = set()
        for i in range(len(self.nums)-1):
            if self.nums[i] in self.nums[i+1:]:
                result_set.add(self.nums[i])
        return list(result_set)

if __name__ == '__main__':
    n = int(input('Введите N: '))
    nums = [randint(1, n) for i in range(n+2)]
    print(f'Сгенерированные числа: {nums}')
    solution = SearchForDuplicateNumbers(nums)
    print(
        'Повторяющиеся числа: {}'.format(
        solution.findDuplicate()
        )
        )
    
