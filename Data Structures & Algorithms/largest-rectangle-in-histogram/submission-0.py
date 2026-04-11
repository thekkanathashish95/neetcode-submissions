class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                pop_i, pop_h = stack.pop()
                pop_area = pop_h * (i - pop_i)
                maxArea = max(maxArea, pop_area)
                start = pop_i
            stack.append((start, h))
        
        for i, h in stack:
            area = h * (len(heights)-i)
            maxArea = max(maxArea, area)

        return maxArea 
        

        