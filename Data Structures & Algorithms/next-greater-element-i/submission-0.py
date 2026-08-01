class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            idx = nums2.index(num)
            found = -1
            for j in range(idx+1, len(nums2)):
                if nums2[j] > nums2[idx]:
                    found = nums2[j]
                    break
            result.append(found)
        return result
        