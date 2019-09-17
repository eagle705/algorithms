```
# 중복되면 안됨, 하지만 중복되는 원소가 순차적으로 2개 이상면 오케이

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

```python
# 처음엔 dict으로 해보려다가 그냥 loop 돌린 케이스
# Run time: 5400 ms	Mem: 14.7 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums[i+1:]):
                if (num_i + num_j) == target:
                    return [i, i+1+j]

```

```python
# 확실히 dict이 빠르긴 함
# Run time: 52 ms Mem: 16.5 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_to_list_of_idx = {}
        for i, num in enumerate(nums):
            if num not in num_to_list_of_idx:
                num_to_list_of_idx[num] = [i]
            else:
                num_to_list_of_idx[num].append(i)

        for i, num in enumerate(nums):
            diff = target-num
            if diff in num_to_list_of_idx:
                if num_to_list_of_idx[diff][-1] == i: # 같은 index면 패쓰
                    continue
                else:
                    return [i, num_to_list_of_idx[diff][-1]]
```
