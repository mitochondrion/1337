from unittest import TestCase
from leetcode import *


class Test(TestCase):
    def test_productExceptSelf(self):
        s = Solution()
        input = [1,2,3,4,5,6,7,8]
        result = s.productExceptSelf(input)
        naive_result = s.productExceptSelf_naive(input)
        expected_result = [40320, 20160, 13440, 10080, 8064, 6720, 5760, 5040]
        print('RESULT', result)
        print('EXPECTED', expected_result)
        self.assertEqual(result, naive_result)
        self.assertEqual(result, expected_result)

    def test_maxSubArray(self):
        s = Solution()
        input = []
        result = s.maxSubArray(input)
        expected_result = []
        self.assertEqual(result, expected_result)