from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    nums_dict = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in nums_dict:
            return [nums_dict[complement], index]
        else:
            nums_dict[number] = index


assert two_sum([3, 3], 6) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
