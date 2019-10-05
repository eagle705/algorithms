# Reverse String
## Task description
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


## Examples

```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Solution

### Frist

* 478 / 478 test cases passed.
* Status: Accepted
* Runtime: 240 ms
* Memory Usage: 17.8 MB
* Link: https://leetcode.com/submissions/detail/266109142/

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while(True):
            if j <= i:
                break            
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
```

## Comment
- in-place, O(1)으로 풀라고해서 그냥 한번에 풀긴했는데, 과연 Recursive 단원에 맞게 풀었냐하면 Nope..
