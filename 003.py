class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current = ""

        for char in s:
            if char in current:
                # If char repeats, cut the string after the previous char
                index = current.index(char)
                current = current[index + 1:]

            current += char
            longest = max(longest, len(current))

        return longest
