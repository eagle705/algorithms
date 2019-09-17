# MaxCounters

Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.

## Task description

You are given N counters, initially set to 0, and you have two possible operations on them:

* increase(X) − counter X is increased by 1,
* max counter − all counters are set to the maximum value of any counter.

A non-empty zero-indexed array A of M integers is given. This array represents consecutive operations:

* if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
* if A[K] = N + 1 then operation K is max counter.

For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)

The goal is to calculate the value of every counter after all operations.

Write a function:

```java
class Solution { public int[] solution(int N, int[] A); }
```

that, given an integer N and a non-empty zero-indexed array A consisting of M integers, returns a sequence of integers representing the values of the counters.

The sequence should be returned as:

* a structure Results (in C), or
* a vector of integers (in C++), or
* a record Results (in Pascal), or
* an array of integers (in any other programming language).

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the function should return [3, 2, 2, 4, 2], as explained above.

Assume that:

* N and M are integers within the range [1..100,000];
* each element of array A is an integer within the range [1..N + 1].

Complexity:

* expected worst-case time complexity is O(N+M);
* expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

## Solution

### First

* Programming language: Python
* Task score:
* Analysis
* Code

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


## Comment
