# MinPerimeterRectangle

Find the minimal perimeter of any rectangle whose area equals N.

## Task description

An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

* (1, 30), with a perimeter of 62,
* (2, 15), with a perimeter of 34,
* (3, 10), with a perimeter of 26,
* (5, 6), with a perimeter of 22.

Write a function:

```java
class Solution { public int solution(int N); }
```

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Assume that:

* N is an integer within the range [1..1,000,000,000].

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

    import math
    # 양옆으로 인덱스 이동
    num_left = 1
    num_right = N

    counter = 0
    min_perimeter = 10**10
    while(True):
        if N % num_left == 0:
            num_right = N // num_left
            counter += 1

            temp_perimeter = 2*(num_left + num_right)
            if temp_perimeter < min_perimeter:
                min_perimeter = temp_perimeter

        if num_left > num_right:
            break

        # sqrt(N)이 되는 이유는 합성수면 적어도 하나는 sqrt(N)이하이기 때문
        if num_left > math.sqrt(N) and counter == 1: # 소수인경우!
            break

        num_left += 1

    return min_perimeter  
```


## Comment
