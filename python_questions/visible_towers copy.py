"""
This is a classic “visible towers” / “next greater element” type problem 👌

From each tower, you can see towers to the right until a taller tower blocks the view.

From your example:

[1, 5, 10, 7, 9]


From 1 → can see 5 and 10 (10 blocks further view) → 2

From 5 → can see 10 → 1

From 10 → can see 7 and 9 → 2

From 7 → can see 9 → 1

From 9 → can see none → 0

Expected output:

[2, 1, 2, 1, 0]
"""

def visible_towers_stack(arr):
    n = len(arr)
    result = [0] * n
    stack = []
    
    for i in range(n - 1, -1, -1):
        count = 0
        
        # Pop all smaller towers
        while stack and stack[-1] < arr[i]:
            stack.pop()
            count += 1
        
        # If stack not empty, one taller tower is visible
        if stack:
            count += 1
        
        result[i] = count
        stack.append(arr[i])
    
    return result


arr = [1, 5, 10, 7, 9]
stack = []
print(stack)
# print(visible_towers_stack(arr))



