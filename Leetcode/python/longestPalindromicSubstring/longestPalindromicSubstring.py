class Solution:
    def longestPalindrome(self, s: str) -> str:
        list_of_palindromic_str = []
        max_len = 0
        max_str = ""
        for i in range(len(s)):
            # 홀수개
            _i, _j = self.recursive_str_checker(s, i, i)
            _len = _j - _i + 1
            if _len > max_len:
                max_len = _len
                max_str = s[_i:_j+1]

            # 짝수개
            _i, _j = self.recursive_str_checker(s, i+1, i)
            _len = _j - _i + 1
            if _len > max_len:
                max_len = _len
                max_str = s[_i:_j+1]
        return max_str


    def recursive_str_checker(self, s, i, j):
        # length check
        if i == 0:
            return i, j
        if j == len(s)-1:
            return i, j

        if s[i-1] == s[j+1]:
            return self.recursive_str_checker(s, i-1, j+1)
        else:
            return i, j
