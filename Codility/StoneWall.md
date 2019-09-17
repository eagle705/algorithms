# StoneWall

Cover "Manhattan skyline" using the minimum number of rectangles.

## Task description

You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by a zero-indexed array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

```java
class Solution { public int solution(int[] H); }
```

that, given a zero-indexed array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:

    H[0] = 8    H[1] = 8    H[2] = 5
    H[3] = 7    H[4] = 9    H[5] = 8
    H[6] = 7    H[7] = 4    H[8] = 8

the function should return 7. The figure shows one possible arrangement of seven blocks.

Assume that:

* N is an integer within the range [1..100,000];
* each element of array H is an integer within the range [1..1,000,000,000].

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

def solution(H):
    # write your code in Python 3.6
    big_rectangle_stack = []

    num_of_blocks = 0
    for h_elm in H:
        big_rectangle_stack = [q for q in big_rectangle_stack if q <= h_elm]        
        if h_elm in big_rectangle_stack:
            pass
        else:
            big_rectangle_stack.append(h_elm)
            num_of_blocks += 1

    return num_of_blocks

# 위에껀 속도가 좀 느림.. 아래껀 메모리를 좀 더 쓰는대신에 속도가 빠름
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    big_rectangle_stack = []
    dict_for_cotain_check = {}

    num_of_blocks = 0
    for h_elm in H:
        # big_rectangle_stack = [q for q in big_rectangle_stack if q <= h_elm]
        while(True):
            if len(big_rectangle_stack) != 0 and h_elm < big_rectangle_stack[-1]:
                val = big_rectangle_stack.pop()
                del dict_for_cotain_check[val]
            else:
                break

        if h_elm in dict_for_cotain_check:
            pass
        else:
            big_rectangle_stack.append(h_elm)
            num_of_blocks += 1
            dict_for_cotain_check[h_elm] = 0 # it could be anything.

    return num_of_blocks    

```

## Comment
