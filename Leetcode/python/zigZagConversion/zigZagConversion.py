class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list_of_list_row_chars = ["" for _ in range(numRows)]

        j = 0
        plus_minus_multiplier = -1
        for i in range(len(s)):
            list_of_list_row_chars[j] += s[i]
            if j == numRows - 1 or j == 0:
                plus_minus_multiplier = plus_minus_multiplier * -1
            if numRows != 1: # 예외처리..!
                j = j + 1 * plus_minus_multiplier

        result_str = ""
        for row in list_of_list_row_chars:
            result_str += row
        return result_str
