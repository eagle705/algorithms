# Brackets

Determine whether a given string of parentheses is properly nested.

## Task description

A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

* S is empty;
* S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
* S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

```java
class Solution { public int solution(String S); }
```

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Assume that:

* N is an integer within the range [0..200,000];
* string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

Complexity:

* expected worst-case time complexity is O(N);
* expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

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
    list_of_left_brackets_stack = []
    left_brackets = ['(', '{', '[']
    right_brackets = [')', '}', ']']
    left_to_right = {left_brackets[i]:right_brackets[i] for i in range(3)}

    for a_elm in S:
        if a_elm in left_brackets:
            list_of_left_brackets_stack.append(a_elm)
        elif a_elm in right_brackets:

            # case many right
            if len(list_of_left_brackets_stack) == 0:
                return 0
            else:
                pop_left_brackets_val = list_of_left_brackets_stack.pop()
                if a_elm != left_to_right[pop_left_brackets_val]:
                    return 0

    # case many left
    if len(list_of_left_brackets_stack) != 0:
        return 0
    else:
        return 1
```


## Comment
