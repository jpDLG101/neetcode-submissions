class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        left = 1
        right = 1
        for i in range(n):
            output[i] *= left
            left *= nums[i]

            output[n - 1 - i] *= right
            right *= nums[n - 1 - i]

        return output