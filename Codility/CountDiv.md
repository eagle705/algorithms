# CountDiv

Compute number of integers divisible by k in range [a..b].

## Task description

Write a function:

```java
class Solution { public int solution(int A, int B, int K); }
```

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Assume that:

* A and B are integers within the range [0..2,000,000,000];
* K is an integer within the range [1..2,000,000,000];
* A ≤ B.

Complexity:

* expected worst-case time complexity is O(1);
* expected worst-case space complexity is O(1).

## Solution

### First

* Programming language: Python
* Task score: 100%
* Analysis
  - The solution obtained perfect score.
  - Detected time complexity: O(1)
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    length = B-A+1

    count = 0
    for i in range(length):
        if (A + i) % K == 0:
            count += 1
    return count

    # you can write to stdout for debugging purposes, e.g.
    # print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6

    if A == B:
        if A % K == 0:
            return 1
        else:
            return 0

    count_from_B = int(B / K)
    count_from_A = int(A / K)

    if A % K == 0:
        return count_from_B - count_from_A + 1
    else:
        return count_from_B - count_from_A

```

### Second

* Programming language: Python
* Task score: 100%
* Analysis
  - The solution obtained perfect score.
  - Detected time complexity: O(1)
* Link: https://app.codility.com/demo/results/training9WZJJF-FJM/
* Code

```python
def solution(A, B, K):
    # write your code in Python 3.6
    count_prev_A = (A-1) // K 
    count_B = B // K
    
    return count_B - count_prev_A
```


## Comment
- 코드는 전에 비하면 훨씬 나아졌다
- prefix_sum 기능으로 이전에 몇갠지 세고 현재 몇갠지 세서 빼줌으로써 총 개수를 구하면 됨