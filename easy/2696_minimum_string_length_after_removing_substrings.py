class Solution:
    def minLength(self, s: str) -> int:
        s_copy = s
        for i in range(len(s_copy)//2):
            if 'AB' not in s_copy and 'CD' not in s_copy:
                break
            if "AB" in s_copy:
                s_copy = s_copy.replace('AB', '')
            if "CD" in s_copy:
                s_copy = s_copy.replace('CD', '')

        return len(s_copy)


if __name__ == '__main__':
    s = Solution()
    # print(s.minLength("ACBBD"))
    print(s.minLength("ABFCACDB"))


