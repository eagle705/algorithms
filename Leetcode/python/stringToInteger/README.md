### 8. String to Integer (atoi)
- 포인트
    - 정규식으로 처리하면 그냥 한방에 끝..
    - 숫자들을 리스트에 넣어놓고.. 처리
    - 예외처리 중요함
    - 더 나은 풀이 있을 것 -_ -;

```
String to Integer (atoi)
Medium

1060

6628

Favorite

Share
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−2^31) is returned.
```

- my code

```python
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MIN = -1 * pow(2, 31)
        INT_MAX = 1 * pow(2, 31) - 1
        number_str_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        number_and_ops_str_list = number_str_list + ["+", "-"]
        str = str.strip()
        if str == "":
            return 0

        if str[0] not in number_and_ops_str_list or str == "+" or str == "-":
            return 0
        else:
            result_str = ""
            for i, str_elm in enumerate(str):
                if i != 0 and str_elm not in number_str_list:
                    break
                result_str += str_elm
            if len(result_str) == 1 and result_str not in number_str_list:
                return 0
            else:
                result_str = int(result_str)
                if result_str >= INT_MAX:
                    return INT_MAX
                elif result_str <= INT_MIN:
                    return INT_MIN
                else:
                    return result_str                
```

- result
```
Success
Runtime: 40 ms, faster than 74.91% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.1 MB, less than 5.95% of Python3 online submissions for String to Integer (atoi).
```
