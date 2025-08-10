# Top K Frequent Elements
#
# Given an integer array nums and an integer k,
# return the k most frequent elements in the array.
#
# Approach:
# 1. Count the frequency of each number using a dictionary.
# 2. Create buckets where index represents frequency,
#    and each bucket contains a list of numbers with that frequency.
# 3. Iterate over the buckets from highest frequency to lowest,
#    collecting numbers until we have k elements.
#
# Time Complexity: O(n)
#   - Counting frequencies takes O(n).
#   - Placing numbers into buckets takes O(n).
#   - Iterating buckets in reverse is O(n) in the worst case.
#
# Space Complexity: O(n)
#   - The frequency dictionary takes O(n).
#   - The buckets list takes O(n).


def topKFrequent(nums, k):
    freq = {}
    buckets = [[] for _ in range(len(nums)+ 1)]

    for number in nums:
        if number in freq:
            freq[number] += 1
        else:
            freq[number] = 1
        
    for number , freq in freq.items():
        buckets[freq].append(number)

    l_bucket = len(buckets) - 1
    result = []

    for i in range(l_bucket , 0 , -1):
        for number in buckets[i]:
            result.append(number)
            if len(result) == k:
                return result

result = topKFrequent([1,2,2,3,3,3], 2)
print(result)