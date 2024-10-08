# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        result = ''
        reversed_result = ''

        for ch in s:
            if ch.lower() in alphabet:
                result += ch.lower()
                reversed_result = ch.lower() + reversed_result

        return result == reversed_result

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while right > left:
            if not s[right].isalnum():
                right -= 1
                continue

            if not s[left].isalnum():
                left += 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            right -= 1
            left += 1

        return True


if __name__ == '__main__':
    s = Solution2()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("raceacar"))
    print(s.isPalindrome("0P"))

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#
# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters
