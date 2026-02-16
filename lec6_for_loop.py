from loguru import logger
""" I already know for loop from my c++ days will try to solve 
few questions using python to revise the concepts"""

""" Q1: To practice nested loops print this pattern :
      *
      * *
      * * *
      * * * *
      * * * * *
"""
logger.info(f"Question 1")
# Option 1: 
for i in range(0,5):
    for j in range (0,i):
        # print(f"i:{i}, j: {j} , *")   
        print(f"*",end = " ")
    print("\n") 

# Option 2:
for i in range(0,5):
    print((i+1)*" *")

"""Q2: Print this pattern
      * * * * *
      * * * *
      * * *
      * * 
      * 
      """
logger.info("Question: 2 ")
for i in range(5, 0, -1):
    print(i * " *")


"""Q3: To print all even numbers between 1 to 100"""
logger.info(f"Question 3")

for i in range(11):
    if i%2 == 0:
        print(i)

"""Question 4: Traverse a string and find number of vowels in it"""
logger.info("Question : 4")
input_str = 'Pneumonoultramicroscopicsilicovolcanoconiosis'
count = 0
for char in input_str:
    if char in ["a","e","i","o","u"]:
        count = count + 1
logger.info(f"Total numbers of vowels in input string is : {count}")

"""Question 5 : Traverse a paragraph and find count of word the"""
logger.info("Question: 5")
input_str = "The morning sun rises gently over the quiet city, filling the sky with soft shades of orange and gold. People begin their day with hope, coffee, and small conversations. Birds flutter between trees while traffic slowly increases. Every sunrise brings another chance to learn, grow, and begin again."
input_list = input_str.split(" ")
count = 0
for word in input_list:
    if word.lower() == "the":
        count = count + 1
logger.info(f"the total number of word the in given paragraph is : {count}")

    


