# NumberOfDiscIntersections

Compute the number of intersections in a sequence of discs.

## Task description

We draw N discs on a plane. The discs are numbered from 0 to N − 1. A zero-indexed array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

    A[0] = 1
    A[1] = 5
    A[2] = 2
    A[3] = 1
    A[4] = 4
    A[5] = 0

There are eleven (unordered) pairs of discs that intersect, namely:

* discs 1 and 4 intersect, and both intersect with all the other discs;
* disc 2 also intersects with discs 0 and 3.

Write a function:

```java
class Solution { public int solution(int[] A); }
```

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

![image](https://codility-frontend-prod.s3.amazonaws.com/media/task_static/number_of_disc_intersections/static/images/auto/0eed8918b13a735f4e396c9a87182a38.png)

Given array A shown above, the function should return 11, as explained above.

Assume that:

* N is an integer within the range [0..100,000];
* each element of array A is an integer within the range [0..2,147,483,647].

Complexity:

* expected worst-case time complexity is O(N*log(N));
* expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

## Solution

### First

* Programming language: Python
* Task score: 100%
* Analysis: O(N*log(N)) or O(N)
* Link: https://app.codility.com/demo/results/trainingTX7KDG-4Z8/
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    lower_list = []
    upper_list = []
    for i, a_elm in enumerate(A):
        lower_list.append(i - a_elm)
        upper_list.append(i + a_elm)

    lower_list.sort()
    upper_list.sort()
    j = 0
    counter = 0
    total_len = len(A)
    for i in range(total_len):
        while(j < total_len and lower_list[j] <= upper_list[i]): # if문 조건 순서도 중요하네..
            # 0 인 경우는 1개 따져줘야되니 +1했다가 어차피 자기 자신은 제외(-1)하니까 그러려니하는 걸로
            counter += j + 1 - 1  # 중복 아님
            counter -= i # 이미 upper의 index로 세어버린 원들의 개수는 빼버림 # 중복 제거
            j = j + 1

            if counter > 10000000:
                return -1

    return counter
```


## Comment
- 솔직히 이문제는 너무 어렵다.. 이해가 잘 안됨..
- 풀이 참조해서 풀었다. 하..
- j개를 더해주는게 젤 이해 안됨..
- 예제에서 겹치는건 아래와 같이해서 11개라는데 흠..

```
0, 1 / 0, 2 / 0, 4
1, 2 / 1, 3 / 1, 4 / 1, 5
2, 3 / 2, 4
3, 4
4, 5
```
