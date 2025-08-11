# 88. Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, 
# nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set 
# to 0 and should be ignored. nums2 has a length of n.


def mergeTwoSortedArray(nums1, m, nums2, n):
    """
    Merges two sorted arrays (nums1 and nums2) into nums1 in-place.

    Parameters:
    nums1 (List[int]): First sorted array with extra space at the end to hold all elements.
    m (int): Number of valid elements in nums1.
    nums2 (List[int]): Second sorted array.
    n (int): Number of elements in nums2.

    Time Complexity:
    ----------------
    O(m + n) → Each element is visited at most once.

    Space Complexity:
    -----------------
    O(1) → No extra significant memory is used; merging is done in-place.
    """

    # Pointer to the last valid element in nums1
    last_position_valid_nums1 = m - 1
    # Pointer to the last element in nums2
    last_position_valid_nums2 = n - 1
    # Pointer to the last available index in nums1 (including extra zeros)
    last_position_nums1 = len(nums1) - 1

    # Merge from the back to avoid overwriting elements in nums1
    while last_position_valid_nums1 >= 0 and last_position_valid_nums2 >= 0:
        if nums1[last_position_valid_nums1] > nums2[last_position_valid_nums2]:
            nums1[last_position_nums1] = nums1[last_position_valid_nums1]
            last_position_valid_nums1 -= 1  # Move left in nums1
        else:
            nums1[last_position_nums1] = nums2[last_position_valid_nums2]
            last_position_valid_nums2 -= 1  # Move left in nums2
        
        last_position_nums1 -= 1  # Move left in nums1's available space

    # Copy any remaining elements from nums2 into nums1
    while last_position_valid_nums2 >= 0:
        nums1[last_position_nums1] = nums2[last_position_valid_nums2]
        last_position_valid_nums2 -= 1
        last_position_nums1 -= 1
    
    return nums1


# Example usage
result = mergeTwoSortedArray([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print(result)  # Expected output: [1, 2, 2, 3, 5, 6]
