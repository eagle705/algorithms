# FrogJmp

Count minimal number of jumps from position X to Y.

## Task description

A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

```
class Solution { public int solution(int X, int Y, int D); }
```

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10  Y = 85  D = 30

the function should return 3, because the frog will be positioned as follows:

* after the first jump, at position 10 + 30 = 40
* after the second jump, at position 10 + 30 + 30 = 70
* after the third jump, at position 10 + 30 + 30 + 30 = 100

Assume that:

* X, Y and D are integers within the range [1..1,000,000,000];
* X ≤ Y.

Complexity:

* expected worst-case time complexity is O(1);
* expected worst-case space complexity is O(1).

## Solution

### First

* Programming language: Python
* Task score: 100%
* Analysis
* Code

```python
def solution(X, Y, D):
    # write your code in Python 3.6
    count = (Y - X) // D
    if count * D + X >= Y:
        return count
    else:
        return count+1
```


### Second

* Programming language: Python
* Task score: 100%
* Analysis: O(1)
* Link: https://app.codility.com/demo/results/trainingFMVXKM-SQE/
* Code

```python
def solution(X, Y, D):
    # write your code in Python 3.6
    total_d = Y-X
    if (total_d / D) == int(total_d / D):
        return int(total_d / D)
    else:
        return int(total_d / D) + 1
```

### Comment
- 첫번째 풀이가 더 나았던거 같다
- return형으로 total_d / D 이렇게만 했더니 float라고 에러가 떳다. 로컬의 인터프리터에서는 int형이라는데 흠.. 암튼 int로 감싸서 리턴해주는게 나을듯
- 두번째 풀이에서는 그냥 start point를 0으로 셋팅해주고 풀었다