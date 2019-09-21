# MissingInteger

Find the minimal positive integer not occurring in a given sequence.

## Task description

Write a function:

```java
class Solution { public int solution(int[] A); }
```

that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer (greater than 0) that does not occur in A.

For example, given:

  A[0] = 1  A[1] = 3  A[2] = 6  A[3] = 4  A[4] = 1  A[5] = 2

the function should return 5.

Assume that:

* N is an integer within the range [1..100,000];
* each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

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
    A = list(set([a for a in A if a > 0]))
    A.sort()
    if len(A) == 0:
        return 1
    else:
        for i, a in enumerate(A):
            if i+1 != a:
                return i+1
        return A[-1] + 1
```

### Second

* Programming language: Python
* Task score: 100%
* Analysis: O(N) or O(N * log(N))
* Link: https://app.codility.com/demo/results/training8ZPPFV-GAE/
* Code

```python
def solution(A):
    # write your code in Python 3.6    
    set_of_A = set(A)    
    for i in range(1, len(A)+1):
        if i not in set_of_A:
            return i
    return len(A)+1
```

## Comment
- 첫번째 풀이 처럼 굳이 정렬 안해도..되고 원소도 0 이상으로 뽑지 않아도 된다. 어차피 체크 리스트 만드는데 O(n) 이기 때문에 그냥 set으로 만들어주면 됨
- 그 후에는 1~N개 까지 루프 돌려주고 거기서 안걸리면 N+1이 없는걸로 리턴해주면 됨

