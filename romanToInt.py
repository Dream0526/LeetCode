
RomanDict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}


Special = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result_list = []
        for item in Special:
            str_count = s.count(item)
            if str_count:
                result_list.append(RomanDict[item]*str_count)
                s = s.replace(item, '')
        if s:
            for item in s:
                result_list.append(RomanDict[item])
        sum = 0
        for data in result_list:
            sum += data
        return sum
