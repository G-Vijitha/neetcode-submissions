class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen[nums[i]] = i
        return False

        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False



        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        