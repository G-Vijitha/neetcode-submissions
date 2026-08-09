class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        # print("left,right: ", left,right)
        while left < right:
            # print("###########################")
            # print("left1,right1: ", left,right)
            mid = left +(right - left)//2
            # print("mid: ", mid)
            # print("nums[mid], nums[right]: ", nums[mid], nums[right])
            # print("nums[mid] > nums[right]: ", nums[mid] > nums[right])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        # mini = nums[0]
        # for num in nums:
        #     if num < mini:
        #         mini = num
        # return mini
        