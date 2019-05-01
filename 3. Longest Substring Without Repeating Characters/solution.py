class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        end = 0
        maxValue = 0
        for i, value in enumerate(s):
            if i == 0:
                maxValue = 1
            else:
                if value in s[end:i]:
                    end = s[end:i].index(value) + end + 1
                if maxValue < (i - end + 1):
                    maxValue = i - end + 1
        return maxValue


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("") == 0
    assert Solution().lengthOfLongestSubstring(" ") == 1
