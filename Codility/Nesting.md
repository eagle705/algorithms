# Nesting

Determine whether given string of parentheses is properly nested.

## Task description

A string S consisting of N characters is called properly nested if:

* S is empty;
* S has the form "(U)" where U is a properly nested string;
* S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

```java
class Solution { public int solution(String S); }
```

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Assume that:

* N is an integer within the range [0..1,000,000];
* string S consists only of the characters "(" and/or ")".

Complexity:

* expected worst-case time complexity is O(N);
* expected worst-case space complexity is O(1) (not counting the storage required for input arguments).

## Solution

### First

* Programming language: Python
* Task score:
* Analysis
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    left_brackets_stack = []
    for s_elm in S:
        if s_elm == '(':
            left_brackets_stack.append(s_elm)
        else:
            if len(left_brackets_stack) == 0:
                return 0
            left_brackets_stack.pop()
    if len(left_brackets_stack) != 0:
        return 0
    else:
        return 1
```

## Comment
