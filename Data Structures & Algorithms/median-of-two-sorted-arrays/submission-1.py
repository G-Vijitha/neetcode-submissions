class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Brute/binary O(m+n)/O(m+n)
        merge = []
        i = 0
        j = 0
        total = len(nums1) + len(nums2)
        # print("total, len(nums1),len(nums2), len(nums1) + len(nums2): ", total, len(nums1),len(nums2),len(nums1) + len(nums2))
        # print("len(merge),total//2, len(merge) <= total//2 : ",len(merge),total//2,len(merge) <= total//2)
        while len(merge) <= total//2:
            # print("##################################")
            # print("len(merge), total//2 : ", len(merge), total//2)
            # print("i,len(nums1), j, len(nums2), nums1[i], nums2[j]): ",i,len(nums1), j,len(nums2),nums1[i], nums2[j])
            # print("i < len(nums1) and (j == len(nums2) or nums1[i] < nums2[j]): ",i < len(nums1) and (j == len(nums2) or nums1[i] < nums2[j]))
            if i < len(nums1) and (j == len(nums2) or nums1[i] < nums2[j]):
                merge.append(nums1[i])
                # print("merge: ", merge)
                i+=1
            else:
                merge.append(nums2[j])
                # print("elsemerge: ", merge)
                j+=1
        if total % 2 == 1:
            return merge[-1]
        return (merge[-1] + merge[-2])/2

        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         merge.append(nums1[i])
        #         i+=1
        #     else:
        #         merge.append(nums2[j])
        #         j+=1
        # while i < len(nums1):
        #     merge.append(nums1[i])
        #     i+=1
        # while j < len(nums2):
        #     merge.append(nums2[j])
        #     j+=1
        # n= len(merge)

        # if n%2 == 1:
        #     return merge[n//2]
        # else:
        #     return (merge[n//2] + merge[n//2 - 1]) / 2