# Find Pivot Index

## Task description
Given an array of integers ```nums```, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

## Example: 1

```
Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
```

## Example: 2

```
Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
```

## Note:

```
- The length of nums will be in the range [0, 10000].
- Each element nums[i] will be an integer in the range [-1000, 1000].
```

## Solution

### Frist
- 741 / 741 test cases passed.
- Status: Accepted
- Runtime: 200 ms
- Memory Usage: 14.9 MB
- Link: https://leetcode.com/submissions/detail/270049516/

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefix_sum = [nums[0]] # if input == [] -> error
        # for num in nums[1:]:        
        #     prefix_sum.append(prefix_sum[-1] + num)        
        prefix_sum = 0
        list_of_prefix_sum = []
        for num in nums:
            prefix_sum += num
            list_of_prefix_sum.append(prefix_sum)
                    
        total_sum = prefix_sum #list_of_prefix_sum[-1]
        for i, left_sum in enumerate(list_of_prefix_sum):
            if left_sum-nums[i] == (total_sum-left_sum):
                return i
        return -1

# print("testCase: ")
# print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
        
```

## Comment
- testcase중에 input이 []인게 있다. 그냥 맨처음처럼 prefix_sum 편하게 구하겠다고 index를 몇개 하드코딩으로 박아주는순간 훅가는거다.. 차라리 그냥 귀찮아도 tmp 변수하나 선언해서하자
