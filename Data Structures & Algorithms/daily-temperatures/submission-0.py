class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                prev_i = stk.pop()
                output[prev_i] = i-prev_i

            stk.append(i)

        return output