sth = ['(', ')', '[', ']', '{', '}']

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        while True:
            first = len(s)
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            after = len(s)
            if first == after:
                break
        if s:
            string_list = list(s)
            tmp_list = []
            head = []
            tail = []
            for letter in string_list:
                if letter in sth:
                    tmp_list.append(letter)
            head = tmp_list[:int(len(tmp_list)/2)]
            tail = tmp_list[int(len(tmp_list)/2):][::-1]
            if len(head) == len(tail):
                for index in range(len(head)):
                    if abs((ord(tail[index]) - ord(head[index]))) > 2:
                        return False
                    if (ord(tail[index]) - ord(head[index])) == 0:
                        return False
                return True

            else:
                return False
        else:
            return True
