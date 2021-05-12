import unittest
from leetcode import *


class Test(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(s.lengthOfLongestSubstring('pwwkew'), 3)
        self.assertEqual(s.lengthOfLongestSubstring('xabcdaexfga'), 8)
        self.assertEqual(s.lengthOfLongestSubstring('xxxxxxx'), 1)
        self.assertEqual(s.lengthOfLongestSubstring(''), 0)

    def test_addTwoNumbers(self):
        s = Solution()

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
        self.assertEqual(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(s.maxSubArray([-2,-1,-3,-4,-1,-2,-1,-5,-4]), -1)
        self.assertEqual(s.maxSubArray([-2]), -2)
        self.assertEqual(s.maxSubArray([]), 0)

    def test_maxProduct(self):
        s = Solution()
        self.assertEqual(s.maxProduct([]), 0)
        self.assertEqual(s.maxProduct([0]), 0)
        self.assertEqual(s.maxProduct([0,0]), 0)

        self.assertEqual(s.maxProduct([1]), 1)
        self.assertEqual(s.maxProduct([-1]), -1)
        self.assertEqual(s.maxProduct([1,1]), 1)
        self.assertEqual(s.maxProduct([-1,1]), 1)
        self.assertEqual(s.maxProduct([1,-1]), 1)
        self.assertEqual(s.maxProduct([-1,-1]), 1)
        self.assertEqual(s.maxProduct([1,1,1]), 1)
        self.assertEqual(s.maxProduct([-1,1,1]), 1)
        self.assertEqual(s.maxProduct([-1,-1,1]), 1)
        self.assertEqual(s.maxProduct([-1,-1,-1]), 1)
        self.assertEqual(s.maxProduct([1,-1,1]), 1)
        self.assertEqual(s.maxProduct([1,-1,-1]), 1)
        self.assertEqual(s.maxProduct([1,1,-1]), 1)

        self.assertEqual(s.maxProduct([-42]), -42)
        self.assertEqual(s.maxProduct([42]), 42)
        self.assertEqual(s.maxProduct([2,2]), 4)
        self.assertEqual(s.maxProduct([-2,2]), 2)
        self.assertEqual(s.maxProduct([2,-2]), 2)
        self.assertEqual(s.maxProduct([-2,-2]), 4)
        self.assertEqual(s.maxProduct([-2,-2,-3]), 6)
        self.assertEqual(s.maxProduct([-3,-2,-2]), 6)
        self.assertEqual(s.maxProduct([-3,-2,-3]), 6)
        self.assertEqual(s.maxProduct([-2,-3,-2]), 6)
        self.assertEqual(s.maxProduct([-2,-3,2]), 12)
        self.assertEqual(s.maxProduct([2,-3,-2]), 12)
        self.assertEqual(s.maxProduct([-2,2,-3]), 12)
        self.assertEqual(s.maxProduct([-3,2,-2]), 12)
        self.assertEqual(s.maxProduct([2,-2,3]), 3)
        self.assertEqual(s.maxProduct([3,-2,2]), 3)
        self.assertEqual(s.maxProduct([2,3,-2,2,4]), 8)
        self.assertEqual(s.maxProduct([2,4,-2,2,3]), 8)
        self.assertEqual(s.maxProduct([2,4,-2,2,-1]), 32)
        self.assertEqual(s.maxProduct([2,-2,-2,2]), 16)
        self.assertEqual(s.maxProduct([-2,-2,-2,-2]), 16)
        self.assertEqual(s.maxProduct([-2,2,-2,2]), 16)
        self.assertEqual(s.maxProduct([2,-2,-2,2]), 16)
        self.assertEqual(s.maxProduct([2,-2,2,-2,2]), 32)
        self.assertEqual(s.maxProduct([2,-2,2,-2,2,-2]), 32)
        self.assertEqual(s.maxProduct([-2,2,-2,2,-2,2]), 32)
        self.assertEqual(s.maxProduct([3,-2,2,-2,2,-2,2]), 48)

        self.assertEqual(s.maxProduct([0,1]), 1)
        self.assertEqual(s.maxProduct([1,0]), 1)
        self.assertEqual(s.maxProduct([0,-1]), 0)
        self.assertEqual(s.maxProduct([-1,0]), 0)
        self.assertEqual(s.maxProduct([1,0,-1]), 1)
        self.assertEqual(s.maxProduct([-1,0,1]), 1)
        self.assertEqual(s.maxProduct([-1,0,-1]), 0)
        self.assertEqual(s.maxProduct([1,0,1]), 1)
        self.assertEqual(s.maxProduct([-1,-1,0,-1]), 1)

        self.assertEqual(s.maxProduct([1,-5]), 1)
        self.assertEqual(s.maxProduct([-5,1]), 1)

        self.assertEqual(s.maxProduct([0,2,3,-2,2,4,0,1-2,3,2]), 8)


    def test_reverseInPlace(self):
        s = Solution()

        a = [1,2,3,4,5]
        s._reverse_in_place(a, 0, 4)

        self.assertEqual(a, [5,4,3,2,1])

        s._reverse_in_place(a, -3, 99)
        self.assertEqual(a, [1,2,3,4,5])

        s._reverse_in_place(a, 1, 3)
        self.assertEqual(a, [1,4,3,2,5])

        s._reverse_in_place(a, 1, 2)
        self.assertEqual(a, [1,3,4,2,5])

        s._reverse_in_place(a, 3, 2)
        self.assertEqual(a, [1,3,4,2,5])


    def test_permute(self):
        s = Solution()

        result = s.permute([2,1,3])
        expected = [
            [1,2,3],
            [1,3,2],
            [2,1,3],
            [2,3,1],
            [3,1,2],
            [3,2,1]
        ]

        self.assertEqual(result, expected)

        self.assertEqual(s.permute([]), [[]])
        self.assertEqual(s.permute([42]), [[42]])

if __name__ == '__main__':
    unittest.main()

