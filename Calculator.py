import SLLStack


class Calculator:
    def __init__(self):
        self.dict = None

    def balanced_parens(self, s: str) -> bool:
        """
        This function checks if the string s contains balanced parentheses
        :param s: str type; the string to be checked
        :return: bool type; True if the string s contains balanced parentheses
        """
        # FIXME: Copy-paste your implementation from Module 2.  Adapt it so that it works with SLLQueue
        
        stack = SLLStack.SLLStack()
        for i in s:
            if i == '(':
                stack.push(i)
            elif i == ')':
                if stack.size() == 0:
                    return False
                stack.pop()
        return True if stack.size() == 0 else False
