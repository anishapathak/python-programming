"""

Question:
 
print a star triangle of depth n , where the nth line contains r '*'s.
But there are a couple of conditions to be applied :
    If the n = r then you have the complete triangle
    If the n < r , then you don’t have the complete triangle, in that case, print the incomplete triangles below
    If the n > r , then you have a complete triangle on the bottom , but on top you need to print an inverted triangle
the following examples would explain all the three cases

Example1: depth = 5 and r = 5
Output:
--------------------
    *
   * *
  * * *
 * * * *
* * * * *
--------------------

Example2: for  depth = 3 and r = 7
Output:
--------------------
  * * * * * 
 * * * * * *
* * * * * * * 
--------------------

Example 3: for  depth = 11 and r = 5
Output:
--------------------  
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *




* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *

--------------------
"""


def traingle(depth, r):
    j = 1
    for i in range (depth):
        if j != r :
            print(" "*i,  "*"*j)
            j += j

traingle(5,5)