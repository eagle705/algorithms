# Largest Number At Least Twice of Others

## Task description
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

## Example: 1

```
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
```

## Example: 2

```
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
```

## Note:

```
- nums will have a length in the range [1, 50].
- Every nums[i] will be an integer in the range [0, 99].
```

## Solution

### Frist

- 250 / 250 test cases passed.
- Status: Accepted
- Runtime: 40 ms
- Memory Usage: 14 MB
- Link: https://leetcode.com/submissions/detail/270056328/

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:        
        # corner point 검사의 대표적인 예
        if len(nums) == 1: # other와 비교하는거니까 자기 자신은 제외
            return 0
        
        sorted_nums = sorted(nums)            
        if sorted_nums[-1] < sorted_nums[-2] * 2:
            return -1
        else:
            return nums.index(sorted_nums[-1])
        
```

## Comment
- corner point 봐야된다는걸 보여주는 대표적인예
- 정렬한 후, index를 뽑기때문에 시간복잡도 면에서는 손해볼수도..!
