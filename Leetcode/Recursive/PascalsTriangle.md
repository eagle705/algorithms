# Pascal's Triangle

## Task description
There are two important things that one needs to figure out before implementing a recursive function:

- **recurrence relation**: the relationship between the result of a problem and the result of its subproblems.
- **base case**: the case where one can compute the answer directly without any further recursion calls. Sometimes, the base cases are also called bottom cases, since they are often the cases where the problem has been reduced to the minimal scale, i.e. the bottom, if we consider that dividing the problem into subproblems is in a top-down manner.

In the above example, you might have noticed that the recursive solution can incur some duplicate calculations, i.e. we compute the same intermediate numbers repeatedly in order to obtain numbers in the last row. For instance, in order to obtain the result for the number f(5, 3), we calculate the number f(3, 2) twice both in the calls of f(4, 2) and f(4, 3).

We will discuss how to avoid these duplicate calculations in the next chapter of this Explore card.

Following this article, you will find exercises for problems related to Pascal's Triangle.

![pascals](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

## Examples

```
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

## Solution

### Frist
- 메모리 에러남
- Link: https://leetcode.com/submissions/detail/266196396/

```python
class Solution:
    
    def __init__(self):
        self.result = []
        self.count = 1
    
    def generate(self, numRows: int) -> List[List[int]]:
        
        # 첫번째 케이스 처리
        if self.count == 1:
            self.result.append([1])
            self.count += 1
        
        # 종료조건
        if self.count-1 == numRows:
            return self.result
        else:
            # 맨 앞에 [1] 추가
            tmp_list = [1]
            pre_row_idx = self.count-2
            pre_row_num = self.count-1
            
            # 이전꺼 참조해서 더해주기
            for i in range(pre_row_num-1):
                res_num = self.result[pre_row_idx][i] + self.result[pre_row_idx][i+1]
                tmp_list.append(res_num)
                
            # 맨 뒤에 [1] 추가
            tmp_list.append(1)
            self.result.append(tmp_list)            
            self.count += 1
        
        # 재귀 타고가기 
        return self.generate(numRows)
```

## Comment
- 맨 윗줄, 맨 오른쪽, 맨 왼쪽 세 경우에 대해서 예외처리 해주고 풀었음
- class 변수를 사용해서 풀었기 때문에 개인적으로 Recursive하게 풀라는 의도대로 풀진 못한게 아닌가 싶음
- [솔루션](https://leetcode.com/problems/pascals-triangle/solution/)에 따르면 미리 다 만들어 놓은다음에 값을 대입해서 푸는 방식이 제일 깔끔하긴한듯..!
