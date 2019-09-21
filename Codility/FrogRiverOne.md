# FrogRiverOne

Find the earliest time when a frog can jump to the other side of a river.

## Task description

A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given a zero-indexed array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

```java
class Solution { public int solution(int X, int[] A); }
```

that, given a non-empty zero-indexed array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

the function should return 6, as explained above.

Assume that:

* N and X are integers within the range [1..100,000];
* each element of array A is an integer within the range [1..X].

Complexity:

* expected worst-case time complexity is O(N);
* expected worst-case space complexity is O(X), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

## Solution

### First

* Programming language: python
* Task score:
* Analysis
* Code

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

### Second

* Programming language: python
* Task score: 100%
* Analysis: O(N)
* Link: https://app.codility.com/demo/results/trainingHDNVQT-KSV/
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    leaf_dict = {}
    count = 0
    for i, a_elm in enumerate(A):
        if a_elm not in leaf_dict:
            leaf_dict[a_elm] = True
            count += 1
            if count == X:
                return i
    return -1
```

## Comment
- dict으로 원소가 있는지를 체크했다. List로 체크할 경우 O(n)이 걸려서.. 리스트로 쓰면 안된다
- 그 밖에는 개수 맞춰줘서 조건 맞을때 리턴해주는 걸로 처리