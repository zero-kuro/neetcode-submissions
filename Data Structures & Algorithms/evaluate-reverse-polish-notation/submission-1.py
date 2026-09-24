class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = "+-*/"
        for i in tokens:
            if i in operands:
                r = stack.pop()
                l = stack.pop()
                if i == '+':
                    new = int(l) + int(r)
                if i == '-':
                    new = int(l) - int(r)
                if i == '*':
                    new = int(l) * int(r)
                if i == '/':
                    new = int(int(l) / int(r))
                stack.append(new)
            else:       
                stack.append(int(i))
        
        return stack[0]
        