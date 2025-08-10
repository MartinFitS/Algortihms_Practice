# Contains Duplicate
#
# Given an integer array nums, return true if any value 
# appears more than once in the array; otherwise, return false.
#
# How to solve this problem:
#
# We can use a data structure known as a hash set, 
# which does not store duplicate values. 
# We iterate through the array, and for each number, 
# we check if it already exists in the hash set. 
# If it does, we return True. 
# If we finish the loop without finding duplicates, we return False.

# Time complexity : Big O(N)
# Space complexity : Big O(N)

def contains_duplicate(nums):
    # Initialize an empty hash set to store unique numbers
    container = set()

    # Iterate through each number in the list
    for number in nums:
        if number in container:
            # If the number already exists in the set, a duplicate was foun
            print("True")
            return True
        else:
            #Otherwise, add the number to the set
            container.add(number)
    #If no duplicates were found, return False
    print("False")
    return False

contains_duplicate([1,2,3,4,5,6,6])