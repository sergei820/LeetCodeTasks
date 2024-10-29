class SlowSolution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            if ransomNote[i] not in magazine:
                return False
            magazine = magazine.replace(ransomNote[i], '', 1)

        return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_dict = {}
        for i in range(len(magazine)):
            letters_dict[magazine[i]] = letters_dict.get(magazine[i], 0) + 1

        for i in range(len(ransomNote)):
            if letters_dict.get(ransomNote[i], 0) <= 0:
                return False
            letters_dict[ransomNote[i]] = letters_dict.get(ransomNote[i], 0) - 1

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct(ransomNote="a", magazine="b"))  # false
    print(s.canConstruct(ransomNote="aa", magazine="ab"))  # false
    print(s.canConstruct(ransomNote="aa", magazine="aab"))  # true

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed
# by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.
