class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        tmp_str = []
        result_list = []
        strs = [list(item) for item in strs]
        while True:
            for str_list in strs:
                try:
                    tmp_str.append(str_list.pop(0))
                except IndexError:
                    break
            if len(tmp_str) != len(strs):
                break
            if len(set(tmp_str)) == 1:
                result_list.append(tmp_str[0])
                tmp_str = []
            else:
                break
        long_prefix = ''
        if result_list:
            for item in result_list:
                long_prefix += item
        return long_prefix