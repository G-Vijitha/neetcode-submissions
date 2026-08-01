class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nxt_grt = {}
        for num in nums2:
            # print("num", num)
            # print("stack: , nxt_grt: ", stack, nxt_grt)
            
            while stack and num > stack[-1]:
                # print("stack[-1]", stack[-1])
                smaller = stack.pop()
                # print("smaller", smaller)
                # print("nxtGRT", nxt_grt)
                nxt_grt[smaller] = num
                # print("nxt_grt[smaller]", nxt_grt[smaller])
                # print("stack2: ", stack)
            stack.append(num)
            # print("stck: ",stack)
        while stack:
            num = stack.pop()
            # print("2ndwhielNUm: ", num)
            nxt_grt[num] = -1
            # print("nxtGRT 2 : ", nxt_grt)
        res = []
        for num in nums1:
            # print("num in 2ndwhile: ", num)
            # print("res: ", res)
            # print("nxt_grt3:  ", nxt_grt)
            # print("nxt_grt[num]: ", nxt_grt[num])
            res.append(nxt_grt[num])
            # print("res2: ", res)
        return res













        # result = []
        # for num in nums1:
        #     idx = nums2.index(num)
        #     found = -1
        #     for j in range(idx+1, len(nums2)):
        #         if nums2[j] > nums2[idx]:
        #             found = nums2[j]
        #             break
        #     result.append(found)
        # return result
        