# CountSemiprimes

Count the semiprime numbers in the given range [a..b]

## Task description

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty zero-indexed arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

The number of semiprimes within each of these ranges is as follows:

* (1, 26) is 10,
* (4, 10) is 4,
* (16, 20) is 0.

Write a function:

```java
class Solution { public int[] solution(int N, int[] P, int[] Q); }
```

that, given an integer N and two non-empty zero-indexed arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

the function should return the values [10, 4, 0], as explained above.

Assume that:

* N is an integer within the range [1..50,000];
* M is an integer within the range [1..30,000];
* each element of arrays P, Q is an integer within the range [1..N];
* P[i] ≤ Q[i].

Complexity:

* expected worst-case time complexity is O(N*log(log(N))+M);
* expected worst-case space complexity is O(N+M), beyond input storage (not counting the storage required for input arguments).

## Solution

### First

* Programming language: Python
* Task score:
* Analysis
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, P, Q):
    # write your code in Python 3.6
    # semiprime을 위한 소수 찾기, O(N)
    import math
    prime_list = []
    for i in range(N//2):
        if i == 0:
            continue
        num = i+1
        count = 0
        for j in range(num):
            if j == 0: continue
            if num % j == 0:
                divider_product_term = num // j
                count +=1
            if j > math.sqrt(num) and count == 1:
                # this is prime
                # 1.14는.. 안되네
                prime_list.append(num)
                break
            elif num == 2:
                prime_list.append(num)

    import itertools
    # 소수 중복조합 찾기 itertools
    comb_list = list(itertools.combinations_with_replacement(prime_list, 2))
    comb_list = [comb[0]*comb[1] for comb in comb_list if comb[0]*comb[1] <= N]
    comb_list.sort()
    # print("comb_list: ", comb_list)

    # 범위 내에서 semiprime 개수 찾기 (이게 좀 어렵네)
    count_res_list = []
    for i in range(len(P)):
        count = 0
        for comb in comb_list:
            if P[i] <= comb and comb <= Q[i]:
                count += 1
        count_res_list.append(count)
    return count_res_list

```

## Comment
