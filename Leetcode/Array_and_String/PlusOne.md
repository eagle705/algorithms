# Plus One

## Task description
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

## Example: 1

```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

## Example: 2

```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

## Note:

```
```

## Solution

### Frist

- 109 / 109 test cases passed.
- Status: Accepted
- Runtime: 32 ms
- Memory Usage: 13.6 MB
- Link: https://leetcode.com/submissions/detail/270072763/

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_index = len(digits) - 1
        while True:
            
            # if digits == [0]:
            #     return [1]
                        
            if digits[last_index] != 9:
                digits[last_index] += 1
                return digits                
            else:
                digits[last_index] = 0                
                last_index -= 1
                
            if last_index < 0:
                return [1] + digits
            
        return digits
```

## Comment
- corner point 봐야된다는걸 보여주는 대표적인예
- 정렬한 후, index를 뽑기때문에 시간복잡도 면에서는 손해볼수도..!
