class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        if string == string[::-1]:
            return True
        return False
