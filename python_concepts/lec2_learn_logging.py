from loguru import logger
import logging

# decaler variable 
length = 100

# simple print 
print(length)

# Python’s built-in logging module
logging.basicConfig(level=logging.INFO)
logging.info(f"using logging method : the length is {length}")

# using loguru : i have installed this using pip in my system
logger.info(f"using logger method : the length is {length}")


