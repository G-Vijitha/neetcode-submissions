class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "" :
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            # print("#############################")
            # print("left, rright: ", left, right)
            # print("left < right and not s[left].isalnum:", left < right and not s[left].isalnum())
            # print("left, right, s[left], s[left].isalnum():", left, right, s[left], s[left].isalnum())
            while left < right and not s[left].isalnum():
                # print("---------------------")
                left+=1
            # print("left, rright: ", left, right)
            # print("right > left and not s[right].isalnum():", right > left and not s[right].isalnum())
            # print("left, right, s[right], s[right].isalnum():", left, right, s[right], s[left].isalnum())
            while right > left and not s[right].isalnum():
                # print("+++++++++++++++++++++++++++")
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
