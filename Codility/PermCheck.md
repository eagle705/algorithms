# PermCheck

Check whether array A is a permutation.

## Task description

A non-empty zero-indexed array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

  A[0] = 4  A[1] = 1  A[2] = 3  A[3] = 2

is a permutation, but array A such that:

  A[0] = 4  A[1] = 1  A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

```java
class Solution { public int solution(int[] A); }
```

that, given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

  A[0] = 4  A[1] = 1  A[2] = 3

the function should return 1.

Given array A such that:

  A[0] = 4  A[1] = 1  A[2] = 3

the function should return 0.

Assume that:

* N is an integer within the range [1..100,000];
* each element of array A is an integer within the range [1..1,000,000,000].

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

```Python
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


## Comment
