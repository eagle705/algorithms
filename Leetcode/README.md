# Leetcode



## Lessons

* Recursive
    - [ReverseString](./Recursive/ReverseString.md)
    - [SwapNodesinPairs](./Recursive/SwapNodesinPairs.md)
* Arrays
    - [OddOccurrencesInArray](./OddOccurrencesInArray.md)


| # | Title | Solution | Difficulty |
|---| ----- | -------- | ---------- |
|8|[String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)| [Python](./algorithms/python/stringToInteger)|Medium|
|6|[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)| [Python](./algorithms/python/zigZagConversion)|Medium|
|5|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)| [Python](./algorithms/python/longestPalindromicSubstring)|Medium|
|3|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)| [Python](./algorithms/python/longestSubstringWithoutRepeatingCharacters)|Medium|
|2|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)| [Python](./algorithms/python/addTwoNumbers)|Medium|
|1|[Two Sum](https://leetcode.com/problems/two-sum/)| [Python](./algorithms/python/twoSum)|Easy|

## 다시 풀 문제
- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- https://leetcode.com/problems/rotate-image/
-

----------
## Leetcode

### 1. Two Sum, Example (Easy)

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


### 2. Add Two Numbers
- 포인트
    - 다음 node의 pointer를 넘겨주고, 재귀적으로 호출
    - None 값 체크해서, 바로 포인터 접근하지말고 변수로 바꿔서 사용
        - None 값 있는 노드느 새로 잘 만들어주고
    - None 체크등은 if문 inline에서 끝내는게 보기 편한듯
    - 경우의 수에 대한 분기 잘 짤라주고
        - 지금처럼 코드 짰을땐 일반화하기 힘들거같으니 일반화하는 방법 고민해봐야함

```
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

- my code

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_val = 0 if l1 is None else l1.val
        l2_val = 0 if l2 is None else l2.val
        val = l1_val + l2_val
        if val >= 10: # if one of l1, l2 is None, Never come here
            val = val - 10
            result_node = ListNode(val)  
            if l1.next is None and l2.next is None:
                result_node.next = ListNode(1)
            elif l1.next is None:
                result_node.next = self.addTwoNumbers(ListNode(1), l2.next)
            elif l2.next is None:
                result_node.next = self.addTwoNumbers(l1.next, ListNode(1))
            else:            
                l1.next.val = l1.next.val + 1
                result_node.next = self.addTwoNumbers(l1.next, l2.next)            
        else:
            result_node = ListNode(val)

            if l1.next is None and l2.next is None:
                return result_node
            elif l1.next is None:
                result_node.next = l2.next
            elif l2.next is None:
                result_node.next = l1.next
            else:            
                result_node.next = self.addTwoNumbers(l1.next, l2.next)

        return result_node
```

- result
```
Success
Runtime: 72 ms, faster than 92.18% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.6 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
```

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

### 6. ZigZag Conversion
- 포인트
    - 각 row가 증가했다가 감소하고 있는걸 이용하자
    - row에 대응되는 리스트에 넣기 위해 index를 증가하면서 넣다가 양 끝단에 도착하면 다시 감소시키기만 하면됨
    - 증감을 위한 flag 변수를 넣고 str len에 맞게 입력해주고 나중에 concat해서 뱉어주자

```
Given a string s, find the longest palindromic The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

- my code

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list_of_list_row_chars = ["" for _ in range(numRows)]

        j = 0
        plus_minus_multiplier = -1
        for i in range(len(s)):            
            list_of_list_row_chars[j] += s[i]
            if j == numRows - 1 or j == 0:
                plus_minus_multiplier = plus_minus_multiplier * -1                
            if numRows != 1: # 예외처리..!
                j = j + 1 * plus_minus_multiplier

        result_str = ""
        for row in list_of_list_row_chars:
            result_str += row            
        return result_str
```

- result
```
Success
Runtime: 68 ms, faster than 62.89% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 13.9 MB, less than 10.00% of Python3 online submissions for ZigZag Conversion.
```

### 8. String to Integer (atoi)
- 포인트
    - 정규식으로 처리하면 그냥 한방에 끝..
    - 숫자들을 리스트에 넣어놓고.. 처리
    - 예외처리 중요함
    - 더 나은 풀이 있을 것 -_ -;

```
String to Integer (atoi)
Medium

1060

6628

Favorite

Share
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−2^31) is returned.
```

- my code

```python
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MIN = -1 * pow(2, 31)
        INT_MAX = 1 * pow(2, 31) - 1
        number_str_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        number_and_ops_str_list = number_str_list + ["+", "-"]
        str = str.strip()
        if str == "":
            return 0

        if str[0] not in number_and_ops_str_list or str == "+" or str == "-":
            return 0
        else:
            result_str = ""
            for i, str_elm in enumerate(str):
                if i != 0 and str_elm not in number_str_list:
                    break
                result_str += str_elm
            if len(result_str) == 1 and result_str not in number_str_list:
                return 0
            else:
                result_str = int(result_str)
                if result_str >= INT_MAX:
                    return INT_MAX
                elif result_str <= INT_MIN:
                    return INT_MIN
                else:
                    return result_str                
```

- result
```
Success
Runtime: 40 ms, faster than 74.91% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.1 MB, less than 5.95% of Python3 online submissions for String to Integer (atoi).
```

### 11. Container With Most Water
- https://leetcode.com/problems/container-with-most-water/
- 포인트
    - n^2 이 안되도록 양 옆에서 조여오는 방식으로 코딩
    - 양 옆에서 조여올때는 특정 조건이 되었을때 index를 이동하도록!
    - index간의 갭이 1밖에 안되기 때문에 정수 환경에서 height가 1이라도 크면 index를 옮기는게 이득임

```
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.



Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

- my code

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_cont_size = 0
        total_len = len(height)
        i = 0        
        j = total_len - i - 1

        # if i+1 == j: #len of height == 2
        #     if height[i] > height[j]:
        #         max_cont_size = height[j] * (j - i)
        #     else:
        #         max_cont_size = height[i] * (j - i)

        while(i+1 <= j):                        
            if height[i] > height[j]:
                cont_size = height[j] * (j - i)
                j = j - 1
            else:
                cont_size = height[i] * (j - i)
                i = i + 1
            if cont_size > max_cont_size:
                max_cont_size = cont_size

        return max_cont_size

```

- result
```
Success
Runtime: 140 ms
Memory Usage: 15.5 MB
```

### 15. 3Sum
- https://leetcode.com/problems/3sum/
- 포인트
    - n^2 이 안되도록 양 옆에서 조여오는 방식으로 코딩
    - 간단하게 sorting하고 시작 (좀 시간 복잡도 손해봐도 -> 손해봐도 nlogn 정도임)
    - 정렬이 되어있으니 특정 조건에 맞게 i,j,k index 옮겨주면서 체크
    - 같은 elm의 경우는 if 문 처리로 빠르게 break로 끊어줘야    


```
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

- my code (이건 참고함)

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        length_nums = len(nums)
        for i in range(len(nums)-2):
            if nums[i]>0:  # 이게 속도에 꽤 중요함1
                break #[7]
            if i>0 and nums[i]==nums[i-1]: # 이게 속도에 꽤 중요함2
                continue #[1]

            j = i+1
            k = length_nums - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    # if (nums[i], nums[j], nums[k]) not in res: #  이게 속도 4배 잡아먹음
                    res.append((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res

```

- result
```
Success
Runtime: 704 ms, faster than 89.65% of Python3 online submissions for 3Sum.
Memory Usage: 16.8 MB, less than 57.14% of Python3 online submissions for 3Sum.
Next challenges:
```


### 17. Letter Combinations of a Phone Number
- https://leetcode.com/problems/letter-combinations-of-a-phone-number/
- 포인트
    - dict으로 필요한거 저장해놓고
    - 재귀적으로 펼쳐지는 트리를 기억하고
    - return 하면 for loop 끝나니, list에 담아서 한꺼번에 리턴해주고
    - 재귀를 받는 쪽에선 extend로 새로운 list를 계속 추가해준다    

```
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
```

- my code

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.number_to_letter = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r", "s"],
            "8": ["t","u","v"],
            "9": ["w","x","y", "z"]
        }

        return self.recursive_letter_converter(digits)

    def recursive_letter_converter(self, digits: str, result: str=""):

        list_of_result = []
        if len(digits) == 0:
            return []
        list_of_letter = self.number_to_letter[digits[0]]
        for letter in list_of_letter:                        
            if len(digits) > 1:                                
                list_of_result.extend(self.recursive_letter_converter(digits[1:], result + letter))
            else: # len(digits) == 1
                list_of_result.append(result + letter)
        return list_of_result
```

- result
```
Success
Runtime: 40 ms, faster than 38.73% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.9 MB, less than 5.88% of Python3 online submissions for Letter Combinations of a Phone Number.
```



### 19. Remove Nth Node From End of List
- https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- 포인트
    - 재귀로 포인트 잡아서 마지막 노드일때 기준을 잡고, 리턴될때를 기준을 잡음
    - 링크드 리스트에서 남은 노드 개수랑, 포인터 자체를 넘겨

```
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
```

- my code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        head, _ = self.get_new_head(head, n)
        return head

    def get_new_head(self, head, n):


        if head is None:
            return None, n-1        
        else:
            _head, n = self.get_new_head(head.next, n)

            if n == 1:            
                return head, n-1
            elif n == -1:            
                head.next = _head
                return head, n
            else:
                return _head, n-1
```

- result
```
Success
Runtime: 48 ms, faster than 7.81% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.9 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.
```


### 49. Group Anagrams

```
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
```

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_to_list = {}
        for _str in strs:
            list_of_str = list(_str)
            list_of_str.sort() # 문자열도 오름 차순으로 정렬이 됨!
            set_of_str = "".join(list_of_str)
            if set_of_str in anagrams_to_list:
                anagrams_to_list[set_of_str].append(_str)
            else:
                anagrams_to_list[set_of_str] = [_str]
        return list(anagrams_to_list.values())

# set으로 하면 글자 개수 차이나는건 못잡음
```


### 347. Top K Frequent Elements

```
Given a non-empty array of integers, return the k most frequent elements.

Example:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

Note:

- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
```

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import operator
        i = 0
        res = []        
        num_to_count = {}
        for num in nums:
            if num in num_to_count:
                num_to_count[num] += 1
            else:
                num_to_count[num] = 1
        
        num_to_count = sorted(num_to_count.items(), key=operator.itemgetter(1), reverse=True)
        
        for num, count in num_to_count:
            i += 1
            if i > k:
                break
            res.append(num)        
        return res
        
# --- Solution --- #
"""
The second step is to build a heap. The time complexity of adding an element in a heap is \mathcal{O}(\log(k))O(log(k)) and we do it N times that means \mathcal{O}(N \log(k))O(Nlog(k)) time complexity for this step.

The last step to build an output list has
\mathcal{O}(k \log(k))O(klog(k)) time complexity.

In Python there is a method nlargest in heapq library (check here the source code) which has the same \mathcal{O}(k \log(k))O(klog(k)) time complexity and combines two last steps in one line.
"""


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 

            
```

```
Runtime: 100 ms, faster than 98.75% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 17.4 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
```

### 300. Longest Increasing Subsequence (LIS)

```
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

- There may be more than one LIS combination, it is only necessary for you to return the length.
- Your algorithm should run in O(n^2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
```

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        
        # return self.naive_LIS(nums)
        return self.dp_LIS(nums)
                
    def naive_LIS(self, nums):
        import itertools                
        for length in range(len(nums), 0, -1):
            c = itertools.combinations(nums, length)
            for combination_case in c:                
                if list(combination_case) == sorted(set(combination_case)): # 같은걸 포함하냐 안하냐는 여기서 결정
                    return length            
                
    def dp_LIS(self, nums):
        L = [1] * len(nums) # 현재 index까지의 최장 증가 수열 길이
        
        for cur, val in enumerate(nums):
            for pre in range(cur):
                if nums[pre] < val: # 같은걸 포함하냐 안하냐는 여기서 결정                   
                    L[cur] = max(L[cur], 1 + L[pre]) # L[cur]을 계속 업데이트함

        # LIS print
        # res = []
        # prev = L[0]
        # prev_idx = 0
        # for i, l in enumerate(L):
        #     if l > prev:
        #         if res == []:
        #                 res.append(nums[prev_idx])
        #                 res.append(nums[i])
        #         else:
        #             res.append(nums[i])
        #     prev = l
        #     prev_idx = i            
        # print(res)      
        
        return max(L)
        
# --- Solution --- #            
```

```
Runtime: 1028 ms, faster than 48.98% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Increasing Subsequence.
```

### 334. Increasing Triplet Subsequence
- bisect algorithm(이진탐색, 이미 정렬된 리스트를 활용, 삽입하면서 정렬하면 이 검색쓸수있음)을 이용해서 LIS만 뽑아내는게 사실상 naive, dp, bisect 중에서 제일 빠름 
- 비어있는 리스트에 삽입하며, 구간 내에서 있어야 할곳으로 삽입하되, 대체가능한 요소들은 대체해서 입력하는 방식
- bisect와 bisect_right은 같은거고 반대되는게 bisect_left임
    - bisect 모듈설명
        - 주어진 리스트 a와 값 x 가 있을 때, x 가 위치해야 할 인덱스를 구하는 함수
        - 그리고 같은 조건에서 값 x를 올바른 위치에 삽입하는 함수
- ref: https://m.blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221389084876&proxyReferer=https%3A%2F%2Fwww.google.com%2F
- ref: https://soooprmx.com/archives/8722
- 이진 탐색 모듈 자체는, 일단 값이 겹치게 되면 hi에서 들고 있게됨, lo == hi가 되는순간 hi에 갖고 있는 값이 lo에도 갖고 있을 수 있게되니 리턴됨

```python
def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect_left(mylist, 3))
```


```
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
```

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        from bisect import bisect_left        
        res = []
        for val in nums:
            
            idx = bisect_left(res, val) # return index to insert val into arr
            if idx == len(res):
                res.append(val)
            else:                
                res[idx] = val
            
            if len(res) == 3:
                return True
        else:
            return False
# --- Solution --- #            
```

```
Runtime: 52 ms, faster than 97.18% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 13.4 MB, less than 88.89% of Python3 online submissions for Increasing Triplet Subsequence.
```


### 395. Longest Substring with At Least K Repeating Characters
- 재귀로 풀어야함.. 재귀로 쪼개서 각 substring이 조건 만족하는지 보고, 만족하는 경우에 리턴하고, 리턴된애들중에서 가장 길이가 큰애들만 저장해가면서 업데이트하면되고 (업데이트 조건이 늘 어렵단말야..)
- Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

```
Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
```

```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        if len(s) < k:
            return 0
        
        if k < 2:
            return len(s)
        
        from collections import Counter
        counter = Counter(s)
        
        partitions = []
        left = 0
        for right in range(len(s)):
            if counter[s[right]] < k:
                substring = s[left:right]
                partitions.append(substring)
                left = right+1
        partitions.append(s[left:])
        
        if len(partitions) == 1:
            return len(partitions[0])
        
        res = 0
        for part_elm in partitions:
            res = max(res, self.longestSubstring(part_elm, k))
            
        return res
```

```
Runtime: 24 ms, faster than 99.59% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
```

### 131. Palindrome Partitioning
- 전형적인 dfs 문제였음
- Given a string s, partition s such that every substring of the partition is a palindrome.
- Return all possible palindrome partitioning of s.



```
Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
```

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.res = []
    
        def dfs(word, chuncks): # 새로 들어오는애는 짤라서 들어오는 애라, 0부터 새로들어온애의 길이에 대한 i 값으로 시작

            if len(word) == 0: # 다 가면 저장해놓고, 종료조건임~!
                self.res.append(chuncks[:]) # deep copy도 중요했고~
                # print(chuncks)                

            for i in range(1, len(word)+1):
                sliced = word[0:i]
                if sliced != sliced[::-1]:
                    continue

                chuncks.append(sliced) # 끝까지 갔다가
                dfs(word[i:], chuncks)
                chuncks.pop() # 다 가면 한개씩 다시 빼서 스택정리~ (스택은 가는 길을 저장해놓는것일뿐)
        dfs(s, [])

        return self.res
```

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []        
        def dfs(word, list_of_path):
            
            if len(word) == 0:
                self.res.append(list_of_path[:])
                # print(self.res)
            
            for i in range(1, len(word)+1):
                sliced = word[0:i]
                if is_pal(sliced):
                    list_of_path.append(sliced)
                    dfs(word[i:], list_of_path)
                    list_of_path.pop()
                else:
                    continue
        
        dfs(s, [])
        return self.res
        
def is_pal(s: str):
    if s == s[::-1]: return True
    else: return False
```

```
Runtime: 72 ms, faster than 91.89% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Palindrome Partitioning.
```

### 139. Word Break
- 전형적인 dp 문제였음
- Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.



```
Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)        
        
        for i in range(0, len(s)):            
            for word in wordDict:
                # 마지막은 스타트 조건임, dp의 True 위치에 따라 많은 조합이 가능함(이전에 체크했던)
                if word in s[i-(len(word)-1):i+1] and (dp[i-len(word)] is True or i-len(word)==-1):
                    dp[i] = True
                    
        # print(dp)
        return dp[-1]
                        
```


```
Runtime: 32 ms, faster than 97.51% of Python3 online submissions for Word Break.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Word Break.
```