# MaxProductOfThree

Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).

## Task description

A non-empty zero-indexed array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

    A[0] = -3
    A[1] = 1
    A[2] = 2
    A[3] = -2
    A[4] = 5
    A[5] = 6

contains the following example triplets:

* (0, 1, 2), product is −3 * 1 * 2 = −6
* (1, 2, 4), product is 1 * 2 * 5 = 10
* (2, 4, 5), product is 2 * 5 * 6 = 60

Your goal is to find the maximal product of any triplet.

Write a function:

```
class Solution { public int solution(int[] A); }
```

that, given a non-empty zero-indexed array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

    A[0] = -3
    A[1] = 1
    A[2] = 2
    A[3] = -2
    A[4] = 5
    A[5] = 6

the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Assume that:

* N is an integer within the range [3..100,000];
* each element of array A is an integer within the range [−1,000..1,000].

Complexity:

* expected worst-case time complexity is O(N*log(N));
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
    A.sort()

    list_of_score = []
    if A[0] < 0 and A[1] < 0 and A[-1] > 0:
        list_of_score.append(A[0] * A[1] * A[-1])


    list_of_score.append(A[-1] * A[-2] * A[-3])
    list_of_score.sort()
    return list_of_score[-1]
```

### First

* Programming language: Python
* Task score: 100%
* Analysis: O(N*log(N))
* Link: https://app.codility.com/demo/results/trainingRKC7YU-7SB/
* Code

```python
def solution(A):
    # write your code in Python 3.6
    A.sort()
    
    left = A[0] * A[1] * A[-1]
    right = A[-1] * A[-2] * A[-3]
    
    max_product = left if left > right else right
    return max_product
```

## Comment
- 두번째코드가 첫번째보단 간단하나 원리는 같고 사실 0 값 체크를 안했으니 그리좋은 코드라 할순 없겠다
