# [CountDistinctSlices](https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/)

Count the number of distinct slices (containing only unique numbers).

## Task description

An integer M and a non-empty array A consisting of N non-negative integers are given. All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. A distinct slice is a slice consisting of only unique numbers. That is, no individual number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:

def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:

- N is an integer within the range [1..100,000];
- M is an integer within the range [0..100,000];
- each element of array A is an integer within the range [0..M].

## Solution

### First

* Programming language: Python
* Task score:
    - Correctness: 100%
    - Performance: 40%
* Analysis
    - O(N * (N + M))
* Link: https://app.codility.com/demo/results/trainingQ7HWHH-ZPW/
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # write your code in Python 3.6
    count = 0
    for i in range(len(A)):
        for j in range(len(A)-i):
            if i+j+1 == len(A):
                if len(A[i:]) == len(set(A[i:])):
                    count += 1
            else:
                if len(A[i:i+j+1]) == len(set(A[i:i+j+1])):
                    count += 1
                else:
                    break
    return count
```


## Comment
- 우선 최대한 편한 방법으로 풀어봤다. 일단 계속 Set을 만들어서 체크하는 것부터 미쓰..라고 생각한다. 저거 생성할때마다 O(N)이 걸리니까
- 그리고 i, j 로 배열 값 비교할때 항상 두번째 for loop안의 값 범위를 설정해주는게 미숙한데.. i+j+alpha 식으로 한다는걸 잊으면 안되겠다. 추가로 A에 대한 인덱싱에서 마지막 값에 대해서는 따로 length로 처리해줘야한다는걸 잊지말자
- 개선에 대한 아이디어는 음..