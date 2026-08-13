class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # print("len(strs[0]): ", len(strs[0]))
        for i in range(len(strs[0])):
            # print("######################################")
            # print("i: ", i)
            for s in strs:
                # print("------------------------------------------")
                # print("s: ", s)
                # print("i,len(s),s[i],strs[0][i]: ", i ,len(s), s[i], strs[0][i])
                # print("i == len(s), s[i] != strs[0][i]: ", i == len(s) , s[i] != strs[0][i])
                # print("i == len(s) or s[i] != strs[0][i]: ", i == len(s) or s[i]!=strs[0][i])
                if i == len(s) or s[i] != strs[0][i]:
                    # print("s[:i]: ",s[:i])
                    return s[:i]
        # print("strs[0]]: ",strs[0])
        return strs[0]
        