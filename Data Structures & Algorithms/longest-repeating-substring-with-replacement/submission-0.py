class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        max_len = 0
        for right in range(len(s)):
            char = s[right]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            if count[char] > max_freq:
                max_freq = count[char]
            window_length = right - left + 1
            while window_length - max_freq > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
                window_length = right - left + 1
            if window_length > max_len:
                max_len = window_length
        return max_len
        