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
