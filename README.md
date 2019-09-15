Algorithm
========

### Algorithm
leetcode & codility 가 좋다는 주변의 얘기를 듣고 바로 시작하게 되서 만든 Repository
- 계획: 일단 1일 1문제 풀기?!
- 목표: 중급은 꼭 다 풀수있어야함 :)

| # | Title | Solution | Difficulty |
|---| ----- | -------- | ---------- |
|8|[String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)| [Python](./algorithms/python/stringToInteger)|Medium|
|6|[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)| [Python](./algorithms/python/zigZagConversion)|Medium|
|5|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)| [Python](./algorithms/python/longestPalindromicSubstring)|Medium|
|3|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)| [Python](./algorithms/python/longestSubstringWithoutRepeatingCharacters)|Medium|
|2|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)| [Python](./algorithms/python/addTwoNumbers)|Medium|
|1|[Two Sum](https://leetcode.com/problems/two-sum/)| [Python](./algorithms/python/twoSum)|Easy|

### 다시 풀 문제
- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- https://leetcode.com/problems/rotate-image/
- 

### Coding Tips
- List.index도 좋지만 List.find가 더 편하다 index가 없을 경우에 -1 리턴하기 때문
- 속도가 우선이면 메모리를 좀 낭비해도 dict으로 코딩하자
- 제곱승은 pow(2, 31)도 되고 2**31도 된다
- None Error가 날 수 있는건 inline if 구문으로 다른변수로 바꾸자
- for loop의 경우 처음과 끝 index를 매우 신경 써라
- n^2이 아닌 방법으로 풀 수 있는 것들을 고민!
  - 양쪽에서 조여오는 경우나
  - BST 같이 mid를 쪼개서 탐색한다든지..!
- 작은 경우의수부터 생각하고 빠르게 브레인스토밍해야
- 어떤 문제들은 그냥 sort 한다음에 푸는게 시간복잡도가 좀 손해봐도 잘풀리는것들이 있음
- 간단한 if 예외처리가 속도를 빠르게함
- if ```elm``` in ```dict or list``` 식의 문법은 경우에 따라서 속도를 4배나 느려지게함
- 수학문제 풀때처럼 빠르게 생각! 틀에서 약간 벗어난 수학문제일때가 많지만
- in-place 문제의 경우 파이썬은 inline에서 여러 객체 대입이 가능하니까 이 특징을 사용하자
- https://www.youtube.com/watch?v=iGFnsuMeUQY
- https://www.youtube.com/user/damazzang/videos
- 코딩테스트 가이드: https://baactree.tistory.com/52
- http://blog.samstdio.com/coding-test/
- https://www.notion.so/580c3a42f21b49b497b7089f539a9f78

### Python Tips
- sort(), reverse() -> 이런건 객체를 반환하지 않음, sort는 기본적으로 오름차순
- reversed 같은 식으로 하면 객체를 반환하지만 reversed 객체로 나오기때문에 list로 형변환 해줘야함
- / : 나누기(소수점도 나옴), %: 나머지(떨어지는 나머지), //: 몫(곱해지는 텀)
- [12. 얕은 복사(shallow copy)와 깊은 복사(deep copy)](https://wikidocs.net/16038)
- [29. 변수 scope](https://wikidocs.net/16055)
- [44. class 정리 - 정적메소드 @classmethod와 @staticmethod의 정리](https://wikidocs.net/16074)
- (Combination을 위한 itertools)[https://www.geeksforgeeks.org/itertools-combinations-module-python-print-possible-combinations/]
- 숫자 -> 이진법 바꾸기 
  - format(32, "b"): '100000'
- 이진법 -> 숫자로 바꾸기
  - int('100000', 2): 32
- unpaired 경우는 if count % 2 == 0 로 2로 나누어 떨어지는지 아닌지로 체크!
- shift 문제의 경우, % 를 이용해서 나누기를 통해 length를 넘어가는 인덱스를 관리한다
- 나누기(/)나 나머지(%) 구하거나, 몫(//)을 구하는 경우 앞에 텀에 괄호 쳐주자
- for loop 두번 돌지말고 한번만 돌게끔.. 전체 합구해놓고 각 loop에서 처리해준다든지.. 이런식으로 가자 2*O(N)이 O(N^2) 보단 낫다
- 원소 확인할때는 list 에 append해서 if in으로 하지말고 set() .add로 해서 확인하는게 훨씨인 빠름
- [파이썬 내장함수 TimeComplexity 참고](https://wiki.python.org/moin/TimeComplexity), 보면 같은 x in s라도 list와 set은 복잡도가 다르고, 리스트의 경우 새로 생성하는거 자체가 O(n)임.. 굳이 생성안해도 되는거면 if로 비교하는게 훨씬 나음!
- list -> set 바꾸는것도 time complexity n 들어감
- 나누어 떨어지는 수 개수 세는 문제 같은 경우는 for loop 돌리지 말고 그냥 / 나 // 연산자로 몫 개수 세고 n mod k == 0인 경우 n 이 0인 경우도 고려해야하니 주의할 것!
- itertools의 경우 yield로 반환하기 때문에 list로 감싸는것과 안감싸는게 차이가 좀많이 남 ```for _ in itertools.combinations(range(length), 3):``` [문서 참고](https://docs.python.org/2/library/itertools.html#itertools.combinations) 
- O(N**2)를 O(N)으로 풀려면 수학적인 센스가 있어야되는 문제들이 몇개 있음 
- stack 문제를 풀때는 마지막에 스택에 값이 남아있는지와, 스택에 값이 없는데 pop 하려고하는때 이 두 가지에 대해서 예외처리 해줘야함
- pop은 왠만하면 바로 쓰지말고, [-1]로 인덱싱해서 쓰다가 조건이 딱 맞춰졌을때 pop으로 빼라 안 그러면 arr_length 때문에 while등에서 조건으로 쓸 경우 에러날 수 있음.. while문에서 쓰는 조건은 간단하게 하고, 차라리 True로 주고 안의 if 문으로 break 거는 처리를 하는게 더 편할 수 있음!
- O(N)을 여러번 하는게 loop 안에서 한번 더 리스트 탐색해서 O(N**2) 만드는 것보다 나음
- cumulative 하게 쌓을땐 list의 extend 기능을 활용해보자
- 재귀는 리턴 조건이 명확할때만 써야!

---------

### codility

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    count_num_dict = {}
    for i, _a in enumerate(A):
        try:
            count_num_dict[_a] += 1
        except:
            count_num_dict[_a] = 1
        
    
    for num, count in count_num_dict.items():
        if count % 2 != 0:
            return num
```


```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    # import copy
    # A_copy = copy.deepcopy(A)
    len_of_arr = len(A)
    
    if len_of_arr == K or len(list(set(A))) == 1:
        return A
    else:
        
        shift_arr = [0] * len_of_arr
        for i, _a in enumerate(A):
            shift_idx = (i+K) % len_of_arr
            shift_arr[shift_idx] = A[i]

    return shift_arr
```


```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    count = (Y - X) // D
    if count * D + X >= Y:
        return count
    else:
        return count+1
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    total_sum = sum(A)
    sum_of_left = 0
    sum_of_right = total_sum
    min_abs = 99999
    for i in range(len(A)-1):
        sum_of_left += A[i]
        sum_of_right = sum_of_right - A[i]
        abs_res = abs(sum_of_left - sum_of_right)
        if abs_res < min_abs:
            min_abs = abs_res
            
    return min_abs
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    min_max_val = A[-1] - A[0]
    set_list = list(set(A))
    if len(set_list) != len(A):
        return 0
    if 1 not in A:
        return 0
    
    if min_max_val == len(A)-1:
        return 1
    else:
        return 0
```


```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    res = -1
    x_list = []
    for i, _a_elm in enumerate(A):
        if _a_elm not in x_list:
            x_list.append(_a_elm)
        if len(x_list) == X:
            return i
    return res
        

# 위에꺼보단 밑에께 훨씬 빠르다

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    res = -1
    x_set = set()
    for i, _a_elm in enumerate(A):
        x_set.add(_a_elm)
        if len(x_set) == X:
            return i
    return res
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    res_list = [0] * N
    for a_elm in A:
        if 1 <= a_elm and a_elm <= N:
            res_list[a_elm-1] += 1
        else:
            max_val = max(res_list)
            res_list = [max_val] * N
    return res_list

## 위에껀 O(N x M) 이고 밑에껀 O(N + M) 임 (max가 N 연산이라.. 차라리 if로 비교해가는게 낫긴함)

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    res_list = [0] * N
    max_val = 0
    for a_elm in A:
        if 1 <= a_elm and a_elm <= N:
            res_list[a_elm-1] += 1
            
            if res_list[a_elm-1] > max_val:
                max_val = res_list[a_elm-1]
        else:
            res_list = [max_val] * N
    return res_list

## 이제 마지막인데, max_val이 변하지 않으면 list 새로 생성하지 않게 바꿈! 새로 생성하는것도 O(n)이라서.. 연산이 크기 때문
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    res_list = [0] * N
    pre_max_val = 0
    max_val = 0
    for a_elm in A:
        if 1 <= a_elm and a_elm <= N:
            res_list[a_elm-1] += 1
            
            if res_list[a_elm-1] > max_val:
                max_val = res_list[a_elm-1]
        else:
            if max_val > pre_max_val:
                res_list = [max_val] * N
            pre_max_val = max_val
    return res_list

```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A = list(set([a for a in A if a > 0]))
    A.sort()
    if len(A) == 0:
        return 1
    else:
        for i, a in enumerate(A):
            if i+1 != a:
                return i+1
        return A[-1] + 1
```


```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    total_sum = 0
    num_of_zero = 0
    for i, a_elm in enumerate(A):
        if a_elm == 0: 
            num_of_zero += 1
        else:
            total_sum += num_of_zero * 1
            
        if total_sum > 1000000000:
            return -1
    return total_sum
 
```

- 일단 킵.. TimeComplexity 바꿔줘야함, list -> set 바꾸는것도 time complexity n 들어감 

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    letter_to_score = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4}
    
    len_arr = len(P)
    
    if len(set(S)) == 1:
        return [letter_to_score[S[0]]] * len_arr
    
    # score_S = [letter_to_score[char] for char in S]
    
    list_of_save_min_by_pos = []
    list_of_res = []
    for i in range(len_arr):
        start_idx = P[i]
        end_idx = Q[i]
        min_score = 9999
        
        for saved_start_idx, saved_end_idx in list_of_save_min_by_pos:
            if  start_idx <= saved_start_idx and saved_end_idx <= end_idx:
                min_score = 1
                break
        if min_score == 1:
            list_of_res.append(min_score)
        else:
        
            if end_idx == len_arr-1:
                for s_elm in S[start_idx:]:
                    min_score = letter_to_score[s_elm] if letter_to_score[s_elm] < min_score else min_score
                    if min_score == 1:
                        break
    
    
            else:
                for s_elm in S[start_idx:end_idx+1]:
                    min_score = letter_to_score[s_elm] if letter_to_score[s_elm] < min_score else min_score
                    if min_score == 1:
                        break
                
            list_of_res.append(min_score)
            if min_score == 1:
                list_of_save_min_by_pos.append((start_idx, end_idx))
    return list_of_res
    
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # try O(n**2)
    min_avg_slice = 9999
    start_pos = None
    len_arr = len(A)
    for i in range(len_arr):
        sum_slice = 0
        for j in range(len_arr-i-1):
            start_idx = i
            end_idx = i+j+1
            
            len_slice = end_idx - start_idx + 1
            
            if j == 0:
                if end_idx == len_arr-1:
                    sum_slice = sum(A[start_idx:])
                else:
                    sum_slice = sum(A[start_idx:end_idx+1])
            else:
                sum_slice += A[end_idx]
            
            avg_slice = sum_slice / len_slice
            
            if avg_slice < min_avg_slice:
                min_avg_slice = avg_slice
                start_pos = start_idx
                
    return start_pos
                
                
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    length = B-A+1
    
    count = 0
    for i in range(length):
        if (A + i) % K == 0:
            count += 1
    return count
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    
    if A == B:
        if A % K == 0:
            return 1
        else:
            return 0
    
    count_from_B = int(B / K)
    count_from_A = int(A / K)
        
    if A % K == 0:
        return count_from_B - count_from_A + 1
    else:
        return count_from_B - count_from_A
```
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    
    list_of_score = []
    if A[0] < 0 and A[1] < 0 and A[-1] > 0:
        list_of_score.append(A[0] * A[1] * A[-1])
    
    
    list_of_score.append(A[-1] * A[-2] * A[-3])
    list_of_score.sort()
    return list_of_score[-1]
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    return len(list(set(A)))
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A = [a_elm for a_elm in A if a_elm > 0]
    # A.sort()
    
    length = len(A)
    import itertools
    
    for p,q,r in itertools.combinations(range(length), 3):
        if (A[p] + A[q] > A[r]) and (A[q] + A[r] > A[p]) and (A[r] + A[p] > A[q]):
            return 1
    return 0
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    lower_list = []
    upper_list = []
    for i, a_elm in enumerate(A):
        lower_list.append(i - a_elm)
        upper_list.append(i + a_elm)
        
    lower_list.sort()
    upper_list.sort()
    j = 0
    counter = 0
    total_len = len(A)
    for i in range(total_len):
        while(j < total_len and lower_list[j] <= upper_list[i]): # if문 조건 순서도 중요하네..
            # 0 인 경우는 1개 따져줘야되니 +1했다가 어차피 자기 자신은 제외(-1)하니까 그러려니하는 걸로
            counter += j + 1 - 1  # 중복 아님
            counter -= i # 이미 upper의 index로 세어버린 원들의 개수는 빼버림 # 중복 제거
            j = j + 1
            
            if counter > 10000000:
                return -1
            
    return counter
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    list_of_left_brackets_stack = []
    left_brackets = ['(', '{', '[']
    right_brackets = [')', '}', ']']
    left_to_right = {left_brackets[i]:right_brackets[i] for i in range(3)}
    
    for a_elm in S:
        if a_elm in left_brackets:
            list_of_left_brackets_stack.append(a_elm)
        elif a_elm in right_brackets:
            
            # case many right
            if len(list_of_left_brackets_stack) == 0:
                return 0
            else:
                pop_left_brackets_val = list_of_left_brackets_stack.pop()
                if a_elm != left_to_right[pop_left_brackets_val]:
                    return 0
    
    # case many left
    if len(list_of_left_brackets_stack) != 0:
        return 0
    else:
        return 1
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    upstream_alive_stack = []
    downstream_alive_stack = []
    
    for i in range(len(A)):
        if B[i] == 0:
            upstream_alive_stack.append([i, A[i]])
            while(len(downstream_alive_stack) != 0 and len(upstream_alive_stack) != 0):
                
                down_index, down_fish_size = downstream_alive_stack[-1]
                up_index, up_fish_size = upstream_alive_stack[-1]
                if down_index > up_index:
                    break
                if up_fish_size < down_fish_size:
                    upstream_alive_stack.pop()
                else:
                    downstream_alive_stack.pop()

        elif B[i] == 1:
            downstream_alive_stack.append([i, A[i]])
                
    return len(upstream_alive_stack) + len(downstream_alive_stack)
                    
            
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    left_brackets_stack = []
    for s_elm in S:
        if s_elm == '(':
            left_brackets_stack.append(s_elm)
        else:
            if len(left_brackets_stack) == 0:
                return 0
            left_brackets_stack.pop()
    if len(left_brackets_stack) != 0:
        return 0
    else:
        return 1
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    big_rectangle_stack = []
    
    num_of_blocks = 0
    for h_elm in H:
        big_rectangle_stack = [q for q in big_rectangle_stack if q <= h_elm]        
        if h_elm in big_rectangle_stack:
            pass
        else:
            big_rectangle_stack.append(h_elm)
            num_of_blocks += 1
        
    return num_of_blocks
    
# 위에껀 속도가 좀 느림.. 아래껀 메모리를 좀 더 쓰는대신에 속도가 빠름
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    big_rectangle_stack = []
    dict_for_cotain_check = {}
    
    num_of_blocks = 0
    for h_elm in H:
        # big_rectangle_stack = [q for q in big_rectangle_stack if q <= h_elm]
        while(True):
            if len(big_rectangle_stack) != 0 and h_elm < big_rectangle_stack[-1]:
                val = big_rectangle_stack.pop()
                del dict_for_cotain_check[val]
            else:
                break
            
        if h_elm in dict_for_cotain_check:
            pass
        else:
            big_rectangle_stack.append(h_elm)
            num_of_blocks += 1
            dict_for_cotain_check[h_elm] = 0 # it could be anything.
        
    return num_of_blocks    

```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    import math
    num_to_list_of_index = {}
    num_to_count = {}
    max_count = 0
    max_num = -9999999999999999
    
    
    if len(A) == 0:
        return -1
    
    more_than_half_length = math.ceil(len(A)/2) if len(A)/2 != int(len(A)/2) else len(A)/2 + 1
    
    for i, a_elm in enumerate(A):
        if a_elm in num_to_list_of_index:
            num_to_list_of_index[a_elm].append(i)
            num_to_count[a_elm] += 1
        else:
            num_to_list_of_index[a_elm] = [i]
            num_to_count[a_elm] = 1
    
        if max_count < num_to_count[a_elm]:
            max_count = num_to_count[a_elm]
            max_num = a_elm
    

    if num_to_count[max_num] >= more_than_half_length:
        return num_to_list_of_index[max_num][0]
    else:
        return -1
```

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    num_to_list_of_index = {}
    num_to_count = {}
    max_num = -99999999999
    max_count = 0
    
    # if len(A) == 1:
    #     return 0

    for i, a_elm in enumerate(A):
        if a_elm not in num_to_list_of_index:
            num_to_list_of_index[a_elm] = [i]
            num_to_count[a_elm] = 1
        else:
            num_to_list_of_index[a_elm].append(i)
            num_to_count[a_elm] += 1
        
        if max_count < num_to_count[a_elm]:
            max_count = num_to_count[a_elm]
            max_num = a_elm
    
    
    if max_num in num_to_list_of_index:
        list_of_max_num_index = num_to_list_of_index[max_num]
    else:
        list_of_max_num_index = None
        max_count = 0
        for num, list_of_index in num_to_list_of_index.items():
            if max_count < len(list_of_index):
                max_count = len(list_of_index)
                list_of_max_num_index = list_of_index
                
    total_count_len = len(list_of_max_num_index)
    total_len = len(A)
    res_count = 0
    
    import math
    # for i, max_num_index in enumerate(list_of_max_num_index):
    #     left_len = max_num_index + 1
    #     left_count = i + 1
        
    #     right_len = total_len - left_len
    #     right_count = total_count_len - left_count
        
    #     left_more_than_half = int(left_len / 2) + 1 if int(left_len / 2) == left_len / 2 else math.ceil(left_len / 2)
        
    #     right_more_than_half = int(right_len / 2) + 1 if int(right_len / 2) == right_len / 2 else math.ceil(right_len / 2)
        
    #     if (left_count >= left_more_than_half) and (right_count >= right_more_than_half):
    #         res_count += 1
    
    
    left_count_arr = []
    for i, max_num_index in enumerate(list_of_max_num_index):
        
        if i == len(list_of_max_num_index) - 1:
            to_next_length = total_len - max_num_index 
        else:
            to_next_length = list_of_max_num_index[i+1] - list_of_max_num_index[i]
        left_count_arr.extend([i + 1] * (to_next_length))
    
    # print("left_count_arr: ", left_count_arr)
        
            
    for i in range(total_len):
        left_len = i + 1
        left_count = left_count_arr[i]
        # left_count = 0
        # for max_num_index in list_of_max_num_index:
        #     if max_num_index <= i:
        #         left_count += 1
        #     else:
        #         break
        
        right_len = total_len - left_len
        right_count = total_count_len - left_count
            
        
        left_more_than_half = int(left_len / 2) + 1 if int(left_len / 2) == left_len / 2 else math.ceil(left_len / 2)
        
        right_more_than_half = int(right_len / 2) + 1 if int(right_len / 2) == right_len / 2 else math.ceil(right_len / 2)
        
        if (left_count >= left_more_than_half) and (right_count >= right_more_than_half):
            res_count += 1
            
    return res_count
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

----------

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

