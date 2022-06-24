# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return

# Drawing Board: take array input, check it is an array, take in target, check it is an int. Assume one solution exists
# Method 1, Brute Force: Check how the sum of the two integers add up with each successive two terms, i.e. add nums[0] + nums[1] == target, if false, nums[0] + nums[2], ...
# This method would use recursion to achieve its goal
# Method 2:

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = input('Please input an array of numbers: ')
        target = input('enter a target number: ')
        print(nums, target)

Solution.twoSum()