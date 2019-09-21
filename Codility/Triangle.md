# Triangle

Determine whether a triangle can be built from a given set of edges.

## Task description

A zero-indexed array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

* A[P] + A[Q] > A[R],
* A[Q] + A[R] > A[P],
* A[R] + A[P] > A[Q].

For example, consider array A such that:

    A[0] = 10    A[1] = 2    A[2] = 5
    A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.

Write a function:

```java
class Solution { public int solution(int[] A); }
```

that, given a zero-indexed array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

    A[0] = 10    A[1] = 2    A[2] = 5
    A[3] = 1     A[4] = 8    A[5] = 20

the function should return 1, as explained above. Given array A such that:

    A[0] = 10    A[1] = 50    A[2] = 5
    A[3] = 1
the function should return 0.

Assume that:

* N is an integer within the range [0..100,000];
* each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

Complexity:

* expected worst-case time complexity is O(N*log(N));
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
    A = [a_elm for a_elm in A if a_elm > 0]
    # A.sort()

    length = len(A)
    import itertools

    for p,q,r in itertools.combinations(range(length), 3):
        if (A[p] + A[q] > A[r]) and (A[q] + A[r] > A[p]) and (A[r] + A[p] > A[q]):
            return 1
    return 0
```

### Second

* Programming language: Python
* Task score: 100%
* Analysis: O(N*log(N))
* Link: https://app.codility.com/demo/results/trainingGBR7BY-ZKJ/
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    A.sort()
    A = [a_elm for a_elm in A if a_elm >0]
    
    N = len(A)
    if N <3:
        return 0
    
    for i in range(N - 2):
        # if A[i+2] + A[i+1] > A[i]: # always True
        # if A[i+2] + A[i] > A[i+1]: # always True
        # if A[i] + A[i+1] > A[i+2]: # should be checked
        if A[i] + A[i+1] > A[i+2]: # 나머지 인덱스를 비교하기보다 가장 큰거 두개가 확률이 제일 큼.. 큰게 되야 작은것도 될 가능성이 있으니까   
            return 1
    return 0
```

## Comment
- 그냥 itertools로 풀면 general하게 풀리겠지만 시간이 오래걸림
- 잘 풀려면 수학을 또 이해해야함.. 생각해보면 알고리즘문제지만.. 코드짜고 루프 효율적으로 돌리는 스킬뿐만 아니라 수학적인 센스로 해결할 수 있는걸 물어보는 듯
- 핵심은 정렬해놓고 나면 삼각형 만족 조건 3개중 2개는 이미 만족된 상황이라는 것
- 나머지 한개는 if A[i] + A[i+1] > A[i+2]: 인데, 이 경우의 경우 A[i]와 A[i+1]을 쓸수 밖에 없는건 이것보다 작은건 어차피 A[i+2] 보다 클 가능성이 더 적기 때문이다. 큰 것끼리 비교하는게 젤 가능성이 높으니.
- 쉽다면 쉬웠지만.. 생각없이 풀면 TimeComplexity가 높게 나올 수 있는 문제였음