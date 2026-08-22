class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If t is longer than s, it cannot fit
        if len(t) > len(s):
            return ""

        # Dictionary storing required character frequencies
        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        # Dictionary storing characters in the current window
        window = {}

        # Number of unique characters we need
        required = len(need)

        # Number of requirements currently satisfied
        have = 0

        # Left side of the sliding window
        left = 0

        # Store the best window length
        min_length = float("inf")

        # Store the starting index of the best window
        result_start = 0

        # Expand the window using right pointer
        for right in range(len(s)):

            # Character entering the window
            char = s[right]

            # Add it to the window count
            window[char] = window.get(char, 0) + 1

            # Check if this character has exactly reached
            # the frequency we need
            if char in need and window[char] == need[char]:
                have += 1

            # If the window contains everything required,
            # try shrinking it
            while have == required:

                # Calculate current window length
                window_length = right - left + 1

                # Update result if this window is smaller
                if window_length < min_length:

                    min_length = window_length
                    result_start = left

                # Character leaving the window
                left_char = s[left]

                # Remove it from the window
                window[left_char] -= 1

                # If we no longer have enough of this
                # required character, the window becomes invalid
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                # Move left pointer forward
                left += 1

        # If no valid window was found
        if min_length == float("inf"):
            return ""

        # Return the smallest window
        return s[result_start:result_start + min_length]