class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = '+-*/'
        stk = []
        for t in tokens:
            if t not in operators:
                stk.append(int(t))
            else:
                if stk:
                    b, a = stk.pop(), stk.pop()
                    if t == "+":
                        stk.append(a + b)
                    elif t == "-":
                        stk.append(a - b)
                    elif t == "*":
                        stk.append(a * b)
                    else:
                        stk.append(int(a / b))

        return stk[0]

                