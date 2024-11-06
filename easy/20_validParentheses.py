class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_dict = {')': '(', '}': '{', ']': '['}

        for bracket in s:
            if len(stack) == 0 and bracket in ')}]':
                return False
            if len(stack) == 0:
                stack.append(bracket)
                continue

            if bracket in brackets_dict.keys() and stack[-1] == brackets_dict[bracket]:
                stack.pop()
            else:
                stack.append(bracket)

            # if bracket == ')' and stack[-1] == '(':
            #     stack.pop()
            # elif bracket == ']' and stack[-1] == '[':
            #     stack.pop()
            # elif bracket == '}' and stack[-1] == '{':
            #     stack.pop()
            # else:
            #     stack.append(bracket)

        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))  # false
    print(s.isValid("([])"))

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Example 4:
# Input: s = "([])"
# Output: true
#
# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
