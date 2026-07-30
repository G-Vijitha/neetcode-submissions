class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countT = {} 
        countS = {}
        for i in s:
            countS[i]= countS.get(i,0)+1
        for j in t:
            countT[j]= countT.get(j,0)+1
        return countT == countS

        