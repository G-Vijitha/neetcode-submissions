class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0
        for r in range(len(s)):
            # print("##############")
            # print("r: ", r)
            # print("mp: ", mp)
            # print("s[r]: ", s[r])
            if s[r] in mp:
                # print("l: ", l)
                # print("mp[s[r]], mp[s[r]]+1, l: ", mp[s[r]], mp[s[r]]+1, l)
                l = max(mp[s[r]]+1, l)
                # print("l1: ", l)
            mp[s[r]] =r
            # print("Newmp[s[r]]: ",mp[s[r]])
            # print("res,r,l: ",res,r)
            res = max(res, r-l+1)
            # print("res: ",res)
        return res        