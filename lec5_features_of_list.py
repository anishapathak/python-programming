from loguru import logger

# 1. list can contain duplicates
dup_list = [1,1,1,2,2,3,3,4]
logger.info(f"list can contain duplicates example : {dup_list}")

""" list if mutable : basically can changes form example : list item can change we can append insert or extend,
also we can replaxce values i within list hence its mutable , also it can store mutiple data type"""

hetro_list = ['1', 1, True, 1.1]
logger.info(f"a single list can store items of different data types exmaple : {hetro_list}")

# 2. Adding two list so instead of using extend qwe can simple add two list and it will work as extend 
list1 = [1,2]
list2 = [3,4]
logger.info(f"example of adding two list list1+list2 is : {list1 + list2}")

# 3. Appending one list in another list 
list1 = [1,2]
list2 = [3,4]
list1.append(list2)
logger.info(f"print result of appending two list is {list1}")

# 4. Insert and pop methods
"""
1. insert() method is used to insert data at nth position , index is compulsory argument
2. pop() is used to remove data from nth postion if index is not passed 
then it will remove last element"""

# insert expample 
list2.insert(10,12)
logger.info(f"after inserting an element in end {list2}")

# pop example
list2.pop()
logger.info(f"list2 after poping last element {list2}")

# 5. Index method : this is used to find an elemnet first occurence and its index value
list1.append(2)
logger.info(list1.index(2))

# 5. split method : this is used to split a string into a list depending on splitting value
split_string = "sec1_sec2_sce3_sce4_sec5_sec6_sec7"
split_list = split_string.split('_')
logger.info(split_list)
