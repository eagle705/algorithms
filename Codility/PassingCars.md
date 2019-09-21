# PassingCars

Count the number of passing cars on the road.

## Task description

A non-empty zero-indexed array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

* 0 represents a car traveling east,
* 1 represents a car traveling west.

The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0  A[1] = 1  A[2] = 0  A[3] = 1  A[4] = 1

We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

```java
class Solution { public int solution(int[] A); }
```

that, given a non-empty zero-indexed array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0  A[1] = 1  A[2] = 0  A[3] = 1  A[4] = 1

the function should return 5, as explained above.

Assume that:

* N is an integer within the range [1..100,000];
* each element of array A is an integer that can have one of the following values: 0, 1.

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
    total_sum = 0
    num_of_zero = 0
    for i, a_elm in enumerate(A):
        if a_elm == 0:
            num_of_zero += 1
        else:
            total_sum += num_of_zero * 1

        if total_sum > 1000000000:
            return -1
    return total_sum
```


### Second

* Programming language: Python
* Task score: 100%
* Analysis: O(N)
* Link: https://app.codility.com/demo/results/trainingCR8EGF-WTY/
* Code

```python
def solution(A):
    # write your code in Python 3.6
    total_count = 0
    product_term = 0
    for i, a_elm in enumerate(A):
        if a_elm == 0:
            product_term += 1
        else:
            total_count += product_term
    
    if total_count > 10**9:
        return -1
    else:
        return total_count
```

## Comment
- 첫번째 풀이와 같다. 은연중에 기억하거나 생각의 회로가 똑같은듯..