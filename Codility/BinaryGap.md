# BinaryGap

Find longest sequence of zeros in binary representation of an integer.

## Task description

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.

Write a function:

```java
class Solution { public int solution(int N); }
```

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

* N is an integer within the range [1..2,147,483,647].

Complexity:

* expected worst-case time complexity is O(log(N));
* expected worst-case space complexity is O(1).

## Solution

### Frist

* Programming language: Python
* Task score: 100%
* Analysis summary:
* Link: https://app.codility.com/demo/results/trainingW9QFPN-GBP/
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary_str = format(N, 'b')
    reversed_binary_list = list(binary_str)
    reversed_binary_list.reverse()
    try:
        
        index = reversed_binary_list.index('1')
        reversed_binary_list = reversed_binary_list[index:]
    except:
        return 0
    
    count = 0
    max_count = 0
    for b in reversed_binary_list:
        if b == '1':
            count = 0
        else:
            count += 1
            if max_count < count:
                max_count = count
                
    return max_count
```

## Comment
- 사실은 좀 불필요한 코드가 많다
- 뒤에 0 남아 있는거 체크하는거 귀찮아서 그냥 뒤집은 다음에 다 버렸다..
- 뒤집은 후에 index 함수로 1이 나오는 포지션을 뽑아서 했는데 예외처리하는게 영 보기 안좋아서 그냥 루프돌리는게 나은가 싶기도하다
- format(N, 'b') 로 이진법 바꾸는거랑 if 문에서 '1' 로 스트링 형태의 숫자로 비교하는게 포인트였음

