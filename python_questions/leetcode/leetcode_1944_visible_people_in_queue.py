# question link : https://leetcode.com/problems/number-of-visible-people-in-a-queue/
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result= [0] * n
        stack = []
        for i in range (n-1, -1, -1):
            count = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count +=1
            if stack:
                count +=1
                
            stack.append(heights[i])
            result[i] = count
        return result 

        
        