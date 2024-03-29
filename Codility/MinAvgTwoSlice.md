# MinAvgTwoSlice

Find the minimal average of any slice containing at least two elements.

## Task description

A non-empty zero-indexed array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

* slice (1, 2), whose average is (2 + 2) / 2 = 2;
* slice (3, 4), whose average is (5 + 1) / 2 = 3;
* slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

```java
class Solution { public int solution(int[] A); }
```

that, given a non-empty zero-indexed array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.

Assume that:

* N is an integer within the range [2..100,000];
* each element of array A is an integer within the range [−10,000..10,000].

Complexity:

* expected worst-case time complexity is O(N);
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


## Solution

### Second

* Programming language: Python
* Task score: 100%
* Analysis: O(N)
* Link1 : https://app.codility.com/demo/results/training3ZXTRH-5R4/
* Link2 : https://wildcatsy.blogspot.com/2017/04/codility-lesson-5-frefix-sums_25.html
* Code

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

## Comment
- 수학을 좀 알아야 풀 수 있었던 문제다..
- 그냥 풀었을땐 O(N**2) 나왔었음
- 수학내용:
  - 평균구했을때 한쪽수는 평균보다 작다
  - 평균들의 평균은 각 인자들의 평균과 같다
- 위 두가지 조건으로 인자의 개수가 2,3인것만 조사하면 되었음
- 4이상은 2,3의 부분집합으로 평균들의 평균을 했을때 부분집합의 평균이 더 작기 때문임
- 하.. 수학 지식 이거.. 거의 없으면 못맞추는거 아닌가?