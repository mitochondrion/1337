from typing import Set, List, Dict
from functools import reduce

class Solution:
    # https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict: Dict[int: int] = {}

        for number_idx, number in enumerate(nums):
            num_dict[number] = number_idx
            sum_counterpart = target - number

            if (sum_counterpart is not number) and (sum_counterpart in num_dict):
                return [number_idx, num_dict[target - number]]

    ##### 🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕

    # https://leetcode.com/problems/product-of-array-except-self/
    def productExceptSelf_naive(self, nums: List[int]) -> List[int]:
        results: List[int] = [nums[0]] * len(nums)
        max_product = reduce((lambda number, result: number * result), nums)

        for idx, number in enumerate(nums):
            results[idx] = int(max_product / number)  # results[idx - 1] * number

        return results

    ##### 🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕

    # https://leetcode.com/problems/product-of-array-except-self/
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        results: List[int] = [None] * nums_len
        reverse_results: List[int] = [None] * nums_len

        for idx, number in enumerate(nums):
            if idx is nums_len - 1:
                break
            elif idx is 0:
                results[idx] = 1
                results[idx + 1] = number
            else:
                results[idx + 1] = results[idx] * number

        last_idx = nums_len - 1
        reverse_idx = last_idx

        while reverse_idx > 0:
            try:
                if reverse_idx is last_idx:
                    reverse_results[reverse_idx] = 1
                    reverse_results[reverse_idx - 1] = nums[reverse_idx]
                else:
                    reverse_results[reverse_idx - 1] = reverse_results[reverse_idx] * nums[reverse_idx]
            finally:
                reverse_idx -= 1

        ##### 🐞 DEBUG 🐞 #####
        print('nums', nums)
        print('products', results)
        print('reverse_products', reverse_results)
        ######################

        for idx, number in enumerate(results):
            if idx is nums_len - 1:
                break
            elif idx is 0:
                results[0] = reverse_results[idx]
                continue
            else:
                results[idx] = results[idx] * reverse_results[idx]

        return results

    ##### 🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕

    # https://leetcode.com/problems/maximum-subarray/
    def maxSubArray(self, nums: List[int]) -> int:
        pass
