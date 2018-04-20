MIN = -(2**31)
MAX = 2**31-1


class Solution(object):


    def reverse(self, num):
        
        if num == 0:
            return 0
        string = str(num)
        reverse_string = string[::-1]
        while True:
            if reverse_string[0] == '0':
                reverse_string = reverse_string[1:]
            else:
                break
        if reverse_string[-1] == '-':
            reverse_num = eval('-'+reverse_string[:-1])
            print(reverse_num)
        else:
            reverse_num = eval(reverse_string)
        
        if MIN<=reverse_num<=MAX:
            return reverse_num
        else:
            return 0
