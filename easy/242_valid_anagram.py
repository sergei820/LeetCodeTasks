class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1, word2 = s, t
        for letter in word1:
            if letter in word2:
                word2 = word2.replace(letter, '', 1)
            else:
                return False
        return len(word2) == 0


class FasterSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for letter in s:
            if not dict1.get(letter):
                dict1[letter] = 1
            else:
                dict1[letter] += 1
        for letter in t:
            if not dict2.get(letter):
                dict2[letter] = 1
            else:
                dict2[letter] += 1

        return dict1 == dict2


class ThirdSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        result_dict = {}

        for letter in s:
            if letter not in result_dict:
                result_dict[letter] = 0
            result_dict[letter] += 1

        for letter in t:
            if letter not in result_dict:
                return False
            else:
                result_dict[letter] -= 1
                if result_dict[letter] < 0:
                    return False

        return True


if __name__ == '__main__':
    s = ThirdSolution()
    print(s.isAnagram(s="anagram", t="nagaram"))  # Output: true
    print(s.isAnagram(s="rat", t="car"))  # Output: false


# Anagram
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# using all the original letters exactly once.

# Given two strings s and t, return true if t is an
# anagram
#  of s, and false otherwise.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
#
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
#
# Output: false
#
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
