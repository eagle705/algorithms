### 5. Longest Palindromic Substring
- 포인트
    - 홀수개와 짝수개일때를 나눠야함
    - 한개씩 증감하면서 찾는거니까 재귀로 해보자
    - max_len 체크하면서 그때의 index를 저장해서 리턴

```
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
```

- my code

```python
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
```

- result
```
Success
Runtime: 1832 ms, faster than 48.98% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.1 MB, less than 20.17% of Python3 online submissions for Longest Palindromic Substring.
```
