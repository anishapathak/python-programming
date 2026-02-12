# How will you find out given number by user is even or odd

from loguru import logger
user_input_num = int(input("enter any number between 1 to 100"))
logger.info(type(user_input_num))

if user_input_num % 2 == 0:
    logger.info(f"the number is prime")
else:
    logger.info(f"the number is odd")
logger.info(f"the number you entered is {user_input_num} enjoy")