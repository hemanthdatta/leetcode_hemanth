class Solution:
    def isValid(self, s: str) -> bool:
        opened=['(','[','{']
        close=[')',']','}']
        stack=[]
        for x in s:
            if x in opened:
                stack.append(x)
            else:
                if len(stack)!= 0 and stack[-1]==opened[close.index(x)]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0



        