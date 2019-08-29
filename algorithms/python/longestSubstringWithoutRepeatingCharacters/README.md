### 3. Longest Substring Without Repeating Characters
- 포인트
    - 겹치는게 나왔다고 리스트를 새로 만들면 안됨
    - 겹치는게 나왔을시 겹치는 index 부분부터 다시 substring개수를 세야함
    - 이를 위해서 [].index(<elm>) 함수가 필수임!

```
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

- my code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_of_substring = []
        max_substr_len = 0
        for s_elm in s:
            if len(list_of_substring) == 0:
                list_of_substring.append(s_elm)
            else:
                if s_elm in list_of_substring:
                    substr_len = len(list_of_substring)
                    if substr_len > max_substr_len:
                        max_substr_len = substr_len                    
                    pre_duplicated_index = list_of_substring.index(s_elm) # 필수
                    list_of_substring.append(s_elm)
                    list_of_substring = list_of_substring[pre_duplicated_index+1:]
                else:
                    list_of_substring.append(s_elm)

        substr_len = len(list_of_substring)
        if substr_len > max_substr_len:
            max_substr_len = substr_len
        return max_substr_len
```

- result
```
Success
Runtime: 100 ms, faster than 27.53% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.9 MB, less than 5.10% of Python3 online submissions for Longest Substring Without Repeating Characters.
```
