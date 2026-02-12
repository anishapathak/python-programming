from loguru import logger

list_of_names = ['anisha', 'manisha', 'kanisha', 'paanisha', 'anipathak']

logger.info("intial list {list_of_names}")
logger.info(type(list_of_names))
# to print first element
logger.info(f"first elemenet is {list_of_names[0]}")
# to print last element
logger.info(f"last element {list_of_names[-1]}")


# add one more item to list
list_of_names.append('anispa')
logger.info(f"after appending {list_of_names}")

# add a list of name to existing list 
new_list_of_names = ['gullu', 'arpu', 'Joy', 'Chota', 'Nanho']
list_of_names.extend(new_list_of_names)
logger.info(f"after appneding another list in existing list : {list_of_names}")

# add one item in firt place in list
list_of_names.insert(0, 'pathak')
logger.info(f"after adding one item in front of list {list_of_names}")

# size of list

logger.info(f"the size of list is: {len(list_of_names)}")