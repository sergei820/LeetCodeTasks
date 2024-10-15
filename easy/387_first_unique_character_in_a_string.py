class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}
        for i in range(len(s)):
            if letters.get(s[i]) is None:
                letters[s[i]] = 1
            else:
                letters[s[i]] += 1

        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i

        return -1


if __name__ == '__main__':
    s = Solution()
    # print(s.firstUniqChar('loveleetcode'))
    print(s.firstUniqChar('aabb'))  # -1

    # solution 1: set -> check union with s
    # solution 2:


# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.
#
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
#
# Example 3:
# Input: s = "aabb"
# Output: -1
#
# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.
