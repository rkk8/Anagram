class Solution:
    def isPalindrome(self, x: int) -> bool:
        num2st = str(x)
        lp=0
        rp=len(num2st)-1
        while lp <= rp:
            if num2st[lp]==num2st[rp]:
                rp -=1
                lp +=1
                print('This may be a palendrome...')
            else:
                print('This is not a palendrome.')
                return False
        print('This is a Palindrome')
        return True

Solution= Solution()
Solution.isPalindrome(1412141)


