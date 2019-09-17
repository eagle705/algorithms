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
