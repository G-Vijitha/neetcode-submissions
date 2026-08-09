class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        # print("len(nums)", len(nums))
        right = len(nums)-1
        # print("left, right: ", left, right)
        while left <= right:
            # print("###################")
            # print("left1, right1: ", left, right)
            mid = left + (right - left)//2
            # print("mid: ", mid)
            # print("nums[mid],target: ", nums[mid],target)
            # print("nums[mid] == target: ", nums[mid] == target)
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # print("nums[left], nums[mid]: ", nums[left], nums[mid])
            # print("nums[left] <= nums[mid]: ", nums[left] <= nums[mid])
            elif nums[left] <= nums[mid]:
                # print("nums[left], target, nums[mid] ", nums[left],target, nums[mid])
                # print("nums[left] <= target < nums[mid] ", nums[left] <= target<nums[mid])
                if nums[left] <= target < nums[mid]:
                    # print("beforeRi : ",right)
                    right = mid -1
                    # print("After Ri : ",right)
                else:
                    # print("belefyi : ",left)
                    left = mid + 1
                    # print("afterlefyi : ",left)
            else:
                # print("nums[mid],nums[target],nums[right]: ",nums[mid],nums[target],nums[right])
                # print("nums[mid] < nums[target] <= nums[right]: ",nums[mid] < nums[target] <= nums[right])
                if nums[mid] < target <= nums[right]:
                    # print("InsideELDEbeforelefyi : ",left)
                    left = mid + 1
                    # print("InsideELDEafterlefyi : ",left)
                else:
                    # print("InsideELDEbeforeRight : ",right)
                    right = mid - 1
                    # print("InsideELDEafterRight : ",right)
        return False






        # for i in range(0,len(nums)):
        #     if nums[i] == target:
        #         return True
        # return False
        