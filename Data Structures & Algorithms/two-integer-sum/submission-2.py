class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashMap O(1)/O(n)
        seen = {}
        for i in range(len(nums)):
            required_number = target - nums[i]

            if required_number in seen:
                return [seen[required_number], i ]

            seen[nums[i]] = i

        # O(n2) / O(n)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        