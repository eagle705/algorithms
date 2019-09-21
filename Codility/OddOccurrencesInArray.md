#  OddOccurrencesInArray

Find value that occurs in odd number of elements.

## Task description

A non-empty zero-indexed array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

* the elements at indexes 0 and 2 have value 9,
* the elements at indexes 1 and 3 have value 3,
* the elements at indexes 4 and 6 have value 9,
* the element at index 5 has value 7 and is unpaired.

Write a function:

```java
class Solution { public int solution(int[] A); }
```

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

the function should return 7, as explained in the example above.

Assume that:

* N is an odd integer within the range [1..1,000,000];
* each element of array A is an integer within the range [1..1,000,000,000];
* all but one of the values in A occur an even number of times.

Complexity:

* expected worst-case time complexity is O(N);
* expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

## Solution

### First

* Programming language: Python
* Task score:
* Analysis summary:
* Code

```python
def solution(A):
    # write your code in Python 3.6
    count_num_dict = {}
    for i, _a in enumerate(A):
        try:
            count_num_dict[_a] += 1
        except:
            count_num_dict[_a] = 1


    for num, count in count_num_dict.items():
        if count % 2 != 0:
            return num
```

### Second

* Programming language: Python
* Task score: 100%
* Analysis summary: O(N) or O(N*log(N))
* Link: https://app.codility.com/demo/results/trainingSYUMCZ-9H3/
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # 그냥 맵에서 카운트 해보자
    num_to_count = {}
    for i, a_elm in enumerate(A):
        if a_elm not in num_to_count:
            num_to_count[a_elm] = 1
        else:
            num_to_count[a_elm] += 1
    
    for num, count in num_to_count.items():
        if count % 2 != 0:
            return num
            
```

## Comment
- 처음이랑 두번째 풀이가 똑같은게 함정..
- 나머지는 even number라고 나와있어서 if N % 2 != 0 으로 테스트해서 결과 뽑았다
