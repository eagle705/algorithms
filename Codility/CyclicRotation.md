# CyclicRotation

Rotate an array to the right by a given number of steps.

## Task description

A zero-indexed array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is also moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. The goal is to rotate array A K times; that is, each element of A will be shifted to the right by K indexes.

Write a function:

```java
class Solution { public int[] solution(int[] A, int K); }
```

that, given a zero-indexed array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function should return [9, 7, 6, 3, 8].

Assume that:

* N and K are integers within the range [0..100];
* each element of array A is an integer within the range [−1,000..1,000].

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

## Solution

### First

* Programming language: Python
* Task score:
* Analysis summary:
* Code

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

## Comment
