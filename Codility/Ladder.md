# [Ladder](https://app.codility.com/programmers/lessons/13-fibonacci_numbers/ladder/)

Count the number of different ways of climbing to the top of a ladder.

## Task description

You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:

- with your first step you can stand on rung 1 or 2,
- if you are on rung K, you can move to rungs K + 1 or K + 2,
- finally you have to stand on rung N.
Your task is to count the number of different ways of climbing to the top of the ladder.

For example, given N = 4, you have five different ways of climbing, ascending by:

- 1, 1, 1 and 1 rung,
- 1, 1 and 2 rungs,
- 1, 2 and 1 rung,
- 2, 1 and 1 rungs, and
- 2 and 2 rungs.
- 
Given N = 5, you have eight different ways of climbing, ascending by:

- 1, 1, 1, 1 and 1 rung,
- 1, 1, 1 and 2 rungs,
- 1, 1, 2 and 1 rung,
- 1, 2, 1 and 1 rung,
- 1, 2 and 2 rungs,
- 2, 1, 1 and 1 rungs,
- 2, 1 and 2 rungs, and
- 2, 2 and 1 rung.

The number of different ways can be very large, so it is sufficient to return the result modulo 2P, for a given integer P.

Write a function:

```python
def solution(A, B):
```

that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2B[I].

For example, given L = 5 and:

```
    A[0] = 4   B[0] = 3
    A[1] = 4   B[1] = 2
    A[2] = 5   B[2] = 4
    A[3] = 5   B[3] = 3
    A[4] = 1   B[4] = 1
```

the function should return the sequence [5, 1, 8, 0, 1], as explained above.

Write an efficient algorithm for the following assumptions:

- L is an integer within the range [1..50,000];
- each element of array A is an integer within the range [1..L];
- each element of array B is an integer within the range [1..30].

## Solution

### First

* Programming language: Python
* Task score:
    - Correctness: 100%
    - Performance: 25%
* Analysis
    - O(L**2)
* Link: https://app.codility.com/demo/results/trainingYJQPUH-X7X/
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    # 결과 재활용을 위한 저장소
    N_to_count = {}
    
    # 1 -> 1, 2 -> 2, 3 -> 3, 4 -> 5, 5 -> 8
    # 피보나치임
    
    # O(N)
    def fib_dynamic(N):
        fib = [0] * (N + 2) # 왜 N + 2지
        fib[1] = 1
        for i in range(2, N+2):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[N+1]
        
    res_list = []    
    for i in range(len(B)):
        if A[i] not in N_to_count:
            res = fib_dynamic(A[i])
            N_to_count[A[i]] = res
        else:
            res = N_to_count[A[i]]
        res_list.append(res % 2**B[i])
    return res_list
```


## Comment
- 피보나치 알고리즘을 좀 더 효율적으로 풀 수 있는 방법 고민해야할 듯 -> equation
- 피보나치 단원이라서 피보나치인줄 알았다.. 좀 더 통찰력이 필요할 듯
- 인덱스를 N+2로 맞추는게 잘 이해가 안감.. 해보면서 파악함
