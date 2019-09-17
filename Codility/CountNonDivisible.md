# CountNonDivisible

Calculate the number of elements of an array that are not divisors of each element.

## Task description

You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:

* A[0] = 3, the non-divisors are: 2, 6,
* A[1] = 1, the non-divisors are: 3, 2, 3, 6,
* A[2] = 2, the non-divisors are: 3, 3, 6,
* A[3] = 3, the non-divisors are: 2, 6,
* A[4] = 6, there aren't any non-divisors.

Write a function:

```java
class Solution { public int[] solution(int[] A); }
```

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

The sequence should be returned as:

* a structure Results (in C), or
* a vector of integers (in C++), or
* a record Results (in Pascal), or
* an array of integers (in any other programming language).

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
the function should return [2, 4, 3, 2, 0], as explained above.

Assume that:

* N is an integer within the range [1..50,000];
* each element of array A is an integer within the range [1..2 * N].

Complexity:

* expected worst-case time complexity is O(N*log(N));
* expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

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

    res_list = []
    for a_elm in A:
        count = 0
        for a_elm_2 in A:
            if a_elm % a_elm_2 != 0:
                count += 1
        res_list.append(count)
    return res_list

## 위에껀 O(N**2)이니 바꿔야함
def solution(A):
    # write your code in Python 3.6
    res_list = []
    N = 50000 #max(A)
    len_A = len(A)
    num_count_list = [0] * (N * 2)

    for a_elm in A:
        num_count_list[a_elm] += 1

    # 전체에서 합성수 빼서 구하자
    for a_elm in A:
        num_divider = 0
        for i in range(a_elm):
            temp_num = i+1
            if a_elm < temp_num*temp_num: # 합성수면 여기 기준으로 좌우로 나뉘니까
                break
            if a_elm % temp_num == 0:
                num_divider += num_count_list[temp_num]
                q = a_elm // temp_num

                # 중복 방지
                if q != temp_num:
                    num_divider += num_count_list[q]    

        result = len_A - num_divider
        res_list.append(result)

    return res_list

```

## Comment
