# [MaxNonoverlappingSegments](https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/)

Find a maximal set of non-overlapping segments.

## Task description

Located on a line are N segments, numbered from 0 to N − 1, whose positions are given in arrays A and B. For each I (0 ≤ I < N) the position of segment I is from A[I] to B[I] (inclusive). The segments are sorted by their ends, which means that B[K] ≤ B[K + 1] for K such that 0 ≤ K < N − 1.

Two segments I and J, such that I ≠ J, are overlapping if they share at least one common point. In other words, A[I] ≤ A[J] ≤ B[I] or A[J] ≤ A[I] ≤ B[J].

We say that the set of segments is non-overlapping if it contains no two overlapping segments. The goal is to find the size of a non-overlapping set containing the maximal number of segments.

For example, consider arrays A, B such that:

    A[0] = 1    B[0] = 5
    A[1] = 3    B[1] = 6
    A[2] = 7    B[2] = 8
    A[3] = 9    B[3] = 9
    A[4] = 9    B[4] = 10
The segments are shown in the figure below.

![images](https://codility-frontend-prod.s3.amazonaws.com/media/task_static/max_nonoverlapping_segments/static/images/auto/68b279360bc48af61d9d3bdfbe1d30fe.png)

The size of a non-overlapping set containing a maximal number of segments is 3. For example, possible sets are {0, 2, 3}, {0, 2, 4}, {1, 2, 3} or {1, 2, 4}. There is no non-overlapping set with four segments.

Write a function:
```
def solution(A, B)
```
that, given two arrays A and B consisting of N integers, returns the size of a non-overlapping set containing a maximal number of segments.

For example, given arrays A, B shown above, the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

- N is an integer within the range [0..30,000];
- each element of arrays A, B is an integer - within the range [0..1,000,000,000];
- A[I] ≤ B[I], for each I (0 ≤ I < N);
- B[K] ≤ B[K + 1], for each K (0 ≤ K < N − 1).

## Solution

### First

* Programming language: Python
* Task score:
    - Correctness: 
    - Performance: 
* Analysis
    
* Link: 
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    num_to_list_of_non_overlap = {}
    for i in range(len(A)-1):
        if i not in num_to_list_of_non_overlap:
            num_to_list_of_non_overlap[i] = []
        for j in range(len(A)-i-1):
            back = i+j+1
            if (A[i] < A[back] and B[i] <= A[back]):
                num_to_list_of_non_overlap[i].append(back)
    num_to_list_of_non_overlap[len(A)-1] = []
    
                    
    # 개수만큼 중복 카운트 되긴 할듯..    
    seg_len_to_count = {len(A): 1}
    max_seg_len_num = 0
    max_count = 0
    for i in range(len(A)):
        seg_len = len(num_to_list_of_non_overlap[i])
        if seg_len not in seg_len_to_count:
            seg_len_to_count[seg_len] = 1
        else:
            seg_len_to_count[seg_len] += 1
            if max_count < seg_len_to_count[seg_len]:
                max_count = seg_len_to_count[seg_len]
                max_seg_len_num = seg_len
    # print("max_seg_len_num: ", max_seg_len_num)
    return max_seg_len_num
```


## Comment
- 아.. 서로 안겹치는것 까진 찾았는데.. 개수 조합하는데서 막혔음..
- 그리디도 어렵게 느껴질떄가 있네..
- https://app.codility.com/demo/results/trainingFYRGD6-YME/

