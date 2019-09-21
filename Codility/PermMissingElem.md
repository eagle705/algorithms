# PermMissingElem

Find the missing element in a given permutation.

## Task description

A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

```java
class Solution { public int solution(int[] A); }
```

that, given a zero-indexed array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2  A[1] = 3  A[2] = 1  A[3] = 5

the function should return 4, as it is the missing element.

Assume that:

* N is an integer within the range [0..100,000];
* the elements of A are all distinct;
* each element of array A is an integer within the range [1..(N + 1)].

Complexity:

* expected worst-case time complexity is O(N);
* expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

## Solution

### First

* Programming language: Python
* Task score: 100%
* Analysis: O(N) or O(N * log(N))
* Link: https://app.codility.com/demo/results/trainingEXDP2H-M8M/
* Code

```python
def solution(A):
    # write your code in Python 3.6
    
    if len(A) == 0:
        return 1
    
    if len(A) == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    A.sort()
    
    for i, a_elm in enumerate(A):
        if a_elm != i+1:
            return i+1
            
    # this case, N=1 is missing value
    return A[-1]+1
```

### Comment
- 사실 처음엔 다 맞지 못했다는...
- 원인은 1~N+1 범위 내에서 1개가 없는건데, 1,2,..,N 이 존재한다면 N+1이 없는거라고 할 수 있는데 그걸 고려하지 않았기 때문
- 정렬하고 풀었기때문에 루프가 돌았는데도 리턴이 안되는 경우는 N+1이 없는 것이므로 N+1을 리턴해주면 되고
- 각 케이스에 대한 예외처리는 아직도 잘 이해가 안됨 왜 empty list일때는 1을 리턴해줘야하는지..-_-;