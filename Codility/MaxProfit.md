# MaxProfit

Given a log of stock prices compute the maximum possible earning.

## Task description

A zero-indexed array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:

    A[0] = 23171
    A[1] = 21011
    A[2] = 21123
    A[3] = 21366
    A[4] = 21013
    A[5] = 21367

If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

```java
class Solution { public int solution(int[] A); }
```

that, given a zero-indexed array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:

    A[0] = 23171
    A[1] = 21011
    A[2] = 21123
    A[3] = 21366
    A[4] = 21013
    A[5] = 21367

the function should return 356, as explained above.

Assume that:

* N is an integer within the range [0..400,000];
* each element of array A is an integer within the range [0..200,000].

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
    if len(A) == 0:
        return 0

    left_index = 0
    right_index = len(A) - 1

    min_left = 1000000000
    max_left = -999999999
    min_right = 1000000000
    max_right = -999999999


    min_left_index = None
    max_left_index = None    
    min_right_index = None
    max_right_index = None


    max_score = 0
    while(True):

        if right_index <= left_index:
            break

        if A[left_index] < min_left:
            min_left = A[left_index]
            min_left_index = left_index

        if max_left < A[left_index]:
            max_left = A[left_index]
            max_left_index = left_index            

        if A[right_index] < min_right:
            min_right = A[right_index]            
            min_right_index = right_index            

        if max_right < A[right_index]:
            max_right = A[right_index]            
            max_right_index = right_index


        if A[left_index+1] <= A[left_index]:
            left_index = left_index + 1
        elif A[right_index] <= A[right_index-1]:
            right_index = right_index - 1
        else:
            left_index = left_index + 1
            right_index = right_index - 1

    max_score = max_right - min_left

    if min_left_index < max_left_index:
        if max_score < max_left - min_left:
            max_score = max_left - min_left

    if min_right_index < max_right_index:
        if max_score < max_right - min_right:
            max_score = max_right - min_right

    if max_score <= 0:
        return 0
    else:
        return max_score
```

## Comment
