# Dominator

Find an index of an array such that its value occurs at more than half of indices in the array.

## Task description

A zero-indexed array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

    A[0] = 3    A[1] = 4    A[2] =  3
    A[3] = 2    A[4] = 3    A[5] = -1
    A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

```java
class Solution { public int solution(int[] A); }
```

that, given a zero-indexed array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

Assume that:

* N is an integer within the range [0..100,000];
* each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

For example, given array A such that

    A[0] = 3    A[1] = 4    A[2] =  3
    A[3] = 2    A[4] = 3    A[5] = -1
    A[6] = 3    A[7] = 3

the function may return 0, 2, 4, 6 or 7, as explained above.

Complexity:

* expected worst-case time complexity is O(N);
* expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

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

## Comment
