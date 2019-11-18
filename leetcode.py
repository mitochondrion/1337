from typing import Set, List, Dict
from functools import reduce

class Solution:
    # https://leetcode.com/problems/two-sum/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict: Dict[int: int] = {}

        for number_idx, number in enumerate(nums):
            num_dict[number] = number_idx
            sum_counterpart = target - number

            if (sum_counterpart != number) and (sum_counterpart in num_dict):
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
            if idx == nums_len - 1:
                break
            elif idx == 0:
                results[idx] = 1
                results[idx + 1] = number
            else:
                results[idx + 1] = results[idx] * number

        last_idx = nums_len - 1
        reverse_idx = last_idx

        while reverse_idx > 0:
            try:
                if reverse_idx == last_idx:
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
            if idx == nums_len - 1:
                break
            elif idx == 0:
                results[0] = reverse_results[idx]
                continue
            else:
                results[idx] = results[idx] * reverse_results[idx]

        return results

    ##### 🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕

    # https://leetcode.com/problems/maximum-subarray/
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_sum = nums[0]
        current_sum = 0

        for number in nums:
            current_sum += number

            if current_sum > max_sum:
                max_sum = current_sum

            if current_sum < 0:
                current_sum = 0

        return max_sum

    ##### 🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕

    # https://leetcode.com/problems/maximum-product-subarray/
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) is 0:
            return 0

        max_product = None
        current_product = None
        current_product_len = 0
        product_until_first_negative = 1
        product_since_last_negative = 1

        for number in nums:
            if number == 0:
                if max_product is None:
                    max_product = 0

                if current_product is not None:
                    if current_product < 0 and current_product_len > 1:
                        current_product = current_product / max(product_since_last_negative, product_until_first_negative)

                    if max_product is None or current_product > max_product:
                        max_product = current_product

                current_product = None
                current_product_len = 0
                product_until_first_negative = 1
                product_since_last_negative = 1
                continue

            current_product_len += 1

            if current_product is None:
                current_product = number
            else:
                current_product *= number

            if number < 0:
                if product_until_first_negative > 0:
                    product_until_first_negative *= number

                product_since_last_negative = number
            else:
                if product_until_first_negative > 0:
                    product_until_first_negative *= number

                if product_since_last_negative < 0:
                    product_since_last_negative *= number

        if current_product is not None:
            if current_product < 0 and current_product_len > 1:
                current_product = current_product / max(product_since_last_negative, product_until_first_negative)

            if max_product is None or current_product > max_product:
                max_product = int(current_product)

        return max_product

