class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_of_substring = []
        max_substr_len = 0
        for s_elm in s:
            if len(list_of_substring) == 0:
                list_of_substring.append(s_elm)
            else:
                if s_elm in list_of_substring:
                    substr_len = len(list_of_substring)
                    if substr_len > max_substr_len:
                        max_substr_len = substr_len
                    pre_duplicated_index = list_of_substring.index(s_elm) # 필수
                    list_of_substring.append(s_elm)
                    list_of_substring = list_of_substring[pre_duplicated_index+1:]
                else:
                    list_of_substring.append(s_elm)

        substr_len = len(list_of_substring)
        if substr_len > max_substr_len:
            max_substr_len = substr_len
        return max_substr_len
