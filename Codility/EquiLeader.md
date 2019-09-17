# EquiLeader

Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.

## Task description

A non-empty zero-indexed array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

we can find two equi leaders:

* 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
* 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.

The goal is to count the number of equi leaders.

Write a function:

```java
class Solution { public int solution(int[] A); }
```

that, given a non-empty zero-indexed array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

the function should return 2, as explained above.

Assume that:

* N is an integer within the range [1..100,000];
* each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

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
    num_to_list_of_index = {}
    num_to_count = {}
    max_num = -99999999999
    max_count = 0

    # if len(A) == 1:
    #     return 0

    for i, a_elm in enumerate(A):
        if a_elm not in num_to_list_of_index:
            num_to_list_of_index[a_elm] = [i]
            num_to_count[a_elm] = 1
        else:
            num_to_list_of_index[a_elm].append(i)
            num_to_count[a_elm] += 1

        if max_count < num_to_count[a_elm]:
            max_count = num_to_count[a_elm]
            max_num = a_elm


    if max_num in num_to_list_of_index:
        list_of_max_num_index = num_to_list_of_index[max_num]
    else:
        list_of_max_num_index = None
        max_count = 0
        for num, list_of_index in num_to_list_of_index.items():
            if max_count < len(list_of_index):
                max_count = len(list_of_index)
                list_of_max_num_index = list_of_index

    total_count_len = len(list_of_max_num_index)
    total_len = len(A)
    res_count = 0

    import math
    # for i, max_num_index in enumerate(list_of_max_num_index):
    #     left_len = max_num_index + 1
    #     left_count = i + 1

    #     right_len = total_len - left_len
    #     right_count = total_count_len - left_count

    #     left_more_than_half = int(left_len / 2) + 1 if int(left_len / 2) == left_len / 2 else math.ceil(left_len / 2)

    #     right_more_than_half = int(right_len / 2) + 1 if int(right_len / 2) == right_len / 2 else math.ceil(right_len / 2)

    #     if (left_count >= left_more_than_half) and (right_count >= right_more_than_half):
    #         res_count += 1


    left_count_arr = []
    for i, max_num_index in enumerate(list_of_max_num_index):

        if i == len(list_of_max_num_index) - 1:
            to_next_length = total_len - max_num_index
        else:
            to_next_length = list_of_max_num_index[i+1] - list_of_max_num_index[i]
        left_count_arr.extend([i + 1] * (to_next_length))

    # print("left_count_arr: ", left_count_arr)


    for i in range(total_len):
        left_len = i + 1
        left_count = left_count_arr[i]
        # left_count = 0
        # for max_num_index in list_of_max_num_index:
        #     if max_num_index <= i:
        #         left_count += 1
        #     else:
        #         break

        right_len = total_len - left_len
        right_count = total_count_len - left_count


        left_more_than_half = int(left_len / 2) + 1 if int(left_len / 2) == left_len / 2 else math.ceil(left_len / 2)

        right_more_than_half = int(right_len / 2) + 1 if int(right_len / 2) == right_len / 2 else math.ceil(right_len / 2)

        if (left_count >= left_more_than_half) and (right_count >= right_more_than_half):
            res_count += 1

    return res_count
```


## Comment
