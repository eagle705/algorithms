# CountFactors

Count factors of given number n.

## Task description

A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

```java
class Solution { public int solution(int N); }
```

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Assume that:

* N is an integer within the range [1..2,147,483,647].

Complexity:

* expected worst-case time complexity is O(sqrt(N));
* expected worst-case space complexity is O(1).

## Solution

### First

* Programming language: Python
* Task score:
* Analysis
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    count = 0
    for i in range(N):
        n = i+1
        if N % n == 0:
            count += 1
    return count

# 위에처럼 하면 O(N)이라 안됨.. O(sqrt(N)) 되야함..
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    count = 0
    r_num = N

    for l_index in range(N):

        l_num = l_index+1

        if r_num < l_num:
            break

        if N % l_num == 0:
            r_num = N // l_num
            if r_num < l_num:
                break
            if r_num == l_num:
                count +=1
            else:
                count += 2
    return count
```

## Comment
