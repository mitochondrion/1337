from typing import Set, List, Dict
from functools import reduce

# See https://github.com/mitochondrion/LRUCache for leetcode LRUCache implementation

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # https://leetcode.com/problems/nth-digit/
    def findNthDigit(self, n: int) -> int:
        if n < 10: return n

        base = 1
        digits_per_num = 1
        remainder = n

        while True:
            nums_per_base = 9 * base
            digits_per_base = nums_per_base * digits_per_num

            if remainder <= digits_per_base:
                break
            else:
                remainder -= digits_per_base
                digits_per_num += 1
                base *= 10

        number = base + (remainder - 1) // (digits_per_num)
        digit = remainder % digits_per_num

        if digit == 0:
            digit = digits_per_num

        place = digits_per_num - digit
        answer = (number % 10**(place + 1)) // 10**place

        return answer

    ##### 🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕

    # https://leetcode.com/problems/longest-substring-without-repeating-characters/
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        current_len = 0
        begin_idx = 0

        # letters -> index
        seen = {}

        for idx, c in enumerate(s):
            current_len += 1

            if c in seen:
                seen_idx = seen[c]

                if seen_idx >= begin_idx:
                    current_len = idx - seen_idx
                    begin_idx = seen_idx + 1

            if current_len > max_len:
                max_len = current_len

            seen[c] = idx

        return max_len

    ##### 🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕

    # https://leetcode.com/problems/add-two-numbers/
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer_head = ListNode()
        answer = answer_head
        answer_head.val = l1.val + l2.val

        if answer.val > 9:
            answer.val += -10
            answer.next = ListNode(1)

        while l1.next or l2.next:
            next_val = 0

            if l1.next:
                l1 = l1.next
                next_val += l1.val

            if l2.next:
                l2 = l2.next
                next_val += l2.val

            if not answer.next:
                answer.next = ListNode(0)

            answer = answer.next
            answer.val += next_val

            if answer.val > 9:
                answer.val += -10
                answer.next = ListNode(1)

        return answer_head

    ##### 🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕

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
        if len(nums) == 0:
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

    ##### 🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕🔥⽕

    # https://leetcode.com/problems/permutations/
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        permutations = [nums]
        current_permutation = nums
        next_permutation = self._permute_next(current_permutation)

        while next_permutation != current_permutation:
            permutations.append(next_permutation)
            current_permutation = next_permutation
            next_permutation = self._permute_next(current_permutation)

        return permutations

    def _reverse_in_place(self, nums, begin_index, end_index):
        if end_index >= len(nums):
            end_index = len(nums) - 1

        if begin_index < 0:
            begin_index = 0

        while begin_index < end_index:
            begin_value = nums[begin_index]
            nums[begin_index] = nums[end_index]
            nums[end_index] = begin_value
            begin_index += 1
            end_index -= 1

    def _permute_next(self, current_permutation):
        next_permutation = current_permutation.copy()
        current_index = len(current_permutation) - 1

        # Find pivot: the lowest place that is not in greater than its next lowest place
        pivot_index = -1

        for index in range(len(current_permutation) - 1, 0, -1):
            if current_permutation[index] > current_permutation[index - 1]:
                pivot_index = index - 1
                break

        if pivot_index < 0:
            return next_permutation

        pivot_value = current_permutation[pivot_index]
        pivot_swap_index = -1
        pivot_swap_value = -1

        for index in range(len(current_permutation) - 1, 0, -1):
            if current_permutation[index] > pivot_value:
                pivot_swap_value = current_permutation[index]
                pivot_swap_index = index
                break

        # Swap pivot
        next_permutation[pivot_swap_index] = pivot_value
        next_permutation[pivot_index] = pivot_swap_value

        # Reverse everything after the pivot
        self._reverse_in_place(next_permutation, pivot_index + 1, len(next_permutation) - 1)

        return next_permutation


