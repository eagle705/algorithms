# MissingInteger

Find the minimal positive integer not occurring in a given sequence.

## Task description

Write a function:

```java
class Solution { public int solution(int[] A); }
```

that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer (greater than 0) that does not occur in A.

For example, given:

  A[0] = 1  A[1] = 3  A[2] = 6  A[3] = 4  A[4] = 1  A[5] = 2

the function should return 5.

Assume that:

* N is an integer within the range [1..100,000];
* each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

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

## Comment
