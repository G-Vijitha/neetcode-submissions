class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # print("res, nums: ", res, nums)
        nums.sort()
        # print("sortednums: ", nums)
        for i in range(len(nums)):
            # print("i , len(nums): ",i, len(nums))
            # print("*******************")
            # print("i,nums[i],nums[i-1]:",i,nums[i],nums[i-1])
            # print("i > 0 and nums[i] == nums[i-1]:",i > 0 and nums[i] == nums[i-1])
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # print("left, right: ", left, right)
                # print("-----------------------------")
                # print("nums[i],nums[left],nums[right]: ",nums[i],nums[left],nums[right])
                total = nums[i] + nums[left] + nums[right]
                # print("total: ", total)
                if total == 0:
                    # print("RES: ", res)
                    res.append([nums[i], nums[left],nums[right]])
                    # print("afterRES: ", res)
                    left += 1
                    right -= 1
                    # print("l,r: ", left, right)
                    # print("left,right, nums[left] , nums[left-1]: ", left,right, nums[left],nums[left-1])
                    # print("left < right and nums[left] == nums[left-1]: ",left < right and nums[left]==nums[left-1])
                    while left < right and nums[left] == nums[left-1]:
                        # print("###############################")
                        # print("left,right, nums[left] , nums[left-1]: ", left,right, nums[left],nums[left-1])
                        # print("left < right and nums[left] == nums[left-1]: ", left < right and nums[left] == nums[left-1])
                        left += 1
                    # print("left,right, nums[right] , nums[right+1]: ", left,right, nums[right],nums[right+1])
                    # print("left < right and nums[right] == nums[right+1]: ", left < right and nums[right] == nums[right+1])
                    while left < right and nums[right] == nums[right+1]:
                        # print("++++++++++++++++++++++++++++++++")
                        # print("left,right, nums[right] , nums[right+1]: ", left,right, nums[right],nums[right+1])
                        # print("left < right and nums[right] == nums[right+1]: ", left < right and nums[right] == nums[right+1])
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res

        