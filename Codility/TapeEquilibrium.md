# TapeEquilibrium

Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

## Task description

A non-empty zero-indexed array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3  A[1] = 1  A[2] = 2  A[3] = 4  A[4] = 3

We can split this tape in four places:

* P = 1, difference = |3 − 10| = 7
* P = 2, difference = |4 − 9| = 5
* P = 3, difference = |6 − 7| = 1
* P = 4, difference = |10 − 3| = 7

Write a function:

```java
class Solution { public int solution(int[] A); }
```

that, given a non-empty zero-indexed array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3  A[1] = 1  A[2] = 2  A[3] = 4  A[4] = 3

the function should return 1, as explained above.

Assume that:

* N is an integer within the range [2..100,000];
* each element of array A is an integer within the range [−1,000..1,000].

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
    total_sum = sum(A)
    sum_of_left = 0
    sum_of_right = total_sum
    min_abs = 99999
    for i in range(len(A)-1):
        sum_of_left += A[i]
        sum_of_right = sum_of_right - A[i]
        abs_res = abs(sum_of_left - sum_of_right)
        if abs_res < min_abs:
            min_abs = abs_res

    return min_abs
```

### Second

* Programming language: Python
* Task score: 100%
* Analysis: O(N)
* Link: https://app.codility.com/demo/results/trainingZA36M4-Y5F/
* Code

```python
def solution(A):
    # write your code in Python 3.6
    
    prefix_sum = []
    sum_num = 0
    for a_elm in A:
        sum_num += a_elm
        prefix_sum.append(sum_num)
    
    min_abs_diff = 10**10
    
    for i in range(len(A)-1):
        front_sum = prefix_sum[i]
        end_sum = prefix_sum[-1] - front_sum
        abs_diff = abs(front_sum - end_sum)        
        # print("abs_diff: ", abs_diff)
        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
    return min_abs_diff
```

### Comment
- 첫번째는 점점 합치는거라 더 빠르긴할듯
- 두번째는 prefix sum으로 풀어서 좀 더 편하긴함
- 마지막인덱스는 빼줘야 두개의 구간으로 비교되는데 그거 한번 빼먹어서 런타임오류났었음.. 까먹지 말것
