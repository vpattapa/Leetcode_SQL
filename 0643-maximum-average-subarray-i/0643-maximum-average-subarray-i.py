class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        max_initial_sum = sum(nums[:k])
        summed = max_initial_sum
        for i in range(len(nums)-k):
            summed = summed-nums[i]+nums[i+k]
            max_initial_sum = max(max_initial_sum, summed)
        return max_initial_sum/k


        