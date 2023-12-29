# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # intialize the K pointer at 0
        k = 0
        
        # iterate through every single value in the input array get the length of the input array nums
        for i in range(len(nums)):
            #if we see a input is not to the value then we preform the swap
            if nums[i] != val:
                # then we put it at position k in the input array
                nums[k] = nums[i]
                # increment by 1
                k += 1
        return k
    