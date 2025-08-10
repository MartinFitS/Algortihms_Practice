# Two Sum

# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Use a dictionary (hash map) to store numbers and their indices.
# For each number, calculate the difference (target - current number).
# If the difference is already in the dictionary, return the stored index and the current index.
# Otherwise, store the current number and its index in the dictionary.
#
# Time complexity: O(N)
# Space complexity: O(N)

def twoSum(nums, target):
    container = {}

    for i , number in enumerate(nums):
        diff = target - number

        if diff in container:
            return[container[diff], i]
        else:
            container[number] = i

result = twoSum([3,4,5,6], 7)
print(result)
