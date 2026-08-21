class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target_count = {}
        window_count = {}
        for char in s1:
            if char in target_count:
                target_count[char] += 1
            else:
                target_count[char] = 1
        left = 0
        for right in range(len(s2)):
            char = s2[right]
            if char in window_count:
                window_count[char] += 1
            else:
                window_count[char] = 1
            if right - left + 1 > len(s1):
                left_char = s2[left]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    window_count.pop(left_char)
                left += 1
            if right - left + 1 == len(s1):
                if window_count == target_count:
                    return True
        return False